# Information-driven modeling of energy markets: an unbalanced Wasserstein barycenter approach

This repository contains the code and data structure needed to reproduce the results in:

> Mari, C., Mari, E., Baldassari, C.  
> *Information-driven modeling of energy markets: an unbalanced Wasserstein barycenter approach*.

The code implements the full pipeline described in the paper:

1. LOESS detrending and computation of log-returns
2. Transformation of time series into visibility graphs
3. Diff2Vec graph embeddings
4. Entropy-based optimization of the unbalanced Wasserstein barycenter
5. Parametric representation of the barycenter via Gaussian Mixture Models (GMM)
6. Construction and calibration of the joint stochastic model
7. Benchmarking against a large set of GARCH-type models

## Repository structure

- `data/`  
  - `raw/`: raw price data (e.g. GME PUN and natural gas prices).  
  - `processed/`: preprocessed log-returns, embeddings, and intermediate objects.
- `src/`: Python modules implementing each component of the methodology.
- `notebooks/`: Jupyter notebooks to reproduce figures and tables in the paper.
- `results/`:
  - `figures/`: figures exported from the notebooks (corresponding to the paper).
  - `tables/`: CSV files with the numerical values of the tables.
- `scripts/`: command-line scripts to run the full pipeline and benchmarks.

## Installation

We recommend using Python ≥ 3.10 in a virtual environment.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Data

The empirical application uses daily prices for:

- Italian natural gas (volume-weighted average, €/MWh)
- Italian electricity (PUN, €/MWh)

from **GME – Gestore dei Mercati Energetici** over the period 2019–2023.

For licensing reasons, the repository is structured so that you can place the raw data locally in:

```text
data/raw/gas_prices_italy_2019_2023.csv
data/raw/electricity_pun_2019_2023.csv
```

The expected CSV schema is documented in `notebooks/01_preprocessing_log_returns.ipynb` and in `src/preprocessing.py`.

## Reproducing the main results

The typical workflow is:

1. Run preprocessing and compute log-returns.
2. Build visibility graphs and compute Diff2Vec embeddings.
3. Compute the entropy-optimized Wasserstein barycenter and fit GMMs.
4. Calibrate the joint stochastic model.
5. Run the GARCH-type benchmarks.
6. Regenerate all figures and tables.

Each step is implemented both as a Jupyter notebook under `notebooks/` and, in skeleton form, as Python modules in `src/` and scripts under `scripts/`.

## How to cite

If you use this structure or code as a reference, please cite:

> Mari, C., Mari, E., Baldassari, C.  
> *Information-driven modeling of energy markets: an unbalanced Wasserstein barycenter approach*.

A `CITATION.cff` file can be added to this repository for automatic citation in GitHub.

## License

Please add your chosen license (e.g. MIT, BSD-3-Clause) in the `LICENSE` file.
