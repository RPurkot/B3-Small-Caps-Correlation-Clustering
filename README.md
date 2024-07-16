# 📈 Stock Returns Clustering Analysis 🏦

Welcome to the **B3 Small Caps Correlation Clustering Analysis** project! This repository contains a comprehensive analysis of clustering stock returns using weekly data from Brazilian small-cap stocks. We utilize various data science techniques, including data collection, processing, and cluster visualization.

## Table of Contents

## Introduction

In this project, we aim to identify clusters among small-cap stocks based on their weekly return correlations. By clustering these stocks, we can uncover patterns and similarities that might help in making informed investment decisions.

## Data Collection

We gather historical stock price data using the Yahoo Finance API (`yfinance`). The data includes:

- **Ticker symbols**: Representing the small-cap stocks.
- **Historical prices**: Adjusted close prices from 2019-01-01 to 2024-06-30.

## Data Processing

1. **Cleaning**: Remove columns with missing values.
2. **Resampling**: Aggregate the data to weekly prices.
3. **Return Calculation**: Calculate weekly returns.
4. **Correlation Matrix**: Construct a matrix of correlations based on the weekly returns.

## Clustering Analysis

We perform clustering using the K-means algorithm, applying the following steps:

1. **Distance Matrix**: Convert the correlation matrix to a distance matrix.
2. **Elbow Method**: Determine the optimal number of clusters.
3. **K-means Clustering**: Apply K-means with the optimal number of clusters.

## Visualization

To visualize the clusters, we use Principal Component Analysis (PCA) to reduce the dimensionality of the data and plot the clusters:

- **PCA**: Reduces the data to two dimensions for easy visualization.
- **Scatter Plot**: Shows the clusters in a 2D space.

## Results

The clusters reveal distinct groups of stocks with similar return behaviors. This information can be useful for portfolio diversification and risk management.
