# Unbalanced Wasserstein Barycenter for Energy Markets

Implementation of the paper: **"Information-driven modeling of energy markets: an unbalanced Wasserstein barycenter approach"**

**Authors**: Carlo Mari, Emiliano Mari, Cristiano Baldassari (University of Tuscia)

---

## 📋 Overview

This repository implements the **5-step pipeline** described in the paper to analyze natural gas and electricity prices:

### Step 1: Preprocessing
Inject and compute normalized detrended log-returns

### Step 2: Visibility Graphs  
Transform time series into graphs

### Step 3: Embeddings
Represent graphs in 128 dimensions (Diff2Vec)

### Step 4: Wasserstein Barycenter
Compute optimal fusion: **λ_gas = 0.65**, **λ_el = 0.35**

### Step 5: Gaussian Mixture Model
Model joint distribution

---

## 🚀 Quick Start

### Install Dependencies

```bash
pip install numpy pandas matplotlib scipy statsmodels POT networkx karateclub ts2vg scikit-learn jupyter
```

### Run Notebooks

```bash
jupyter notebook
```

Execute in order:
1. `01_preprocessing.ipynb` - Load data, detrending with LOESS, detrended and and normalized log-returns 
2. `02_visibility_graphs.ipynb` - Build graphs
3. `03_embeddings.ipynb` - Diff2Vec embeddings
4. `04_wasserstein.ipynb` - Optimal barycenter
5. `05_gmm.ipynb` - Final model

---

##  Data

** Data already included! Available freely on mercatoelettrico.org**

Files in `data/`:
- `logret_gas.dat` - Natural gas log-returns (2019-2023)  
- `logret_electricity.dat` - Electricity log-returns (2019-2023)

**1825 observations** already preprocessed with LOESS. Ready to use!

---

## Main Result

The method automatically finds:
- Natural gas weight: **65%** (dominant)
- Electricity weight: **35%**

This reflects the European market structure!

---

## 📧 Contact

- Cristiano Baldassari: cristiano.baldassari@unitus.it

---

## 📄 License

MIT License - Feel free to use this code
