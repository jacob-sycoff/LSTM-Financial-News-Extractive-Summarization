from __future__ import absolute_import
from rouge.rouge import FilesRouge, Rouge

###Added the lines below this
import sys
import FinRouge

sys.modules['rouge'] = FinRouge
###And above this

__version__ = "1.0.0"
__all__ = ["FilesRouge", "Rouge"]
