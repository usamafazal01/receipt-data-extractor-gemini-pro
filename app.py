from dotenv import load_dotenv

load_dotenv()

from show_data import display_extracted_data

import streamlit as st

import os

from PIL import Image


import google.generativeai as genai

GoogleApiKey = os.getenv("Google_API_KEY")

genai.configure(api_key=GoogleApiKey)

## Function to load OpenAI model and get respones

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text
    

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application For Invoice")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

input_prompt = """
              Please extract relevant information from the uploaded invoice image and provide the data in JSON format. The extracted data may include key-value pairs or structured information such as:

- Vendor Information (name, address, contact details)
- Invoice Details (number, date, due date)
- Item Details (description, quantity, unit price, total price)
- Tax Details (type, rate, amount)
- Payment Information (transaction ID, amount, method)
- Other Information (sent by, received by, additional notes)

Extract as much information as possible from the invoice, organizing it into a JSON format. Ensure that the JSON object is structured in a way that captures the variability of the data present in different invoices.

For example:
{
    "vendor": {
        "name": "",
        "address": "",
        "contact": ""
    },
    "invoice": {
        "number": "",
        "date": "",
        "due_date": ""
    },
    "items": [
        {
            "description": "",
            "quantity": "",
            "unit_price": "",
            "total_price": ""
        },
        ...
    ],
    "taxes": [
        {
            "type": "",
            "rate": "",
            "amount": ""
        },
        ...
    ],
    "payment": {
        "transaction_id": "",
        "amount": "",
        "method": ""
    },
    "other_information": {
        "sent_by": "",
        "received_by": "",
        "notes": ""
    },
    ...
}

Please provide the extracted data in the specified JSON format.

               """

## If ask button is clicked

if submit:
    if submit:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)

    # Remove code block wrappers from the response
        response = response.strip().strip('```json').strip() 
        response = response.replace("JSON ", "").strip()
    
    #Calling function from show_data.py
        display_extracted_data(response)
    

 