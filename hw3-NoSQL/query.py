import boto3
import csv

# read key and secret
with open('new_user_credentials.csv', 'r') as csvfile:
	csvf = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(csvf)
	for item in csvf:
		access_key = item[2]
		secret_key = item[3]

# access dynamo service
dyndb = boto3.resource('dynamodb',
 region_name='us-west-2',
 aws_access_key_id=access_key ,
 aws_secret_access_key=secret_key 
)

# specify the table
table = dyndb.Table("DataTable")
table.meta.client.get_waiter('table_exists').wait(TableName='DataTable')

# pull 'PartitionKey': 'exp1', 'RowKey': '1'
print("pull 'PartitionKey': 'exp1', 'RowKey': '1'")
response = table.get_item(
    Key={
        'PartitionKey': 'exp1',
        'RowKey': '1'
    }
)
item = response['Item'] 
print(item)
print()

# pull 'PartitionKey': 'exp2', 'RowKey': '2'
print("pull 'PartitionKey': 'exp2', 'RowKey': '2'")
response = table.get_item(
    Key={
        'PartitionKey': 'exp2',
        'RowKey': '2'
    }
)
item = response['Item'] 
print(item)
print()

# pull 'PartitionKey': 'exp3', 'RowKey': '3'
print("pull 'PartitionKey': 'exp3', 'RowKey': '3'")
response = table.get_item(
    Key={
        'PartitionKey': 'exp3',
        'RowKey': '3'
    }
)
item = response['Item'] 
print(item)
print()
