import requests
import json

# cPanel API credentials
api_username = "edumetrics"
api_token = "B4Z1XQX2I50FLRB57QE6XZA8WEN0K44I"
domain = "edu-metrics.com"
email_username = "example"
email_password = "example"

# API endpoint URL
api_url = f"https://edumetrics.com:2083/execute/Email/add_pop"

# Request payload
payload = {
    "email": f"{email_username}@{domain}",
    "password": email_password,
    "quota": 250 # Mailbox quota in megabytes
}

# Request headers
headers = {
    "Authorization": f"cpanel {api_username}:{api_token}",
    "Content-Type": "application/json"
}

# Send API request
response = requests.post(api_url, data=json.dumps(payload), headers=headers)

# Check the response
if response.status_code == 200:
    print("Email account created successfully!")
else:
    print(f"An error occurred: {response.text}")
