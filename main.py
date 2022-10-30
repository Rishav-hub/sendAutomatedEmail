import os
import pandas as pd
from sendDetailedEmail.email import MailAttachment
from config.app_constants import email_id, name, remarks, folder_path, file_name, assignment_no 

def sendMail(clientEmail):
    try:
        sender = MailAttachment(clientEmail=clientEmail)
        sender.send()

    except Exception as e:
        raise e

def getData() -> pd.DataFrame:
    try:
        file_path = os.path.join(folder_path, file_name)
        df: pd.DataFrame = pd.read_csv(file_path)
        df: pd.DataFrame = df[[email_id, name, remarks]]
        return df
    except Exception as e:
        raise e

if __name__=="__main__":
    df: pd.DataFrame = getData()
    for i in range(len(df)):
        sender = MailAttachment(assignment_no, df[email_id][i], df[name][i], df[remarks][i])
        sender.send()
    
