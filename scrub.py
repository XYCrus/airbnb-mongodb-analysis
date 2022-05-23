# -*- coding: utf-8 -*-
import pandas as pd

pd.set_option('display.max_rows', 500)

df = pd.read_csv("./data/listings.csv")

inspect = df.isna().sum()
print(inspect)

df_clean = df.dropna(subset=['host_name','review_scores_rating'])
inspect_clean = df_clean.isna().sum()
print(inspect_clean)

df_clean.to_csv('./data/listings_clean.csv') 