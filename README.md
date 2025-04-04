# Information-driven modeling of energy markets: an unbalanced Wasserstein barycenter approach

by
Carlo Mari, 
Cristiano Baldassari.


## Abstract

We propose a novel methodology to jointly model the price dynamics of natural gas and electricity by integrating advanced Machine Learning techniques with tools from optimal transport theory. The framework combines Graph Machine Learning with the unbalanced Wasserstein barycenter to uncover latent structures and dependencies within interconnected energy markets. The approach begins by converting time series of log-returns into visibility graphs, which are then mapped into high-dimensional vector spaces through graph embedding techniques. This transformation reveals hidden information that is not easily detectable in raw, unidimensional data. In the embedding space, temporal and structural features become more distinct, enabling a clearer understanding of market behavior. An information-driven Wasserstein barycenter is then computed by optimizing its weights via Shannon entropy maximization, revealing an asymmetric fusion of the two markets, with natural gas exerting a dominant influence. To capture the underlying stochastic structure, we fit a Gaussian Mixture Model to the barycenter using maximum likelihood estimation via the Expectation-Maximization algorithm. A three-component mixture provides an effective representation. To account for commodity-specific effects, an additional Gaussian component is introduced for each market. The model is calibrated to match the empirical moments of the log-return distributions and their observed correlation. Applied to Italian energy market data from 2019 to 2023, a period marked by extreme volatility and structural disruptions, the methodology accurately reproduces both common dynamics and idiosyncratic fluctuations. This framework offers a robust and adaptable tool for risk assessment, derivative pricing, and the analysis of energy market interdependencies, especially in complex and asymmetric environments.

## Reproducing the results

This repo provides the Python notebooks [step 1](), [step 2]() containing the code to implement the method we propose in the paper and covers all the steps of the following analytic workflow, divided in two steps:

## Getting the code
You can download a copy of all the files in this repository by cloning the
[git](https://github.com/cbaldassari/unbalanced) repository:
```
    git clone https://github.com/cbaldassari/unbalanced
```
or [download a zip archive](https://github.com/cbaldassari/manifold/archive/refs/heads/main.zip).
