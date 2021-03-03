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

class FullAgent:
    def __init__(self, sender=DefaultSender, pretrained_sender=True,
                 receiver=DefaultReceiver, pretrained_receiver=True,
                 understander=DefaultUnderstander, pretrained_understander=True,
                 reward_estimator=DefaultEstimator, pretrained_estimator=True):
       self.sender = sender
       self.receiver = receiver
       self.understander = understander
       self.reward_estimator = reward_estimator
    
    def train_sender(self, lossfunc=send_loss):
        if not self.pretrained_sender:
            self.sender.forward(lossfunc)
    
    def train_receiver(self, lossfunc=rec_loss):
        if not self.pretrained_receiver:
            self.receiver.forward(lossfunc)
    
    def train_understander(self, lossfunc=und_loss):
        if not self.pretrained_understander:
            self.understander.forward(lossfunc)