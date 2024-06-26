from core import DEVICE
import torch
from torch import Tensor

class AlphaBatch:
  def __init__(self, xy_e: Tensor, device: torch.device = DEVICE):
    self.device = device
    self._alphas = xy_e.to(self.device)
    self.beam_xy = xy_e
    # distribuciones de fotones generadas por la detección del alpha
    #self._photonDistribs: Dict[str, Dict[str, List[Tensor]]] = defaultdict(lambda: defaultdict(list))


    def __repr__(self) -> str:
        return f"Batch of {len(self)} alphas"

    def __len__(self) -> int:
        return len(self._alphas)
      
  def get_photon_distribution(self) -> Tensor:
      '''Not implemented for now, as the reconstruction process is made separately'''
      pass

    # analog of hits would be the photon distributions ( self.append_photonDistribs...)

