"""Preprocessing: LOESS detrending, log-prices, log-returns, stationarity tests."""

from typing import Tuple
import pandas as pd


def load_raw_data(gas_path: str, el_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Load raw gas and electricity price data from CSV files.

    Parameters
    ----------
    gas_path : str
        Path to the CSV file containing natural gas prices.
    el_path : str
        Path to the CSV file containing electricity (PUN) prices.

    Returns
    -------
    gas_df : pd.DataFrame
        DataFrame with gas prices indexed by date.
    el_df : pd.DataFrame
        DataFrame with electricity prices indexed by date.
    """
    gas_df = pd.read_csv(gas_path, parse_dates=True, index_col=0)
    el_df = pd.read_csv(el_path, parse_dates=True, index_col=0)
    return gas_df, el_df


def loess_detrend_and_log_returns(price_df: pd.DataFrame, bandwidth: float = 0.10) -> pd.DataFrame:
    """Placeholder for LOESS detrending and log-return computation.

    This function should:
    - compute log-prices,
    - apply LOESS detrending to extract the trend,
    - obtain the stochastic component and log-returns.

    Returns a DataFrame with columns such as:
    ['log_price', 'trend', 'xi', 'r'].
    """
    raise NotImplementedError("Implement LOESS detrending and log-return computation here.")


def run_stationarity_tests(returns_df: pd.DataFrame) -> pd.DataFrame:
    """Placeholder for ADF, PP, and KPSS tests on the log-returns.

    Returns
    -------
    summary : pd.DataFrame
        A table with test statistics and p-values for each test.
    """
    raise NotImplementedError("Implement stationarity tests (ADF, PP, KPSS) here.")
