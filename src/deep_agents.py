"""
deep_agents.py

Wrapper class to write 
"""

import torch
import torch.nn as nn
import egg.core as core

from torchvision import datasets, transforms
from torch.nn import functional as F

from emecommdefaults import DefaultSender, DefaultReceiver, DefaultUnderstander, DefaultEstimator

import copy

def send_loss():
    """
    Default loss function for sender module
    """
    pass

def rec_loss():
    """
    Default loss function for receiver module
    """
    pass

def und_loss():
    """
    Default loss function for understander module
    """
    pass

def reset_param_util(model):
    for m in model.modules:
        if isinstance(m, nn.Linear):
            m.wei

class FullAgent(torch.nn.Module):
    def __init__(self,
                 sender=DefaultSender, pretrained_sender=False,
                 receiver=DefaultReceiver, pretrained_receiver=False,
                 understander=DefaultUnderstander, pretrained_understander=False,
                 reward_estimator=DefaultEstimator, pretrained_estimator=False):
       self.sender = sender
       self.receiver = receiver
       self.understander = understander
       self.reward_estimator = reward_estimator
    
    def train_sender(self, lossfunc=send_loss):
        if not self.pretrained_sender:
            self.sender.forward()
        else:
            return
    
    def train_receiver(self, lossfunc=rec_loss):
        if not self.pretrained_receiver:
            self.receiver.forward()
        else:
            return
    
    def train_understander(self, lossfunc=und_loss):
        if not self.pretrained_understander:
            self.understander.forward()
        else:
            return