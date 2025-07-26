# gbff_parser.py — Extract gene info from GenBank

from Bio import SeqIO
import pandas as pd

def parse_gbff(filepath):
    genes = []
    for record in SeqIO.parse(filepath, "genbank"):
        for feature in record.features:
            if feature.type == "CDS":
                locus = feature.qualifiers.get("locus_tag", ["-"])[0]
                product = feature.qualifiers.get("product", ["-"])[0]
                ec = feature.qualifiers.get("EC_number", ["-"])
                genes.append({
                    "Contig": record.id,
                    "Locus": locus,
                    "Start": int(feature.location.start),
                    "End": int(feature.location.end),
                    "Strand": feature.location.strand,
                    "Product": product,
                    "EC": ";".join(ec) if ec else "-"
                })
    return pd.DataFrame(genes) 
