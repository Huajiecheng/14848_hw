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

terminal  
https://hub.docker.com/r/chenghuajie/terminal (source code under terminal)

# Kubernetes deployment
Current work is on local machine and result of each application has a screenshot.  
1.  
use kubectl apply -f with filename and the yaml file in the kubernetes folder to deploy and build up service for applications.  
2.  
use kubectl run -i --tty terminal --image=chenghuajie/terminal to run the terminal.  
With input option, the link to each application will be printed out.  
All the ports are hardcoded with the ip as localhost now.  
