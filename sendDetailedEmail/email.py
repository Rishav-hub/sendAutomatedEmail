import smtplib
import os
from email.message import EmailMessage
from getCredentials.read import ConfigReader
from config.app_constants import sender_email, passkey

CURRENT_FOLDER = "sendDetailedEmail"

HTML_TEMPLATE_NAME = "Template_corona_info.html"
HTML_TEMPLATE_PATH = os.path.join(CURRENT_FOLDER, HTML_TEMPLATE_NAME)

# AUTH_DATA = ConfigReader()
# eMAIL = AUTH_DATA.read_config()['eMAILsender']
# ePASSKEY = AUTH_DATA.read_config()["ePASSKEY"]

eMAIL = sender_email
ePASSKEY = passkey

class MailAttachment:

    def __init__(self, assignment_no=None, clientEmail=None, name=None, remarks=None):
        self.assignment_no = assignment_no
        self.name = name
        self.clientEmail = clientEmail
        self.remarks = remarks

    def send(self):
        """_summary_: This method sends an email with an attachment to the client.
        """        
        msg = EmailMessage()
        msg["Subject"] = f"FSDS Bootcamp 2.0 || Assignment {self.assignment_no} Evaluation"
        msg["From"] = eMAIL
        msg["To"] = "query@ineuron.ai"
        msg["bcc"] = self.clientEmail
        msg['X-Priority'] = '2'

        msg.set_content(f"""
Hi {self.name},

Your Assignment {self.assignment_no} has been evaluated. 
Remarks -: {self.remarks}.

Regards,
Rishav Dash
Jr. Data Scientist
""")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(eMAIL, ePASSKEY)
            print("log in successfull!! \nsending email")
            smtp.send_message(msg)
            print("email Sent")
