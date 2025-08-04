
from langchain.tools import tool
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_WHATSAPP = "whatsapp:+14155238886" 

@tool
def get_whatsapp_message(to: str, message: str) -> str:
    """
    Send a WhatsApp message using Twilio.
    
    Args:
        to: Recipient's WhatsApp number (e.g., '+923001234567')
        message: The message to send
    
    Returns:
        Confirmation SID or error string
    """
    try:
        client = Client(TWILIO_SID, TWILIO_TOKEN)
        msg = client.messages.create(
            from_=FROM_WHATSAPP,
            body=message,
            to=f"whatsapp:{to}"
        )
        return f"Message sent with SID: {msg.sid}"
    except Exception as e:
        return f"Failed to send message: {str(e)}"
