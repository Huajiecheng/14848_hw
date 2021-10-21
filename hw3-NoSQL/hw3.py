import boto3
import csv

# read key and secret
with open('new_user_credentials.csv', 'r') as csvfile:
	csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(csvf)
	for item in csvf:
		access_key = item[2]
		secret_key = item[3]

# create an s3 instance object
s3 = boto3.resource('s3',
 aws_access_key_id=access_key ,
 aws_secret_access_key=secret_key
)

bucket_name = "datacont-huajiec"
try:
	s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
	'LocationConstraint': 'us-west-2'})
except Exception as e:
	print (e)

bucket = s3.Bucket(bucket_name)
bucket.Acl().put(ACL='public-read')

# create the DynamoDB table
dyndb = boto3.resource('dynamodb',
 region_name='us-west-2',
 aws_access_key_id=access_key ,
 aws_secret_access_key=secret_key 
)

try:
	table = dyndb.create_table(TableName='DataTable',
		KeySchema=[
			{
			'AttributeName': 'PartitionKey',
			'KeyType': 'HASH'
			},
			{
			'AttributeName': 'RowKey',
			'KeyType': 'RANGE'
			}
			],
		AttributeDefinitions=[
			{
			'AttributeName': 'PartitionKey',
			'AttributeType': 'S'
			},
			{
			'AttributeName': 'RowKey',
			'AttributeType': 'S'
			},
		],
		ProvisionedThroughput={
			'ReadCapacityUnits': 5,
			'WriteCapacityUnits': 5
		}
	)
except Exception as e:
	print (e)

#if there is an exception, the table may already exist. if so...
table = dyndb.Table("DataTable")


table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')

print(table.item_count)

# reading the csv file, uploading the blobs and creating the table
with open('data/experiments.csv', 'r') as csvfile:
	csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(csvf)
	for item in csvf:
		print(item)
		body = open("data/" + item[4], 'rb')
		s3.Object(bucket_name, item[4]).put(Body=body )
		md = s3.Object(bucket_name, item[4]).Acl().put(ACL='public-read')

		url = "https://s3-us-west-2.amazonaws.com/"+bucket_name+"/"+item[4]
		metadata_item = {'PartitionKey': item[4].split(".")[0], 'RowKey': item[0], 
		'Temp': item[1], 'Conductivity': item[2] , 'Concentration' : item[3], 'url':url} 
		try:
			table.put_item(Item=metadata_item)
		except:
			print("item may already be there or another failure")
