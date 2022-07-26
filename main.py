import os
import json
import time
import requests
from download_image import download_image as dl

# set the url api
API_URL = 'https://sindomall.com/api/get-post-product-data-by-region-and-date'
# set the parameters
PARAM = {
    'server_key': 'c36edcc96abfc7f5a07db022f2c3b096',
    'region_name': 'batu',
    'start_date': '2022-07-21',
    'to_date': '2022-07-21'
}
# set directory name to save the image
IMAGE_DIR = 'images'

# download images
dl(API_URL, IMAGE_DIR, PARAM)

exit()
time.sleep(300)
response = requests.post(API_URL, PARAM)  # Fetch the data from the API

# check response status
if response.status_code == 200 and response.json()['api_status'] == 200:
    data_count = response.json()['total_data']  # Extract total data
    data_product = response.json()['data']  # Extract data product

    print(str(data_count) + ' posts has found, this will take a while please wait...')
    for index, product in enumerate(data_product):  # loop over each posts
        if index % 100 == 0 and index != 0:  # when it reaches 100 posts, then let the machine rest for 5 minutes
            sleep_minutes = 5  # set the sleep minutes
            # print the rest message
            print(f'Let the machine rest for {sleep_minutes} minutes...')
            time.sleep(sleep_minutes * 60)  # sleep for * minutes

        print(index, '=', product['product_name'])
else:
    print('data not found !')