import json
#importing functions for training and predicting the model
from secret_sauce.models import training, predict_action
#importing torch 
import torch.nn as nn
from torch.autograd import Variable
import torch

training_data = []
foss = open('secret_sauce/action_dataset.json', 'r')
for line in foss:
    #fetching training data
    training_data.append(json.loads(line))

training_data = training_data[0]
training(10000, training_data) #training the model
#sample
predict_action("good bye")


