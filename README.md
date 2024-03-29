# News Media and Violence Against Women: Understanding Framings of Stigma

## Data Sources
* NELA-GT [[Link-2020]](https://doi.org/10.7910/DVN/CHMUYZ); [[Link-2021]](https://doi.org/10.7910/DVN/RBKVBM); [[Link-2022]](https://doi.org/10.7910/DVN/AMCV2H)
* NELA-Local [[Link-Full]](https://doi.org/10.7910/DVN/GFE66K)

## Data Preparation
Use ```data-prep/create_csv.py``` and ```data-prep/filter_data.py``` to filter and clean the downloaded NELA-GT and NELA-Local datasets.

## Approval/Stigma embeddings
Embeddings for approval and stigma dimensions available at ```embds/approvalEmd.pkl``` and ```embds/stigmaEmd.pkl```

Followed *Mittal and De Choudhury [(2023)](https://dl.acm.org/doi/abs/10.1145/3544548.3580834)* to get the approval/stigma embeddings.

## Approval/Stigma score alignment
* Run ```get_doc_embds.py``` to get sentence-level BERT embeddings for news articles within NELA-GT and NELA-Local datasets.
* Run  ```get_stigma_alignment.py``` to generate approval/stigma cosine similarity alignment scores for the news articles.

## References
Mittal, S.; and De Choudhury, M. 2023. Moral Framing of Mental Health Discourse and Its Relationship to Stigma: A Comparison of Social Media and News. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23).
