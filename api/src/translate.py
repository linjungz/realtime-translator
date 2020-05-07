import boto3
import json
import time
import urllib

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print(event)

    if event['queryStringParameters'] :
        input_text = event['queryStringParameters']['text'] 
        print(input_text)
        msg = translate(input_text, 'en', 'zh')['TranslatedText']
        print(msg)
        status_code = 200
    else:
        msg = "Error"
        status_code = 400

    return {
        "headers": {
            'Access-Control-Allow-Origin' : '*'
        },
        "statusCode": status_code,
        "body": json.dumps({
            "message": msg,
        },ensure_ascii=False),
    }

def translate(text, source_language_code, target_language_code):
    mytranslate = boto3.client('translate')

    translated_text = mytranslate.translate_text(
    Text=text,
    SourceLanguageCode= source_language_code,
    TargetLanguageCode= target_language_code)

    return translated_text
