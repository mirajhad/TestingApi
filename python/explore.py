from twilio.rest import Client

client = Client(
    "SID", 
    "TOKEN"
    )

for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()

# msg = client.messages.create(
#     to="+9162942120",
#     from_="+120549280",
#     body="hello from python",
#  )


# print(f"created a new message: {msg.sid}")
