import streamlit as st
import json
import pandas as pd

def display_extracted_data(response):
    try:
        # Log the response for debugging
        st.write("Received response:", response)
        
        # Remove leading/trailing whitespace and '```json' string
        response = response.strip().strip('```json').strip()
        
        # Remove the "JSON" prefix from the response
        response = response.replace("JSON ", "").strip()
        
        # Parse JSON response into a dictionary
        try:
            data = json.loads(response)
        except json.decoder.JSONDecodeError as e:
            st.error("Error parsing JSON data: {}".format(e))
            st.error("Received response: {}".format(response))
            return

        # Filter out key-value pairs where the value is empty
        cleaned_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                # Remove empty values from dictionary
                non_empty_values = {k: v for k, v in value.items() if v}
                if non_empty_values:
                    cleaned_data[key] = non_empty_values
            elif isinstance(value, list):
                # Remove empty dictionaries from list
                non_empty_dicts = [item for item in value if isinstance(item, dict) and any(item.values())]
                if non_empty_dicts:
                    cleaned_data[key] = non_empty_dicts

        # Convert the cleaned data into a DataFrame
        df_data = [(key, str(value)) for key, value in cleaned_data.items()]
        df = pd.DataFrame(df_data, columns=['Key', 'Value'])

        # Display the extracted data as a table
        if not df.empty:
            st.subheader("Extracted Information")
            st.dataframe(df)
        else:
            st.warning("No extracted information to display.")

    except Exception as e:
        st.error("Error processing response: {}".format(e))