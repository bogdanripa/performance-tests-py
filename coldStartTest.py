import requests
import os
import time

def lambda_handler(event):
    print('START')
    start_time = time.time()
    
    response = requests.get('https://b58073ee-f2a6-4282-8c57-6d29d6eed81e.eu-central-1.cloud.genez.io')
    #os.environ['GENEZIO_CHILD_URL'])
    fetch_time = int((time.time() - start_time) * 1000)  # milliseconds

    if not response.ok:
        raise Exception(f'Network response was not ok: {response.status_code} {response.reason}')

    print(f'DONE in {fetch_time}ms')

    return {
        'statusCode': 200,
        'body': str(fetch_time)
    }
