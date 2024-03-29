"""Sample script to generate sentence-level BERT embeddings to represent news articles"""

from transformers import BertTokenizer, BertModel
import torch
import pickle
import numpy as np
import pandas as pd

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')
model.to('cuda')

# download NELA-GT and NELA-Local datasets
# replace the empty 'docs' variable with a list of articles' content
# run the script separately for both NELA-GT (national) and NELA-Local (local) datasets
docs = []

docEmds = []

for j in range(len(docs)):

  sent = docs[j]
  inputs = tokenizer(sent, return_tensors = "pt", max_length = 512, truncation = True)
  inputs.to('cuda')
  outputs = model(**inputs)
  last_hidden_states = outputs.last_hidden_state
  docEmd = last_hidden_states[0][0].cpu().detach().numpy()
  docEmds.append(docEmd)

# save the generated embeddings
outfile = open("national_doc_embds_exp.pkl", "wb")
pickle.dump(docEmds, outfile)