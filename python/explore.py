from twilio.rest import Client

client = Client(
    "AC614ab027351d5f6423512366e0eeae37", 
    "152c9e03f06d6b322dc3595d5fe6a00e"
    )

for msg in client.messages.list():
    print(f"Deleting {msg.body}")
    msg.delete()

# msg = client.messages.create(
#     to="+916294260120",
#     from_="+12054984280",
#     body="hello from python",
#  )


# print(f"created a new message: {msg.sid}")