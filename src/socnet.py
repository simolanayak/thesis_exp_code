import torch
from torch import Tensor
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import numpy as np

import sys

import networkx as nx
from networkx import DiGraph as dg

#TODO: Make small world
def make_small_world(maxdeg, density, numnodes):
    pass
class WrongGraphType(Exception):
    pass

class AgentPool:
    def __init__(self):
        pass

class SocialNetwork:
    def __init__(self, numnodes=None, adjmat=None, nettype="complete",
                 density=1.0, maxdeg=6, is_directed=False, forests=False,
                 num_forests=1):
        self.numnodes = numnodes
        self.adjmat = adjmat
        self.nettype = nettype
        self.density = density
        self.nxgraph = None
        self.is_directed = is_directed
        self.num_forest = num_forests
        
        if nettype == 'complete' or nettype == 'c':
            self.nxgraph = nx.complete_graph(numnodes)
        if nettype == 'scalefree' or nettype == 'sf':
            self.nxgraph = nx.scale_free_graph(numnodes)
        if nettype == 'smallworld' or nettype == 'sw' or nettype == 'ws' or nettype == 'watts-strogatz':
            self.nxgraph = make_small_world(maxdeg, density, numnodes)
        self.adjmat = nx.linalg.graphmatrix.adjacency_matrix(self.nxgraph)
        
    def mingle(self, newnetwork, inter_intra_ratio=1.0, high_contact_only=False):
        #newnetwork: 
        #inter-intra ratio: parameter specified in Graesser et al. 2019
        #high_contact_only: high-connectivity nodes from each network only contact each other
        #a.mingle(b) is supposed to be equivalent to b.mingle(a)
        pass
        
    def min_degree(self, node_a, node_b):
        pass
    
    def get_node_degree(self, node):
        if self.is_directed:
            return dg.get_degree(node)
        else:
            return nx.get_degree(node)
    
    def get_node_indegree(self, node):
        if not self.is_directed:
            return self.get_node_degree(node)
        else:
            return dg.in_degree(node)
    
    def get_node_outdegree(self, node):
        if not self.is_directed:
            return self.get_node_degree(node)
        else:
            return dg.out_degree(node)
