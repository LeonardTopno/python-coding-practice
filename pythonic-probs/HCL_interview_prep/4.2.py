"""
variable1 = {"snmp_read" : "RO", "snmp_write" : "RW", "id": ""}

id_list = ["aaa", "abc", "efg"]


Get each id from id_list and pass the value for id key in variable 1. 

Make sure varibale1 as dictionary, call the api(url=https://1.1.1.1/api/v1/sample-program/@1212) for all payload constructed and API call = POST,
validate the id value from response same as input pauload id value.

Validate the id value from response same as input payload id value.
"""



import requests

variable1 = {"snmp_read" : "RO", "snmp_write" : "RW", "id": ""}

id_list = ["aaa", "abc", "efg"]

def verify_id_in_response_same_as_id_in_payload(variable1, id_list):

    for id in id_list:
        
        # updating the id key in varibale1
        variable1["id"] = id

        # call the api POST request
        response = requests.post(url="https://1.1.1.1/api/v1/sample-program/@1212", json=variable1)


        #Checking if the response is successful

        if response.status_code == 200:
            
            # Parse thge JSON response
            print(f"response, {response}")
            response_data = response.json()

            # validate the reponse id in the response.
            if response_data.get("id") == id:
                print(f"ID {id} validated successfulyy.")
            else:
                print(f"ID {id} validation failed.")

        else: 
            print(f"API call failed for ID {id}. Status code: {response.status_code}")
            print(f"response: {response}")
            print(f"response: {type(response)}")


## Driver code
if __name__ == "__main__":

    verify_id_in_response_same_as_id_in_payload(variable1, id_list)
