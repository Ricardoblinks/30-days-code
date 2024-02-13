from twilio.rest import Client

# Twilio credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'

def send_sms(recipient_number, message):
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_number
        )
        print("SMS sent successfully!")
        print("Message SID:", message.sid)
    except Exception as e:
        print("Error:", e)

# Example usage
recipient_number = '+1234567890'  # Replace with recipient's phone number
message = 'Hello from Twilio! This is a test SMS notification.'

send_sms(recipient_number, message)
