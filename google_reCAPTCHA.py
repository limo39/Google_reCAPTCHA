import requests
import json

def verify_recaptcha(response, secret_key):
    api_url = 'https://www.google.com/recaptcha/api/siteverify'
    data = {
        'secret': secret_key,
        'response': response
    }
    response = requests.post(api_url, data=data)
    result = json.loads(response.text)
    return result['success']

# Example usage
response = input("Enter the reCAPTCHA response: ")
secret_key = 'your_secret_key'  
verification_result = verify_recaptcha(response, secret_key)
if verification_result:
    print("reCAPTCHA verification successful.")
else:
    print("reCAPTCHA verification failed.")
