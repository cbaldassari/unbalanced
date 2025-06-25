# Information-driven modeling of energy markets

Codebase for the paper:
**"Information-driven modeling of energy markets: an unbalanced Wasserstein barycenter approach"**

## Overview

This repository provides the full implementation of the methodology proposed in the paper, including:
- Construction of visibility graphs from price time series
- Graph embeddings via Diff2Vec
- Computation of unbalanced Wasserstein barycenters
- Shannon entropy-based weight optimization
- GMM calibration on the barycenter
- Reproduction of empirical vs simulated distributions

## File Structure

- `src/`: core Python modules
- `notebooks/`: example Jupyter notebooks with visual outputs
- `data/`: placeholder for raw time series (not tracked)
- `requirements.txt`: required libraries (e.g. POT, scikit-learn, networkx)

## Getting Started

```bash
git clone https://github.com/yourusername/energy-wasserstein-model.git
cd energy-wasserstein-model
pip install -r requirements.txt
