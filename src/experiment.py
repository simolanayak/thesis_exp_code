import networkx as nx
import matplotlib.pyplot as plt

import torch

import argparse


from egg import core
class Experiment:
    def __init__(self, nets, dataset, train_loader, test_loader,
                 core_params=[], msg_type="fixed", msg_len="2"):
        if core_params != []:
            self.core_params = core.init(params=core_params)   #takes in an array of core params
        else:
            self.core_params = core.init()
            
        self.msg_type = msg_type
        self.msg_len = msg_len
        
        self.dataset = dataset
        self.train_loader = train_loader
        self.test_loader = test_loader
    
    def run(self):
        pass
        
if __name__ == "__main__":
    pass
    #TODO: argparse
    #TODO: yml file reader
    
    #TODO: create experiment
    
    #TODO: run it [quite literally .run()]
    