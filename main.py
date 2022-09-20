import requests
token=input("TOKEN ->")
channel_ID=input("channel ID ->")
Guild_ID=input("Server ID ->")
Massage_ID=input("Massage ID ->")
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

i=1

while i<5:
    r=requests.post(url=url, headers=header, json=payload)
    print(r.content)
