import requests
import os
import time

def lambda_handler(event):
    print('START')
    start_time = time.time()
    
    response = requests.get('https://d33b1b0c-a88c-44eb-9047-8f57a3fe1166.eu-central-1.cloud.genez.io')
    #os.environ['GENEZIO_CHILD_URL'])
    fetch_time = int((time.time() - start_time) * 1000)  # milliseconds

    if not response.ok:
        raise Exception(f'Network response was not ok: {response.status_code} {response.reason}')

    print(f'DONE in {fetch_time}ms')

    return {
        'statusCode': 200,
        'body': str(fetch_time)
    }
