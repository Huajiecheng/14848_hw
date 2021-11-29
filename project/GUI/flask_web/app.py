from flask import Flask, render_template
import json

app = Flask(__name__)

links_name = ["hadoop_port", "sonar_port", "jupyter_port", "spark_port"]

@app.route('/')
def index():
    f = open('./static/config.json', "r")
    config = json.loads(f.read())
    f.close()
    url_config = {}
    for i in links_name:
        url_config[i] = "http://" + config["ip"] + ":" + config[i] 
    return render_template('index.html', config=url_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)