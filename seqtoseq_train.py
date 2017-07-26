import json
from secret_sauce.seqtoseq_model import seqtoseq_train, reply_predict
import torch.nn as nn
#importing torch
from torch.autograd import Variable
import torch
training_data = []

with open('chitchat_dataset.json') as data_file:
    data = json.load(data_file)

for line in data:
    #fetching training data
    training_data.append((line["question"],line["answer"]))
seqtoseq_train(10000,training_data)
print("who are you ?")
print(reply_predict("who are you"))
