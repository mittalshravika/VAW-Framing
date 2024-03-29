"""Script to get approval/stigma score alignment for news articles"""
# Example script to get scores for local news articles

from transformers import BertTokenizer, BertModel
import pickle
import numpy as np

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

infile = open("Embds/stigmaEmd.pkl", "rb")
stigmaEmd = pickle.load(infile)
infile = open("Embds/approvalEmd.pkl", "rb")
approvalEmd = pickle.load(infile)

infile = open("Embds/local_doc_embds.pkl", "rb") # replace this with "Embds/national_doc_embds.pkl" to get scores for national news articles
newsEmds = pickle.load(infile)

newsScores = []

for j in range(0, len(newsEmds)):

  newsEmd = newsEmds[j]

  stigmaDim = approvalEmd - stigmaEmd

  stigmaSim = (np.dot(stigmaDim, newsEmd))/(np.linalg.norm(stigmaDim)*np.linalg.norm(newsEmd))
  newsScores.append(stigmaSim)

outfile = open("StigmaScores/cosine_scores_local_news_exp.pkl", "wb")
pickle.dump(newsScores, outfile)