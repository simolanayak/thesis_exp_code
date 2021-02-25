import torch
from torch import Tensor
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import numpy as np

import sys

import networkx as nx

#TODO: Make small world
def make_small_world(maxdeg, density, numnodes):
    pass
class SocialNetwork:
    def __init__(self, numnodes=None, adjmat=None, nettype="complete", density=1.0, maxdeg=6, is_directed=False):
        self.numnodes = numnodes
        self.adjmat = adjmat
        self.nettype = nettype
        self.density = density
        self.nxgraph = None
        self.is_directed = is_directed
        
        if nettype == 'complete' or nettype == 'c':
            self.nxgraph = nx.complete_graph(numnodes)
        if nettype == 'scalefree' or nettype == 'sf':
            self.nxgraph = nx.scale_free_graph(numnodes)
        if nettype == 'smallworld' or nettype == 'sw' or nettype == 'ws' or nettype == 'watts-strogatz':
            self.nxgraph = make_small_world(maxdeg, density, numnodes)
        self.adjmat = nx.linalg.graphmatrix.adjacency_matrix(self.nxgraph)
        
    def contact(self, newnetwork, inter=1.0, intra=1.0, interpreters_only=False):
        pass
    
    def get_node_degree(self, node):
        pass
    
    def get_node_indegree(self, node):
        pass
    
    def get_node_outdegree(self, node):
        pass
    
    
