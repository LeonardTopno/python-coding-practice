"""
josn.load() -> It is used to convert JSON string to Pythhon Dictionary

syntax:

if response.status_code == 200: 
    reponse_data = json.load(response.text)   # Here response.text is the raw JSON string from the resonse  # response_data = reponse.json()

"""

#----------------------------------

"""
json.dumps()

We can use json.dumps(varibale1) to manually convert a dictionary to a JSON string, and then send it as data.

New method:
requests.post() 

# call the api POST request
response = requests.post(url="https://1.1.1.1/api/v1/sample-program/@1212", json=variable1)

This response.post() method is used with thge `json` parameter to automatically convert `variable1` (a Python dictionary) to a JSON string for the POST request.



Leo's note: This approach is better as this simplifies the process by leaveraging the "requests" library's built-in JSON handling capabilities, maing the code cleaner and easier to read.

"""