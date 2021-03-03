import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from egg import core

class DefaultSender(nn.Module):
    def __init__(self):
        pass

class DefaultReceiver(nn.Module):
    def __init__(self):
        pass

class DefaultUnderstander(nn.Module):
    def __init__(self):
        pass

class DefaultEstimator(nn.Module):
    def __init__(self):
        pass