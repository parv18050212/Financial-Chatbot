import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key='YOUR_GEMINI_API_KEY')

def generate_financial_advice(query):
    """
    Generate financial advice using Gemini AI.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(query)
    return response.text