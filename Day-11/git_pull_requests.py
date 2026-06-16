import requests

# response is an object that this module(request) is returning. And this object has multiple functions.
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")


#print(response.status_code) => Returns the status code. Screenshot attached for more of this object functions.

# When we are using response.json() it automatically converts from json to dictionary under the hood.
complete_details = response.json()

for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])