# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import re
import nltk
import pickle
from emot.emo_unicode import EMOJI_UNICODE, EMOTICONS_EMO, UNICODE_EMOJI
train = pd.read_csv("SMS_train.csv")
test = pd.read_csv("SMS_test.csv")
#train['Message_body'] = train['Message_body'].to_string().lower()

train['Label'] = train['Label'].replace({'Non-Spam':0,'Spam':1})
train['Message_body'] = re.sub(r'[\.\?\!\,\:\;\"]', '', train['Message_body'])
print(train.head())

"""
print("before:", train.head(),'\n')
train['Label'] = train['Label'].replace({'Non-Spam':0,'Spam':1})
print("after:", train.head())"""
