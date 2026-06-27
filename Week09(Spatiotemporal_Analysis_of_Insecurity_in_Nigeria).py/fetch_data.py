import requests
import pandas as pd

# ENTER YOUR ACLED LOGIN DETAILS

USERNAME = "idokojapaul.20241428903@futo.edu.ng"
PASSWORD = "@Acleddata001"


# REQUEST ACCESS TOKEN


auth_url = "https://acleddata.com/oauth/token"

auth_data = {
    "username": USERNAME,
    "password": PASSWORD,
    "grant_type": "password",
    "client_id": "acled",
    "scope": "authenticated"
}

print("Logging in...")

response = requests.post(auth_url, data=auth_data)

if response.status_code != 200:
    print("Authentication Failed!")
    print(response.text)
    quit()

token = response.json()["access_token"]

print("Login Successful!")
print()


# DOWNLOAD ACLED DATA


headers = {
    "Authorization": f"Bearer {token}"
}

base_url = "https://acleddata.com/api/acled/read"

page = 1
limit = 500
all_records = []

print("Downloading Nigeria data...\n")

while True:

    params = {
        "country": "Nigeria",
        "limit": limit,
        "page": page
    }

    response = requests.get(
        base_url,
        headers=headers,
        params=params
    )

    if response.status_code != 200:
        print("Error:", response.text)
        break

    result = response.json()

    records = result.get("data", [])

    if len(records) == 0:
        break

    all_records.extend(records)

    print(f"Downloaded page {page} ({len(records)} records)")

    page += 1

# SAVE TO CSV


df = pd.DataFrame(all_records)

filename = "nigeria_acled_raw.csv"

df.to_csv(filename, index=False)

print()
print("=" * 40)
print("DOWNLOAD COMPLETE")
print("=" * 40)
print(f"Rows Downloaded : {len(df)}")
print(f"Columns         : {len(df.columns)}")
print(f"Saved File      : {filename}")