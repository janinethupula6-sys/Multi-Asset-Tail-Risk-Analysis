## Project Title
**When Diversification Disappears**  
*A Regime-Aware Wavelet-Copula Framework for Multi-Horizon Tail Risk*

## Research Question
How does downside dependence among equities, long-term US government bonds, gold, and Bitcoin vary across investment horizons and market regimes, and how much portfolio tail risk is mismeasured when those changes are ignored?

## Portfolio
The study uses an equally weighted four-asset portfolio:

- **SPY** — US equities
- **TLT** — long-duration US Treasury bonds
- **GLD** — gold
- **BTC-USD** — Bitcoin

Each asset has a 25% portfolio weight.

## Data
Daily adjusted prices are downloaded from Yahoo Finance using `yfinance`.

Study period used in the notebooks:
- Start: 2015-01-01
- End: 2026-10-01

Only common trading dates across all four assets are retained.

## Methodology
The project follows this workflow:

1. Download and clean synchronized market data.
2. Calculate daily log returns.
3. Define Normal and Stress regimes using lagged 20-day SPY volatility.
4. Decompose returns with a Daubechies-4 wavelet.
5. Group detail components into:
   - Short scale: D1 + D2
   - Medium scale: D3 + D4
   - Long scale: D5 + D6
6. Estimate empirical lower-tail dependence.
7. Fit Gaussian, Student-t, Clayton, and Gumbel pairwise copulas and select by AIC.
8. Build horizon/regime tail-risk maps.
9. Estimate portfolio VaR and Expected Shortfall using multivariate Gaussian and Student-t copulas.
10. Test the framework out-of-sample using the 2023–2026 period.
11. Backtest VaR using Kupiec and Christoffersen tests.
12. Generate final report figures and summary tables.

## Train/Test Design
- **Training:** through 2022-12-31
- **Testing:** from 2023-01-01 onward

## Market Regime Rule
A day is classified as **Stress** when lagged 20-day annualized SPY volatility exceeds the 75th percentile of the training-period volatility distribution. Otherwise it is classified as **Normal**.

## Risk Measures
- 95% Value-at-Risk
- 99% Value-at-Risk
- 97.5% Expected Shortfall

Expected Shortfall is the main tail-risk measure.

## Project Structure
```text
quant_edge_1/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_returns_diagnostics.ipynb
│   ├── 03_market_regimes.ipynb
│   ├── 04_wavelet_analysis.ipynb
│   ├── 05_empirical_tail_dependence.ipynb
│   ├── 06_copula_models.ipynb
│   ├── 07_tail_risk_map.ipynb
│   ├── 08_portfolio_risk.ipynb
│   ├── 09_out_of_sample.ipynb
│   ├── 10_backtesting.ipynb
│   └── 11_final_results.ipynb
│
├── outputs/
│   ├── figures/
│   └── tables/
│
├── README.md
├── requirements.txt
└── run_all.py
```

## Installation
Create a virtual environment if desired, then install dependencies:

```bash
pip install -r requirements.txt
```

## Reproduce the Full Analysis
From the project root, run:

```bash
python run_all.py
```

The script executes every notebook in order and stops immediately if any notebook fails.

## Important Interpretation Note
The short, medium, and long labels are approximate wavelet frequency bands, not literal holding-period returns.

## AI Disclosure
AI tools were used for conceptual clarification, coding assistance, debugging, and drafting support. The team remains responsible for all methodological choices, code, calculations, interpretation, and final claims.
