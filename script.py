import requests
import json

with open("credentials.json") as credentials_content:
    credentials = json.load(credentials_content);

#print("Logging in as : " + credentials["username"])

payload = {
    "username": credentials["username"],
    "password": credentials["password"]
}

with requests.Session() as s:
    login_url = "https://eleves.mines-paris.eu/accounts/login/"

    p = s.post(login_url, data=payload)
    print p.text
