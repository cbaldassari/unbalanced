"""Visibility graph construction from log-returns."""

import pandas as pd
import networkx as nx


def build_visibility_graph(returns: pd.Series) -> nx.Graph:
    """Build a visibility graph from a univariate log-return series.

    Parameters
    ----------
    returns : pd.Series
        Time series of log-returns.

    Returns
    -------
    G : networkx.Graph
        Visibility graph.
    """
    raise NotImplementedError("Implement visibility graph construction (e.g., using ts2vg or custom code).")
