import streamlit as st
import requests

# Set the title of the app
st.title("Chatbot API Tester")

# Create a text input for the user to enter their query
user_query = st.text_input("Enter your query:")

# When the user clicks the submit button
if st.button("Submit"):
    # Define the API endpoint
    api_url = "https://combinedbotbackend.onrender.com/query"

    # Prepare the payload
    payload = {
        "query": user_query
    }

    # Make the POST request to the API
    response = requests.post(api_url, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json()
        # Display the response
        st.success("Response from API:")
        st.json(response_data)
    else:
        st.error("Error: Unable to get a response from the API.")
