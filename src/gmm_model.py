"""GMM fit for the barycenter and moment matching."""

import numpy as np
from sklearn.mixture import GaussianMixture


def fit_gmm_barycenter(samples: np.ndarray, n_components: int, n_inits: int = 1000) -> GaussianMixture:
    """Fit a univariate GMM to barycenter samples using multiple random restarts."""
    raise NotImplementedError("Implement GMM fitting with multiple initializations here.")


def compute_moments_from_gmm(gmm: GaussianMixture) -> dict:
    """Compute the first four moments of a univariate GMM analytically.

    Returns a dict with keys: 'mean', 'std', 'skew', 'kurt'.
    """
    raise NotImplementedError("Implement analytic moment computation for GMM here.")
