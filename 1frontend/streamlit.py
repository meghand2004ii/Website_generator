import streamlit as st
import os



import google.generativeai as genai

def load_prompt(file_path='prompts.txt'):
        with open(file_path,'r') as f:
            prompt=f.read()
        return prompt

def generate_website_content(prompt):
    # Call Gemini AI's API to generate website content
    genai.configure(api_key=st.secrets["GEMINI_AI_API_KEY"])
    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(prompt)

    # Extract the generated website content from the response
    generated_website_content=""
    for part in response.parts:
         generated_website_content+=part.text
    return generated_website_content

def main():
    st.title("AI Website Generator")
    st.write("Welcome to the AI Website Generator. Please fill in the below fields")

    website_type = st.text_input("Enter the type of website")
    framework = st.text_input("Enter the framework")

    prefix=f"Generate a website using {website_type} type with {framework} framework, "
    prompt = load_prompt()

    final_prompt = f"{prefix}{prompt}"
    generate_button = st.button("Generate Website")

    if generate_button:
         st.write(generate_website_content(final_prompt))
        # generate_website(website_type, framework)

# def generate_website(website_type, framework):
#     payload = {"website_type": website_type, "framework": framework}
#     response = requests.post("http://localhost:5000/generate_website")#, json=payload)
#     print(dir(response))
#     if response.status_code == 200:
#         st.write(response.json())
#         # zip_filename = response.json().get("zip_filename")
#         # st.write(f"Website generated successfully. Download your files [here](http://localhost:5000/{zip_filename}).")
#     else:
#         st.error("Failed to generate website.")

if __name__ == "__main__":
    main()
