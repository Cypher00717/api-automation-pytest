from Utils.sanitizer import sanitize_payload, sanitize_response
from Utils.logger import logger

import requests


class AuthClient:
    def __init__(self, base_url, auth_token):
        self.base_url = base_url
        self.auth_token = auth_token

    def post(self, endpoint, payload):
        url = self.base_url + endpoint
        
        logger.info(f"POST Request URL: {url}")
        logger.info(f"POST Request Payload: {sanitize_payload(payload)}")

        try: 
            response = requests.post(url, json=payload)

        except requests.exceptions.RequestException as e:
            logger.error(f"Error occurred while making POST request: {e}")
            raise

        logger.info(f"POST Request Status Code: {response.status_code}")
        logger.info(f"POST Request Response: {sanitize_response(response.json())}")    

        return response

    def get(self, endpoint):
        url = self.base_url + endpoint
        
        logger.info(f"GET Request URL: {url}")
        
        headers = {"Authorization": f"Bearer {self.auth_token}"}
        try:
            response = requests.get(url, headers=headers)
        except requests.exceptions.RequestException as e:
            logger.error(f"Error occurred while making GET request: {e}")
            raise

        logger.info(f"GET Request Status Code: {response.status_code}")
        logger.info(f"GET Request Response: {sanitize_response(response.json())}")
        
        return response