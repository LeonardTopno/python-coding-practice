
"""
Write a program to call rest api (url=https://1.1.1.1/api/v1/sample-program@1212) with content-type as application/json,
REST API call = GET,
Response code = 500 Server Error
Your code should accept http error and validate whether you have received 500 server error, raise exception when 500 error not received.

"""

import requests

headers = {
    "Content-Type": "application/json"
}

def call_api_get_req(url):
    try:
        response = requests.get(url, headers = headers)

        if response.status_code == 500:
            print("Received 500 Server Error")
        else: 
            print("API call successful with status code", response.status_code) 
    
    except requests.exceptions.RequestException as e:
        print("Error calling the API:", e)
        raise Exception("Not recived Server Error 500. Error: ", e)



## Driver code
if __name__ == "__main__":
    url = "https://1.1.1.1/api/v1/sample-program@1212"
    call_api_get_req(url)
    