#network_visualizer.py — Simple Pathway Network Plot

import networkx as nx import matplotlib.pyplot as plt import streamlit as st

def draw_network(pathway_df): G = nx.Graph() for _, row in pathway_df.iterrows(): ec = row['EC'] pathway = row['Pathway'] G.add_node(ec, type='EC') G.add_node(pathway, type='Pathway') G.add_edge(ec, pathway)

plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=1000, font_size=8)
st.pyplot(plt)

