# Bitcoin Price Tracker

A desktop application built with Python that retrieves the current Bitcoin price, stores historical price data locally, displays saved price records, and visualizes Bitcoin price changes over time.

## Overview

**Bitcoin Price Tracker** is a lightweight desktop application designed to provide a simple way to monitor Bitcoin prices.

The application uses the CoinGecko API to retrieve the latest Bitcoin price in USD. Users can save retrieved prices to a local SQLite database, review their price history, and visualize stored prices using a chart.

The graphical user interface is built with CustomTkinter to provide a modern and user-friendly desktop experience.

## Features

* 🔄 Fetch the latest Bitcoin price
* 💵 Display the current Bitcoin price in USD
* 🔔 Show a desktop notification when the price is retrieved
* 💾 Save Bitcoin prices to a local SQLite database
* 📜 View previously saved price records
* 📈 Visualize Bitcoin price history with a chart
* 🖥️ Modern desktop interface using CustomTkinter
* 🗃️ Local data storage using SQLite

## Technologies Used

* **Python**
* **CustomTkinter** — graphical user interface
* **Requests** — API communication
* **CoinGecko API** — Bitcoin price data
* **SQLite** — local database storage
* **Plyer** — desktop notifications
* **Matplotlib** — data visualization

## Project Structure

```text
bitcoin-price-tracker/
│
├── bitcoin_price_tracker.py
├── requirements.txt
├── .gitignore
└── README.md
```

> The SQLite database is created locally when the application is used and is intentionally excluded from version control.

## How It Works

The application follows a simple workflow:

```text
CoinGecko API
      ↓
Fetch Bitcoin Price
      ↓
Display Current Price
      ↓
Save Price
      ↓
SQLite Database
      ↓
View History / Generate Chart
```

### 1. Fetch Bitcoin Price

The application sends a request to the CoinGecko API and retrieves the current Bitcoin price in USD.

### 2. Save Price Data

Users can save the retrieved price together with its timestamp.

The data is stored in a local SQLite database named:

```text
bitcoin_prices.db
```

### 3. View Price History

The application retrieves previously saved prices from the database and displays them in a separate window.

### 4. Visualize Price Data

Saved Bitcoin prices can be visualized using Matplotlib to show price changes over time.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/MOHADESSEH/bitcoin-price-tracker.git
```

### 2. Navigate to the project directory

```bash
cd bitcoin-price-tracker
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application with:

```bash
python bitcoin_price_tracker.py
```

After launching the application:

1. Click **Get Latest Price** to retrieve the current Bitcoin price.
2. Click **Save to Database** to store the current price.
3. Click **Price History** to view previously saved prices.
4. Click **Show Chart** to visualize the stored price data.

## Database

The application uses SQLite for local data storage.

The `prices` table contains:

| Field       | Type    | Description                            |
| ----------- | ------- | -------------------------------------- |
| `id`        | INTEGER | Unique record identifier               |
| `price_usd` | REAL    | Bitcoin price in USD                   |
| `timestamp` | TEXT    | Date and time when the price was saved |

The database file is generated automatically when the application is first executed.

## API

This project uses the **CoinGecko API** to retrieve Bitcoin price information.

The application requests Bitcoin's current USD price and displays the returned value in the graphical interface.

## Future Improvements

Possible future improvements include:

* Support for additional cryptocurrencies
* Multiple fiat currencies
* Automatic periodic price updates
* Configurable price alerts
* More advanced statistical analysis
* Interactive charts
* Exporting historical data to CSV
* Improved error handling and API request timeouts
* Separation of the application into multiple modules
* Unit and integration tests

## Learning Objectives

This project demonstrates practical use of:

* Python GUI development
* REST API consumption
* JSON data processing
* SQLite database management
* Data visualization
* Desktop notifications
* Event-driven programming
* Basic software project organization

## Author

**MOHADESSEH**

GitHub: [MOHADESSEH](https://github.com/MOHADESSEH)
