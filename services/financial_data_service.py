import requests

# Replace with your API key for the financial data provider
FINANCIAL_API_KEY = 'SPG66VCBOLO78Y2K'
FINANCIAL_API_URL = 'https://www.alphavantage.co/query'  # Example API

def get_live_market_data(symbol):
    """
    Fetch live market data for a given stock symbol.
    """
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '5min',
        'apikey': FINANCIAL_API_KEY,
    }
    response = requests.get(FINANCIAL_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch market data"}