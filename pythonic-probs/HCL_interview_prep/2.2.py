import re

def validate_url(url):
    # Regular expression pattern for matching URLs
    pattern = r"^(https?://)[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}(\/\S*)?$"
    pattern = r"^(https?://)?[a-zA-Z0-9-\.]+\.[a-zA-Z]{2,}(\/\S*)?$"
              
    
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Check if the input URL matches the pattern
    if regex.match(url):
        return True
    else:
        return False

# Test URls given in the question
url1 = "https://www.google.com"
url2 = "http://fb.com"
url3 = "www.bing.com"

print(validate_url(url1))  # True
print(validate_url(url2))  # True
print(validate_url(url3))  # False
