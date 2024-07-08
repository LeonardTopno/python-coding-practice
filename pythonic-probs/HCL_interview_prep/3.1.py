# Given dictionaries
knowngood_dictionary = {"response": [{},{},{},{},{},{},{},{},{},{},{},{},{}], "version": "1.0"}
api_response = {"response": [{},{},{},{},{},{},{},{},{},{},{},{},{},{"id": "1234"}], "version": "1.0"}



def make_two_dict_equal(api_response):
    # Remove the "id" key from each dictionary in the "response" list of api_response
    for item in api_response["response"]:
        print(item)
        if "id" in item:
            print(f"item with id {item}")
            #del item["id"]
            api_response["response"].remove(item)
        
    print(f"api_response finally {api_response}")
    print(f"knowngood_dictionary {knowngood_dictionary}")

    # Check if both dictionaries are equal
    if api_response == knowngood_dictionary:
        print("The dictionaries are equal.")
    else:
        print("The dictionaries are not equal.")


# Drive Code
if __name__ == "__main__":
    make_two_dict_equal(api_response)
    

