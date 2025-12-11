"""Entropy-optimized unbalanced Wasserstein barycenter."""

import numpy as np


def compute_wasserstein_barycenter(emb_gas: np.ndarray, emb_el: np.ndarray, lambda_ng: float) -> np.ndarray:
    """Compute the Wasserstein barycenter of two embedding distributions.

    Parameters
    ----------
    emb_gas : np.ndarray
        Embeddings for gas.
    emb_el : np.ndarray
        Embeddings for electricity.
    lambda_ng : float
        Weight for gas (lambda_el = 1 - lambda_ng).

    Returns
    -------
    barycenter_samples : np.ndarray
        Samples from the barycenter distribution in embedding space.
    """
    raise NotImplementedError("Implement Wasserstein barycenter computation here.")


def entropy_grid_search(emb_gas: np.ndarray, emb_el: np.ndarray, grid: np.ndarray) -> float:
    """Perform an entropy-based grid search over lambda_ng.

    Parameters
    ----------
    emb_gas : np.ndarray
    emb_el : np.ndarray
    grid : np.ndarray
        Grid of candidate lambda_ng values.

    Returns
    -------
    lambda_opt : float
        Entropy-maximizing weight.
    """
    raise NotImplementedError("Implement entropy-based weight selection here.")
