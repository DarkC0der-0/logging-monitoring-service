import json
from app import create_app
from app.routes import upload_image

app = create_app()

def handler(event, context):
    with app.app_context():
        response = app.test_client().post('/upload', data=event['body'])
        return {
            'statusCode': response.status_code,
            'body': response.data.decode('utf-8')
        }