# Sales Analytics System

A Python + FastAPI project for sales analysis and prediction.

## Features

- REST API endpoints:
  - `/top-categories` → Top selling categories
  - `/top-products` → Top 5 products
  - `/monthly-sales` → Monthly sales totals
  - `/prediction` → Next month's sales prediction
- Data stored in SQLite (`db/sales.db`)
- Visualizations with Matplotlib
- Swagger UI for easy testing (available after deployment)

## Setup

1. Clone the repo:
```bash
git clone <your-repo-url>
cd sales-analytics-system
