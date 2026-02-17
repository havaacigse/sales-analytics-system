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

## Live API

- **Base URL:** [https://sales-analytics-system-3yy0.onrender.com](https://sales-analytics-system-3yy0.onrender.com)  
- **Swagger Documentation:** [https://sales-analytics-system-3yy0.onrender.com/docs](https://sales-analytics-system-3yy0.onrender.com/docs)  

## Setup & Run (Local Development)

1. Clone the repo and go into the project folder, then create virtual environment, activate it, install dependencies, and run the server (all in one):

```bash
git clone https://github.com/havaacigse/sales-analytics-system.git
cd sales-analytics-system

# Create virtual environment
python -m venv venv

# Activate environment (macOS / Linux)
source venv/bin/activate
# Activate environment (Windows)
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:app --reload

#Open your browser to access:
Swagger UI: http://127.0.0.1:8000/docs
API root: http://127.0.0.1:8000