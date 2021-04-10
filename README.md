# LSTM-Financial-News-Extractive-Summarization
Extractive Summarization of Financial News Articles Using LSTM Model for Headline Creation. Scored Using Newly Proposed FinRouge Scoring System. 
FinRouge is a modified version of PyPi's Rouge package that awards higher scores for summaries that contain financial jargon.

There are several sections to this repo. If you are attempting to run this code on your machine, use the notebooks in the following order:
>1. Open data_preparation.ipynb and follow the directions contained within
>2. Explore the rouge_modifications.ipynb notebook to learn about the Rouge and FinRouge scores. Note that some sections require FinRouge and some require the original version of rouge. FinRouge will automatically be imported with the call to import rouge when running notebooks within the repo, so it will be the reader's responsibility to disable the local "FinRouge" version of rouge when needed in the notebook to use the original version of rouge.
>3. You can now run the EDA.ipynb notebook to learn more about the data and the main.ipynb notebook to see the model and various topics surrounding it
