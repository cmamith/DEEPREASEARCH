import os
from typing import Dict

import sendgrid
from sendgrid.helpers.mail import Email, Mail, Content, To
from agents import Agent, function_tool


@function_tool
def send_email(subject: str, html_body: str) -> Dict[str, str]:
    """Send an email with the given subject and HTML body"""
    sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))
    sender = os.environ.get("SENDER_EMAIL")
    recipient = os.environ.get("RECIPIENT_EMAIL")
    
    if not sender or not recipient:
        print("Error: SENDER_EMAIL and RECIPIENT_EMAIL must be set in .env")
        return "error: missing email configuration"

    from_email = Email(sender)
    to_email = To(recipient)
    content = Content("text/html", html_body)
    mail = Mail(from_email, to_email, subject, content).get()
    response = sg.client.mail.send.post(request_body=mail)
    print("Email response", response.status_code)
    return "success"


INSTRUCTIONS = """You are able to send a nicely formatted HTML email based on a detailed report.
You will be provided with a detailed report. You should use your tool to send one email, providing the 
report converted into clean, well presented HTML with an appropriate subject line."""

email_agent = Agent(
    name="Email agent",
    instructions=INSTRUCTIONS,
    tools=[send_email],
    model="gpt-4o-mini",
)
