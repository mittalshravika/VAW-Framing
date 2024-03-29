import pandas as pd
import csv

df = pd.read_csv('global_newsdata.csv')

# keywords to filter VAW specific articles
filter_terms = ["sexual assault", "sexually assaulted", "sexual attach", "acid attack", "attacked her", "attacking her", "her attacker", "sexual violence", "he violently", \
    "she was stabbed", "he stabbed", "sexually violent crime", "sexually violent crimes", "sexually violent criminal", "sexual violence", "rape", "gender violence", \
    "assault with a deadly weapon", "workplace violence", "she was killed", "she was murdered", \
    "domestic violence", "domestic dispute", "intimate partner violence", "sexual abuse", "sexually abused", "victim of sexual abuse", "victims of sexual abuse", \
    "sexual offender", "simple assault", "nonnegligent manslaugter", \
    "manslaugter", "negligent manslaugter", "justifiable homicide", "forcible rape", "forcible sodomy", "sexual assault with an object", "forcible fondling", "stalk her", "stalking her", "stalker", "stalkers", "youth violence", \
    "family violence", "physical abuse", "spouse abuse", "sexually abusing", "groping", "sex trafficking"]

# meta information available
id = list(df["id"])
date = list(df["date"])
source = list(df["source"])
title = list(df["title"])
content = list(df["content"])
url = list(df["url"])
published = list(df["published"])
published_utc = list(df["published_utc"])
collection_utc = list(df["collection_utc"])

f = open("filtered_national_newsdata_VAW.csv", "w", encoding = 'UTF8', newline = '')
header = ["id", "date", "source", "title", "content", "url", "published", "published_utc", "collection_utc"]
writer = csv.writer(f)
writer.writerow(header)

filtered_num = 0
for i in range(len(content)):
    text = content[i].lower()
    valid = False
    for t in filter_terms:
        if t in text:
            valid = True
    if valid:
        filtered_num += 1
        entry = [id[i], date[i], source[i], title[i], content[i], url[i], published[i], published_utc[i], collection_utc[i]]
        writer.writerow(entry)

f.close()