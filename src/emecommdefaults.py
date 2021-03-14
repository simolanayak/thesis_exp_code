import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.parameter import Parameter
import torch.optim as optim

import egg.core as core

class DefaultSender(nn.Module):
    def __init__(self, msg_dim):
        super(DefaultSender, self).__init__()
        self.fc1 = nn.Linear(784, 400)
        self.fc21 = nn.Linear(400, msg_dim)
        self.fc22 = nn.Linear(400, msg_dim)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        mu, logvar = self.fc21(x), self.fc22(x)
        return mu, logvar
class DefaultReceiver(nn.Module):
    def __init__(self):
        super(DefaultReceiver, self).__init__()
    
    def forward(self, inputs):
        pass

class DefaultUnderstander(nn.Module):
    def __init__(self):
        super(DefaultUnderstander, self).__init__()
    
    def forward(self, inputs):
        pass

class DefaultEstimator(nn.Module):
    def __init__(self, hiddendim):
        super(DefaultEstimator, self).__init__()
        #decide arch
    
    def forward(self, inputs):
        pass
        