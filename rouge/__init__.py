from __future__ import absolute_import
from rouge.rouge import FilesRouge, Rouge

##Line below added for FinBert implementation to inform the user that they are using FinRouge and not regular rouge
print("You have imported FinRouge. FinRouge is a modified verison of rouge for summarization of finance related documents")

__version__ = "1.0.0"
__all__ = ["FilesRouge", "Rouge"]
