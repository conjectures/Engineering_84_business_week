# Python requests package
import requests
import task01

#Let's connect to live web using python request

# we will connect to www.bbc.com and check if it is live.
responses = requests.get("https://www.bbc.co.uk")
# 200 - ok
# 4xx - error on user side
if responses.status_code == "200":
    print(f"The website is up and running with status code {responses.status_code}")
else:
    print(f"Something went wrong {responses.status_code}")


print("Using the api")
print(task.status_code_check('https://www.google.com'))



# print(response)
# print(response.__dict__)
response = requests.get("https://www.bbc.co.uk")
# Response object overwrites __bool__ method (class polymorphism) to check status code
# Returns True if self.status_check < 400
if response:
    print(f"Success with status code {response.status_code}")
else:
    print("Something went wrong")


