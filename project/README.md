# 14848_project
# Docker image used  
jupyter notebook  
https://hub.docker.com/r/chenghuajie/jupyternotebook (source code under jupyternotebook)

spark  
https://hub.docker.com/r/bitnami/spark

hadoop  
https://hub.docker.com/r/bde2020/hadoop-datanode  
https://hub.docker.com/r/bde2020/hadoop-namenode

sonar  
https://hub.docker.com/r/chenghuajie/sonar (source code under sonar)

GUI  
https://hub.docker.com/r/chenghuajie/gui (source code under GUI)

# Kubernetes deployment
1.
Create a cluster using
```sh
gcloud container clusters create --machine-type n1-standard-2 --num-nodes 2 \
--zone us-central1-a --cluster-version latest {clustername}
```
2.
Reserve a static ip address   
On google cloud, find VPC network-> External IP addresses and then click on RESERVE STATIC ADDRESS and create a static ip address
![alt text](https://github.com/Huajiecheng/14848_hw/blob/main/project/screenshots/static_ip.JPG?raw=true)

3.  
Change the loadBalancerIP in yaml files under kubernetes folder with the obtained static ip address    
Files to change are gui.yaml, jupyternotebook.yaml, sonar.yaml, spark.yaml, hadoop/namenode-service.yaml

4.
Upload all the kubernetes folder to cloud storage with a bucket named 14848-project
![alt text](https://github.com/Huajiecheng/14848_hw/blob/main/project/screenshots/bucket.JPG?raw=true)

5.
Open cloud shell and copy the kubernetes folder to the cluster
```sh
gsutil cp -r gs://14848-project/ .
```
6.
Apply all the yaml file in the kubernetes folder to deploy and build up service for applications  
```sh
cd 14848-project/kubernetes
kubectl apply -R -f .
```
![alt text](https://github.com/Huajiecheng/14848_hw/blob/main/project/screenshots/apply_yaml.JPG?raw=true)

7.
Change config json file under static folder in the gui pods with the static ip address obtained before using vim
```sh
kubectl get pods
kubectl exec -it {gui pod name} -- /bin/sh
```
![alt text](https://github.com/Huajiecheng/14848_hw/blob/main/project/screenshots/change_config.JPG?raw=true)

8.
Now the application is ready to use and we can check the pods. Then we can access the link of gui.
![alt text](https://github.com/Huajiecheng/14848_hw/blob/main/project/screenshots/all_pods.JPG?raw=true)
![alt text](https://github.com/Huajiecheng/14848_hw/blob/main/project/screenshots/deployment.JPG?raw=true)
![alt text](https://github.com/Huajiecheng/14848_hw/blob/main/project/screenshots/service.JPG?raw=true)

9.
demo video: https://drive.google.com/file/d/1KZJ8kd2NiBqCP-0h72KXTovpngKoHznK/view?usp=sharing
