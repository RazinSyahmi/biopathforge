# BioPathForge Streamlit App

import streamlit as st
import os
from utils.gbff_parser import parse_gbff
from utils.pathway_predictor import predict_pathways
from utils.network_visualizer import draw_network

st.set_page_config(page_title="BioPathForge", layout="wide")
st.title("🧬 BioPathForge: Functional Genome & Pathway Explorer")

# File upload
uploaded_file = st.file_uploader("Upload a .gbff (GenBank) file", type=["gbff", "gbk"])

if uploaded_file:
    with open("uploaded.gbff", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded and saved!")

    # Parse file
    st.subheader("🔍 Gene Extraction")
    genes_df = parse_gbff("uploaded.gbff")
    st.dataframe(genes_df.head(10))

    # Pathway Prediction
    st.subheader("🧬 Pathway Prediction (KEGG/MetaCyc)")
    pathways_df = predict_pathways(genes_df)
    st.dataframe(pathways_df.head(10))

    # Visualization
    st.subheader("🕸️ Pathway Network Visualization")
    draw_network(pathways_df)

    # Export
    st.download_button("Download Gene Table", genes_df.to_csv(index=False), "genes.csv")
    st.download_button("Download Pathway Table", pathways_df.to_csv(index=False), "pathways.csv")
else:
    st.info("Please upload a GenBank .gbff file to begin.")
