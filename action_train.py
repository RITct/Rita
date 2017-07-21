#Run this code to retrain the action recognition model
#delete secret_sauce/ann.pt before training.
import json
from secret_sauce.models import training, predict_action
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
    
training_data = training_data[0]
training(10000, training_data) #training the model
#sample
print(predict_action("good bye"))


