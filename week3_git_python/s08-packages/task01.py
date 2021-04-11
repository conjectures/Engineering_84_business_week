# TASK
# Create a function called status code check
# Function should return the status code 
# DRY

import requests

def status_code_check(address):
    responses = requests. get(address)
    return responses.status_code
