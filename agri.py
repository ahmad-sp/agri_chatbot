import streamlit as st
from PIL import Image
import requests
import certifi

# Function to call the generative AI API
def generate_response(prompt, api_key):
    url = "https://api.generativeai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 150
    }
    try:
        response = requests.post(url, headers=headers, json=data, verify=certifi.where())
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()["choices"][0]["text"].strip()
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Agriculture Chatbot")
    st.write("Upload a picture of a plant and ask your agriculture-related questions.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        prompt = st.text_input("Ask your question about the plant:")
        if prompt:
            if "plant" in prompt.lower() or "agriculture" in prompt.lower():
                with st.spinner('Generating response...'):
                    api_key = st.secrets["generativeai"]["api_key"]
                    response = generate_response(prompt, api_key)
                    if response:
                        st.write(response)
            else:
                st.write("Please ask questions related to agriculture.")

if __name__ == "__main__":
    main()