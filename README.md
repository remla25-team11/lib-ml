# lib-ml

`lib-ml` is a Python library that provides preprocessing utilities for machine learning tasks in the REMLA project. It includes functionality for text cleaning, stopword removal, and stemming, and is used by the `model-service` to prepare input data for sentiment classification.

## Features

- Text preprocessing for sentiment analysis
- Custom stopword handling (preserves "not")
- Porter stemming
- Designed to be reusable across services

## Installation

You can install the package directly via GitHub using:

```bash
pip install git+https://github.com/remla25-team11/lib-ml@v0.1.1
