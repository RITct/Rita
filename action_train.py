import json
from secret_sauce.models import training, predict_action
import torch.nn as nn
from torch.autograd import Variable
import torch

training_data = []
foss = open('secret_sauce/action_dataset.json', 'r')
for line in foss:
    training_data.append(json.loads(line))

training_data = training_data[0]
training(10000, training_data)
#sample
predict_action("good bye")


