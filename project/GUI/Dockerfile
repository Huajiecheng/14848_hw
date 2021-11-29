FROM python:latest
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get -y install vim
WORKDIR /usr/src/myapp/flask_web
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]