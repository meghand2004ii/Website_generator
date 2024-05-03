from dotenv import load_dotenv
load_dotenv()
import os
from flask import Flask, request, jsonify
import requests
import google.generativeai as genai

app = Flask(__name__)

# Retrieve the API key from an environment variable
GEMINI_AI_API_KEY = os.getenv("GEMINI_AI_API_KEY")

if GEMINI_AI_API_KEY is None:
    raise ValueError("GEMINI_AI_API_KEY environment variable is not set")

def load_prompt(file_path='prompts.txt'):
        with open(file_path,'r') as f:
            prompt=f.read()
        return prompt 

@app.route("/generate_website", methods=["POST"])
def generate_website_content():
    # Load the prompt from the file
    prompt = load_prompt()

    # Call Gemini AI's API to generate website content
    genai.configure(api_key=GEMINI_AI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)

    # Extract the generated website content from the response
    generated_website_content=""
    for part in response.parts:
         generated_website_content+=part.text
    return generated_website_content

# def generate_website():
#     website_type = request.json.get("website_type")
#     framework = request.json.get("framework")
    

    # Generate prompts based on the website type and framework
    #prompts = generate_prompts(website_type, framework)

    # Call Gemini AI's API to generate website content
    #generated_website_content = generate_website_content(prompts)

    # Save the generated website content to a file or return it directly
    # For demonstration, we'll return it directly as a JSON response
    #return jsonify({"generated_website_content": generated_website_content})

# def generate_prompts(website_type, framework):
#     # Generate prompts based on the website type and framework
#     prompts = f"Generate a {website_type} website using {framework} framework."
#     return prompts

    




if __name__ == "__main__":
    app.run(debug=True)
