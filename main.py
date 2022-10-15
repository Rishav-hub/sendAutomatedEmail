import os
import pandas as pd
from sendDetailedEmail.email import MailAttachment

def sendMail(clientEmail):
    try:
        sender = MailAttachment(clientEmail=clientEmail)
        sender.send()

    except Exception as e:
        raise e

def getData() -> pd.DataFrame:
    try:
        folder_path = "artifacts"

        for i in os.listdir(folder_path):
            if i.endswith(".csv"):
                file_path = os.path.join(folder_path, i)
                df: pd.DataFrame = pd.read_csv(file_path)
                df: pd.DataFrame = df[["Email address", "Name", "Remarks / Mail Body"]]
                return df
    except Exception as e:
        raise e

if __name__=="__main__":
    df: pd.DataFrame = getData()
    for i in range(len(df)):
        sender = MailAttachment(4, df["Email address"][i], df["Name"][i], df["Remarks / Mail Body"][i])
        sender.send()
    
