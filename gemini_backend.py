from flask import Flask, request, jsonify
import google.generativeai as genai
import requests
import html2text
from flask_cors import CORS
import logging

# Replace with your Gemini API Key
GEMINI_API_KEY = "AIzaSyDngWZ2AABGCSvoGGhDguDDEFs-e7nBkSk"
genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

logging.basicConfig(level=logging.INFO)

def get_leetcode_problem_description(title_slug):
    url = "https://leetcode.com/graphql"
    headers = {
        "Content-Type": "application/json",
        "Referer": f"https://leetcode.com/problems/{title_slug}/"
    }
    payload = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": title_slug},
        "query": '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                title
                content
            }
        }'''
    }
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            question = data.get("data", {}).get("question", {})
            if question and question.get("content"):
                raw_text = html2text.html2text(question["content"])
                clean_text = "\n".join([line for line in raw_text.splitlines() if line.strip() != ""])
                return question["title"], clean_text
            else:
                logging.error(f"No question content found for slug: {title_slug}")
        else:
            logging.error(f"LeetCode API returned status {response.status_code} for slug: {title_slug}")
    except Exception as e:
        logging.error(f"Error fetching problem description: {e}")
    return None, None

@app.route('/generate', methods=['POST'])
def generate_intuition():
    data = request.get_json()
    slug = data.get('slug', '').strip()
    if not slug:
        return jsonify({'error': 'No problem slug provided.'}), 400
    title, problem_description = get_leetcode_problem_description(slug)
    if not problem_description:
        return jsonify({'error': 'Could not fetch problem description for the given slug.'}), 404

    prompt = f"""
You are a coding assistant whose primary goal is to help users build coding intuition for solving Data Structures and Algorithms (DSA) LeetCode problems. 
Your expertise lies in explaining the reasoning behind different approaches to problem-solving. 
Keep your answers concise and to the point.

Leetcode Problem Title: {title}
Leetcode Problem Description: {problem_description}

For the Leetcode problem, follow these steps:
1. Provide a detailed intuition for the brute force solution. Explain the approach and reasoning behind it.
2. State the time and space complexity of the brute force solution.
3. Provide a detailed intuition for the most optimal solution. Explain the approach and reasoning behind it.
4. State the time and space complexity of the optimal solution.
5. Do NOT generate any code. Your focus is solely on providing intuitions and complexities.
"""

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return jsonify({'intuition': response.text.strip()})
    except Exception as e:
        logging.error(f"Error generating Gemini response: {e}")
        return jsonify({'error': 'Error generating Gemini response.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 