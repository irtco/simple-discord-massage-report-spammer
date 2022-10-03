import requests
token=input("TOKEN ->")
channel_ID=input("channel ID ->")
Guild_ID=input("Server ID ->")
Massage_ID=input("Massage ID ->")

print("""
-----------------------------------------------------
|      illegal Content              |       0       |
|      Harassment                   |       1       |
|      Spam or Phishing Links       |       2       |
|      Self Harm                    |       3       |
|      NSFW Content                 |       4       |
-----------------------------------------------------
""")
Reason=input("Reason (0-4)->")

header={
    "authorization": token,
    "content-type": "application/json"
}

payload={
    "channel_id": channel_ID,
    "guild_id": Guild_ID,
    "message_id": Massage_ID,
    "reason": Reason
}

url='https://discord.com/api/v9/report'

r=requests.post(url=url, headers=header, json=payload)

print(r.content)

i=1

while i<5:
    r=requests.post(url=url, headers=header, json=payload)
    print(r.content)
