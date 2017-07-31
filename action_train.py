#Run this code to retrain the action recognition model
#delete secret_sauce/ann.pt before training.
import json
from secret_sauce.action_models import action_train, action_predict
#importing functions for training and predicting the model
import torch.nn as nn
#importing torch
from torch.autograd import Variable
import torch

training_data = []

with open('action_dataset.json') as data_file:
    data = json.load(data_file)

for line in data:
    #fetching training data
    training_data.append(line)

action_train(20000, training_data) #training the model
#testing with a new input
#print("say wahts tinkerhub")
print("intent:" + action_predict("how is it"))
"""
accuracy= 0 % input= tell me more about RIT actual= website guess= website
accuracy= 0 % input= give me more information actual= website guess= website
accuracy= 1 % input= who is the principal  actual= website guess= website
accuracy= 0 % input= give me the phone number actual= contact guess= contact
accuracy= 31 % input= open college website actual= website guess= website
accuracy= 43 % input= open college website actual= website guess= website
accuracy= 0 % input= navigate me to RIT actual= location guess= location
accuracy= 30 % input= give me more information actual= website guess= website
accuracy= 28 % input= good bye actual= goodbye guess= goodbye
accuracy= 69 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 0 % input= navigate me to RIT actual= location guess= location
accuracy= 76 % input= open college website actual= website guess= website
accuracy= 67 % input= i have to go actual= goodbye guess= goodbye
accuracy= 80 % input= open college website actual= website guess= website
accuracy= 77 % input= i am going actual= goodbye guess= goodbye
accuracy= 78 % input= i am going actual= goodbye guess= goodbye
accuracy= 65 % input= how to go there actual= location guess= location
accuracy= 80 % input= i want to talk with authorities actual= contact guess= contact
accuracy= 80 % input= give me the phone number actual= contact guess= contact
accuracy= 90 % input= see you later actual= goodbye guess= goodbye
accuracy= 95 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 79 % input= how to go there actual= location guess= location
accuracy= 93 % input= show me RIT website actual= website guess= website
accuracy= 94 % input= see you later actual= goodbye guess= goodbye
accuracy= 87 % input= i have to go actual= goodbye guess= goodbye
accuracy= 88 % input= good bye actual= goodbye guess= goodbye
accuracy= 92 % input= give me the phone number actual= contact guess= contact
accuracy= 95 % input= who is the principal  actual= website guess= website
accuracy= 80 % input= how can i reach actual= location guess= location
accuracy= 80 % input= how to contact actual= contact guess= contact
accuracy= 91 % input= give me more information actual= website guess= website
accuracy= 98 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 96 % input= who is the principal  actual= website guess= website
accuracy= 95 % input= give me the phone number actual= contact guess= contact
accuracy= 97 % input= show me RIT website actual= website guess= website
accuracy= 99 % input= latest news about RIT actual= website guess= website
accuracy= 91 % input= connect me with RIT actual= contact guess= contact
accuracy= 98 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 96 % input= give me the phone number actual= contact guess= contact
accuracy= 99 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 93 % input= how to go there actual= location guess= location
accuracy= 94 % input= good bye actual= goodbye guess= goodbye
accuracy= 93 % input= how to go there actual= location guess= location
accuracy= 98 % input= see you later actual= goodbye guess= goodbye
accuracy= 98 % input= who is the principal  actual= website guess= website
accuracy= 95 % input= good bye actual= goodbye guess= goodbye
accuracy= 89 % input= RIT actual= website guess= website
accuracy= 97 % input= give me the phone number actual= contact guess= contact
accuracy= 98 % input= show me RIT website actual= website guess= website
accuracy= 94 % input= how to go there actual= location guess= location
accuracy= 96 % input= give me more information actual= website guess= website
accuracy= 100 % input= tell me more about RIT actual= website guess= website
accuracy= 90 % input= RIT actual= website guess= website
accuracy= 96 % input= good bye actual= goodbye guess= goodbye
accuracy= 97 % input= give me more information actual= website guess= website
accuracy= 97 % input= give me more information actual= website guess= website
accuracy= 98 % input= talk to you soon actual= goodbye guess= goodbye
accuracy= 99 % input= open college website actual= website guess= website
accuracy= 97 % input= i have to go actual= goodbye guess= goodbye
accuracy= 98 % input= give me the phone number actual= contact guess= contact
accuracy= 100 % input= tell me more about RIT actual= website guess= website
accuracy= 96 % input= connect me with RIT actual= contact guess= contact
accuracy= 96 % input= how can i reach actual= location guess= location
accuracy= 97 % input= i have to go actual= goodbye guess= goodbye
accuracy= 95 % input= navigate me to RIT actual= location guess= location
accuracy= 94 % input= how to contact actual= contact guess= contact
accuracy= 97 % input= good bye actual= goodbye guess= goodbye
accuracy= 95 % input= navigate me to RIT actual= location guess= location
accuracy= 99 % input= see you later actual= goodbye guess= goodbye
accuracy= 99 % input= i am going actual= goodbye guess= goodbye
accuracy= 98 % input= i have to go actual= goodbye guess= goodbye
accuracy= 99 % input= i am going actual= goodbye guess= goodbye
accuracy= 99 % input= open college website actual= website guess= website
accuracy= 99 % input= show me RIT website actual= website guess= website
accuracy= 99 % input= i want to talk with authorities actual= contact guess= contact
accuracy= 95 % input= RIT actual= website guess= website
accuracy= 100 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 97 % input= how can i reach actual= location guess= location
accuracy= 99 % input= i want to talk with authorities actual= contact guess= contact
accuracy= 98 % input= how can i reach actual= location guess= location
accuracy= 100 % input= tell me more about RIT actual= website guess= website
accuracy= 100 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 100 % input= tell me more about RIT actual= website guess= website
accuracy= 100 % input= latest news about RIT actual= website guess= website
accuracy= 98 % input= good bye actual= goodbye guess= goodbye
accuracy= 98 % input= i have to go actual= goodbye guess= goodbye
accuracy= 96 % input= navigate me to RIT actual= location guess= location
accuracy= 95 % input= RIT actual= website guess= website
accuracy= 97 % input= navigate me to RIT actual= location guess= location
accuracy= 100 % input= have a nice day actual= goodbye guess= goodbye
accuracy= 98 % input= connect me with RIT actual= contact guess= contact
accuracy= 99 % input= i want to talk with authorities actual= contact guess= contact
accuracy= 100 % input= open college website actual= website guess= website
accuracy= 96 % input= RIT actual= website guess= website
accuracy= 96 % input= RIT actual= website guess= website
accuracy= 96 % input= RIT actual= website guess= website
accuracy= 97 % input= navigate me to RIT actual= location guess= location
accuracy= 100 % input= tell me more about RIT actual= website guess= website
accuracy= 97 % input= how to contact actual= contact guess= contact
accuracy= 100 % input= latest news about RIT actual= website guess= website
go to college website
intent: website
"""

