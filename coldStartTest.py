import requests
import os
import time

def lambda_handler(event):
    print('START')
    start_time = time.time()
    
    response = requests.get(os.environ['GENEZIO_CHILD_URL'])
    fetch_time = int((time.time() - start_time) * 1000)  # milliseconds

    if not response.ok:
        raise Exception(f'Network response was not ok: {response.status_code} {response.reason}')

    print(f'DONE in {fetch_time}ms')

    return {
        'statusCode': 200,
        'body': str(fetch_time)
    }
