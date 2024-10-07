# Fibonacci Calculator with Redis Caching

This project implements a Fibonacci sequence calculator that utilizes Redis for caching previously computed results to improve performance. The caching mechanism helps to avoid redundant calculations for the same Fibonacci numbers.

## Features

- Computes Fibonacci numbers using a recursive function.
- Caches computed Fibonacci numbers in Redis for quick retrieval.
- Reduces the computation time for repeated calls.

## Requirements

- Python 3.x
- `redis` library

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dperepadya/redisCache.git