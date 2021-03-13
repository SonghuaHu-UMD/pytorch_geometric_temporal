import torch
from temporalgcn import TGCN
from torch.nn import MultiheadAttention
from torch_geometric.nn import GCNConv

class A3TGCN(torch.nn.Module):
    r"""An implementation of the Temporal Graph Convolutional Gated Recurrent Cell.
    For details see this paper: `"T-GCN: A Temporal Graph ConvolutionalNetwork for
    Traffic Prediction." <https://arxiv.org/abs/1811.05320>`_

    Args:
        in_channels (int): Number of input features.
        out_channels (int): Number of output features.
        improved (bool): Stronger self loops. Default is True.
        cached (bool): Caching the message weights. Default is False.
        add_self_loops (bool): Adding self-loops for smoothing. Default is True.
    """
    def __init__(self, in_channels: int, out_channels: int, improved: bool=False,
                 cached: bool=False, add_self_loops: bool=True):
        super(TGCN, self).__init__()

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.improved = improved
        self.cached = cached
        self.add_self_loops = add_self_loops
        
        
        self.base_tgcn = TGCN(in_channels = self.in_channels,
                              out_channels = self.out_channels,
                              improved = self.improved,
                              cached = self.cached,
                              add_self_loops = self.add_self_loops)


    def forward(self, X: torch.FloatTensor, edge_index: torch.LongTensor,
                edge_weight: torch.FloatTensor=None, H: torch.FloatTensor=None) -> torch.FloatTensor:
        """
        Making a forward pass. If edge weights are not present the forward pass
        defaults to an unweighted graph. If the hidden state matrix is not present
        when the forward pass is called it is initialized with zeros.

        Arg types:
            * **X** *(PyTorch Float Tensor)* - Node features for T time periods.
            * **edge_index** *(PyTorch Long Tensor)* - Graph edge indices.
            * **edge_weight** *(PyTorch Long Tensor, optional)* - Edge weight vector.
            * **H** *(PyTorch Float Tensor, optional)* - Hidden state matrix for all nodes.

        Return types:
            * **H** *(PyTorch Float Tensor)* - Hidden state matrix for all nodes.
        """
        H_accum = 0
        return H
