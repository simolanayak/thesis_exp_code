import sys

import torch
from torch import Tensor
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

import numpy as np

import networkx as nx
from networkx import DiGraph as dg

import deep_agents
from deep_agents import FullAgent

from emecommdefaults import DefaultSender, DefaultReceiver, DefaultUnderstander, DefaultEstimator
class WrongGraphTypeException(Exception):
    pass
class NullGraphException(Exception):
    pass

def make_agent_pool(num_agents, sender_type=DefaultSender,
                    receiver_type=DefaultReceiver, understander_type=DefaultUnderstander,
                    estimator_type=DefaultUnderstander):
    return [FullAgent(sender=sender_type, receiver=receiver_type, 
                      understander=understander_type, reward_estimator=estimator_type)
                      for i in range(num_agents)]

class SocialNetwork:
    def __init__(self, agent_pool=[], numnodes=0, nettype="unspecified",
                 density=1.0, maxdeg=6, is_directed=False,
                 rand_seed=1, weight_type="comm_succ"):
        """[summary]

        Args:
            agent_pool (list, optional): [description]. Defaults to [].
            numnodes(int, optional): Defaults to 0.
            nettype (str, optional): [description]. Defaults to "unspecified".
            density (float, optional): [description]. Defaults to 1.0.
            maxdeg (int, optional): [description]. Defaults to 6.
            is_directed (bool, optional): [description]. Defaults to False.
            weight_type (str, optional): [description]. Defaults to "comm_succ".
            num_forests (int, optional): [description]. Defaults to 1.

        Raises:
            WrongGraphTypeException: If a 
            NullGraphException: If a networkx graph is not fed for a merged method
        """
        #object variables:
        #agent_pool
        #num_nodes
        #is_dir
        #maxdeg
        #weight_type (what kind)
        #num_forests
        
        self.agent_pool = agent_pool
        
        self.numnodes = len(agent_pool)
        
        self.nettype = nettype
        if nettype == 'complete' or nettype == 'com':
            self.nxgraph = nx.complete_graph(self.agent_pool)
        if nettype == 'scalefree' or nettype == 'sf':
            self.nxgraph = nx.scale_free_graph(self.agent_pool)
        if nettype == 'smallworld' or nettype == 'sw':
            self.nxgraph = nx.watts_strogatz_graph(self.agent_pool)
        if nettype == 'chain' or nettype == 'path' or nettype == 'ch':
            self.nxgraph = nx.path_graph(self.agent_pool)
        if nettype == 'merged' or nettype == 'm':
            if self.nxgraph is None:
                raise NullGraphException("Please feed an existing graph.")
        if nettype == 'unspecified' or nettype == 'u':
            self.nxgraph = nx.binomial_graph(self.agent_pool, seed=rand_seed, directed=self.is_directed)
            
        self.nxgraph.add_nodes_from(agent_pool)
        
        self.is_directed = is_directed
        self.weight_type = weight_type
        self.num_forests = num_forests
                
        #self-correcting num forests:
    def update_weight(self, vtx_a, vtx_b):
        self.nxgraph.update()
        
    def mingle(self, newnetwork, inter_intra_ratio=1.0):
        """ Merges two communities together.
        Future version will have three at once and nodes randomly selected between the three

        Args:
            newnetwork (SocialNetwork): the second network to merge it with
            inter_intra_ratio (float, optional): Connections between vs. connection within. Defaults to 1.0.
        """
        if newnetwork is None:
            raise NullGraphException("Second network not in existence.")
        if newnetwork.nxgraph is None:
            raise NullGraphException("Second network not in existence.")
        
        totalnodes = self.numnodes + newnetwork.numnodes
        
        if inter_intra_ratio == 0:
            new_num_forests = self.num_forests + newnetwork.num_forests
        else:
            new_num_forests = self.num_forests
        
        merged_net = SocialNetwork(numnodes=totalnodes, nettype='merged', num_forests=new_num_forests)
    
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
