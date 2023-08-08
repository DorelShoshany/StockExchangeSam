# StockExchangeSam

Welcome to the Stock Exchange App! This app allows you to interact with a stock market system and retrieve information about stocks, query total costs, and more.

## Getting Started

Before running the app, please make sure you have the following prerequisites:

1. **Python Interpreter:** Make sure you have a Python interpreter installed on your system. You can download and install Python from the official [Python website](https://www.python.org/downloads/).

2. **Virtual Environment (Recommended):** It's recommended to create and activate a virtual environment for Python. If you're using a development environment like PyCharm, it may create the virtual environment for you. If not, you can create and activate a virtual environment using the following commands:

   ```bash
   # Create a virtual environment
   python -m venv venv
   
   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS and Linux
   source venv/bin/activate

## Running the App

1. Clone this repository to your local machine:
   git clone https://github.com/your-username/stock-exchange-app.git
   cd stock-exchange-app

2. Build and run the app using Docker Compose:
   docker-compose up --build
  Once the containers are up and running, you can access the app through your web browser or a tool like curl.
  The app will be available at http://localhost:5000.

3. To stop the app and containers, use:
   docker-compose down

## Endpoints

1. information about a stock by symbol: GET https://localhost:5000/stocks/{symbol}
2. information about your total cost in $: GET http://localhost:5000/total-cost
3. you can reset the total cost to 0: GET http://localhost:5000/total-cost/rest


