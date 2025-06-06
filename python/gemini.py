import google.generativeai as genai
from leetcode_prob_description import get_leetcode_problem_description

# Replace with your Gemini API Key
genai.configure(api_key="AIzaSyDngWZ2AABGCSvoGGhDguDDEFs-e7nBkSk")

# Set the LeetCode problem slug
TITLE_SLUG = "two-sum"

# Fetch the problem description
problem_description = get_leetcode_problem_description(TITLE_SLUG)

# Initialize Gemini Flash 2.0 model
model = genai.GenerativeModel("gemini-1.5-flash")

# Compose the prompt
prompt = f"""
You are a coding assistant whose primary goal is to help users build coding intuition for solving Data Structures and Algorithms (DSA) LeetCode problems. 
Your expertise lies in explaining the reasoning behind different approaches to problem-solving. 
Keep your answers concise and to the point.

Leetcode Problem Description: {problem_description}

For the Leetcode problem, follow these steps:
1. Provide a detailed intuition for the brute force solution. Explain the approach and reasoning behind it.
2. State the time and space complexity of the brute force solution.
3. Provide a detailed intuition for the most optimal solution. Explain the approach and reasoning behind it.
4. State the time and space complexity of the optimal solution.
5. Do NOT generate any code. Your focus is solely on providing intuitions and complexities.
"""

# Get the response
response = model.generate_content(prompt)

# Print the model's reply
print(response.text.strip())
