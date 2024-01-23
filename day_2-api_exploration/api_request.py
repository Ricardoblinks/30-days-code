# import the neccessary libraries
import requests

# define a function to handle the request
"""
steps:
1. using the endpoint that we want our api to communicate with
2. and also the method that the particular api requires
3. then make a requests to the endpoint
4. store the response in a variable and return it out of the function 
"""
def apiRequest(endpoint, method='get', body={}):
    if (method.lower() == 'post'):
        response = requests.post(endpoint, body)
    elif (method.lower() == 'put'):
        response = requests.put(endpoint, body)
    elif (method.lower() == 'delete'):
        response = requests.delete(endpoint, body)
    else:
        response = requests.get(endpoint)

    return response.json()
    

# an endpoint to get user ip address
endpoint = 'https://api64.ipify.org?format=json'


# print the results gotten from the endpoint
print(apiRequest(endpoint, "get"))