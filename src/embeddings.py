"""Diff2Vec embeddings and PCA projections."""

import numpy as np


def compute_diff2vec_embedding(G, dim: int = 128) -> np.ndarray:
    """Compute a Diff2Vec embedding for a given graph.

    Parameters
    ----------
    G : networkx.Graph
        Visibility graph.
    dim : int
        Embedding dimension.

    Returns
    -------
    emb : np.ndarray, shape (n_nodes, dim)
        Embedding matrix.
    """
    raise NotImplementedError("Implement Diff2Vec embedding here.")


def pca_projection(emb: np.ndarray, n_components: int = 2) -> np.ndarray:
    """Compute PCA projections of embeddings for visualization.

    Parameters
    ----------
    emb : np.ndarray
        High-dimensional embeddings.
    n_components : int
        Number of principal components.

    Returns
    -------
    proj : np.ndarray
        Low-dimensional projection.
    """
    raise NotImplementedError("Implement PCA projection here.")
