"""
Links:
- https://pypi.org/project/Flask/
- https://flask.palletsprojects.com/en/2.1.x/installation/
- https://stackoverflow.com/questions/39406177/managing-contents-of-requirements-txt-for-a-python-virtual-environment
- https://www.elastic.co/guide/en/apm/agent/python/current/flask-support.html

"""

from flask import Flask
from elasticapm.contrib.flask import ElasticAPM

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'FlaskApp',
    'SECRET_TOKEN': '',
    'SERVER_URL': 'http://localhost:8200',
    'ENVIRONMENT': 'production',
    'DEBUG': True
}

apm = ElasticAPM(app)

#apm = ElasticAPM(app, service_name='FlaskApp', secret_token='')

@app.route('/')
def hello_world():
   return 'Hello Worlffd'

if __name__ == '__main__':
   app.run(debug=True)