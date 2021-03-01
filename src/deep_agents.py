import torch
from torch import nn

'''
Wrapper class for the deep neural agents to do the experiments on
Consists of a sender and a receiver (03/01/2021)
'''
class Agent:
    def __init__(self, sendUnit=None, receiveUnit=None, understander=None):
        self.sender = sender
        self.receiver = receiver
        
    def train_sender(self, method):
        if method == "r" or method.upper() == "REINFORCE":
            pass
        if method == "gs" or method.upper() == "GUMBEL-SOFTMAX":
            pass
    def train_receiver(self, method):
        pass