import boto3
import json
import time
import urllib
import os


def lambda_handler(event, context):
    print(event)

    bucket_name = os.environ['BucketName']

    if event['queryStringParameters'] :
        input_text = event['queryStringParameters']['text'] 
        print(input_text)
        url = polly(input_text, 'Zhiyu', bucket_name)
        print(url)
        status_code = 200
    else:
        url = "Error"
        status_code = 400

    return {
        "headers": {
            'Access-Control-Allow-Origin' : '*'
        },
        "statusCode": status_code,
        "body": json.dumps({
            "url": url
        }),
    }

def polly(text, voice_id, bucket_name):
    mypolly = boto3.client('polly')
    mys3 = boto3.client('s3')

    response = mypolly.synthesize_speech(
        VoiceId = voice_id,
        OutputFormat = "mp3",
        Text = text)

    print(response)

    tmp_path = '/tmp/speech.mp3'

    file = open(tmp_path, 'wb')
    file.write(response['AudioStream'].read())
    file.close()

    key = 'output/' + str(time.time_ns()) + '.mp3'

    mys3.upload_file(tmp_path, bucket_name, key)
    presigned_url = mys3.generate_presigned_url(
        'get_object',
        Params={
            'Bucket' : bucket_name,
            'Key' : key
        })
    
    return presigned_url