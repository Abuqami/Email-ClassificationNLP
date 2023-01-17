# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import re
import nltk
import pickle
from emot.emo_unicode import EMOJI_UNICODE, EMOTICONS_EMO, UNICODE_EMOJI
def clean_MessageBody(df, OldMessage_body, NewMessage_body):
    df[NewMessage_body] = df[OldMessage_body].str.lower()
    df[NewMessage_body] = df[NewMessage_body].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))
    #below code is responsible for Numbers removal
    df[NewMessage_body] = df[NewMessage_body].apply(lambda elem: re.sub(r"\d+", "", elem))
    return df





train = pd.read_csv("SMS_train.csv")
test = pd.read_csv("SMS_test.csv")
#train['Message_body'] = train['Message_body'].to_string().lower()

#train['Label'] = train['Label'].replace({'Non-Spam':0,'Spam':1})
#train['Message_body'] = re.sub(r'[\.\?\!\,\:\;\"]', '', train['Message_body'])

print("\nHeadBefore:\n",train.head())

Ready_data = clean_MessageBody(train,"Message_body","NewMessage_body")


print("\nHeadAfter:\n",Ready_data.head())






"""
print("before:", train.head(),'\n')
train['Label'] = train['Label'].replace({'Non-Spam':0,'Spam':1})
print("after:", train.head())"""
