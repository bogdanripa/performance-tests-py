import urllib3
import os
import time

def lambda_handler(event):
    print('START')
    start_time = time.time()
    
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://d33b1b0c-a88c-44eb-9047-8f57a3fe1166.eu-central-1.cloud.genez.io')
    #os.environ['GENEZIO_CHILD_URL'])
    fetch_time = int((time.time() - start_time) * 1000)  # milliseconds

    if response.status != 200:
        raise Exception(f'Network response was not ok: {response.status}')

    print(f'DONE in {fetch_time}ms')

    return {
        'statusCode': 200,
        'body': str(fetch_time)
    }
