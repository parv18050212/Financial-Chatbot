from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from services.gemini_service import generate_financial_advice
from services.financial_data_service import get_live_market_data
import os

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS for frontend communication

# Serve the main HTML file
@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# Endpoint to handle user queries
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    user_query = data.get('query', '')

    if not user_query:
        return jsonify({"error": "Query is required"}), 400

    # Generate response using Gemini AI
    response = generate_financial_advice(user_query)
    return jsonify({"response": response})

# Endpoint to fetch live market data
@app.route('/market-data', methods=['GET'])
def market_data():
    symbol = request.args.get('symbol', 'AAPL')  # Default to AAPL if no symbol is provided
    data = get_live_market_data(symbol)
    return jsonify(data)

# Serve static files (CSS, JS)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)