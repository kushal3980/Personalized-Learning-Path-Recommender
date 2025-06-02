# skill_graph.py

import networkx as nx

def build_skill_graph():
    G = nx.DiGraph()

    # Define edges (from basic → advanced)
    edges = [
        ("python", "pandas"),
        ("python", "numpy"),
        ("pandas", "data cleaning"),
        ("numpy", "scikit-learn"),
        ("scikit-learn", "classification"),
        ("scikit-learn", "regression"),
        ("classification", "tensorflow"),
        ("regression", "tensorflow"),
        ("tensorflow", "keras"),
        ("keras", "deep learning"),
        ("deep learning", "mlops"),
        ("mlops", "aws"),
        ("mlops", "docker"),
        ("python", "flask"),
        ("python", "fastapi"),
        ("python", "numpy"),
        ("numpy", "pandas"),
        ("pandas", "data visualization"),
        ("data visualization", "machine learning"),
        ("machine learning", "deep learning"),
        ("python", "numpy"),
        ("numpy", "pandas"),
        ("pandas", "data preprocessing"),
        ("data preprocessing", "feature engineering"),
        ("feature engineering", "scikit-learn"),
        ("scikit-learn", "model evaluation"),
        ("scikit-learn", "machine learning"),
        ("machine learning", "deep learning"),
        ("deep learning", "neural networks"),
        ("deep learning", "computer vision"),
        ("deep learning", "natural language processing"),
        ("machine learning", "model evaluation"),
        ("deep learning", "docker"),
        ("docker", "mlops"),
        ("mlops", "cloud computing"),
        ("cloud computing", "aws"),
        ("python", "git"),
        ("python", "docker")
    ]

    G.add_edges_from(edges)
    return G
