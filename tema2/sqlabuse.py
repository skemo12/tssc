import requests

HOST = "localhost"
PORT = 8080
url = "inside/message/send/3"

# Create form request
form = {
    "message": "update, accounts, id=77, profile_img=profile/vader.jpg"
}

# Send request
response = requests.post(f"http://{HOST}:{PORT}/{url}", data=form)
print(response.text)
print(response.status_code)