#pathway_predictor.py — Simulated EC → Pathway Prediction

import pandas as pd import random

#Dummy EC-to-pathway mapping for demonstration

EC_PATHWAY_MAP = { "1.1.1.1": "Glycolysis", "2.7.1.1": "Pentose phosphate pathway", "3.5.4.4": "Purine metabolism", "4.2.1.11": "Citric acid cycle", "6.3.5.5": "Amino acid biosynthesis" }

def predict_pathways(genes_df): predictions = [] for _, row in genes_df.iterrows(): ecs = row['EC'].split(';') if row['EC'] != '-' else [] for ec in ecs: pathway = EC_PATHWAY_MAP.get(ec, random.choice(list(EC_PATHWAY_MAP.values()))) predictions.append({ "Locus": row['Locus'], "EC": ec, "Pathway": pathway }) return pd.DataFrame(predictions)

