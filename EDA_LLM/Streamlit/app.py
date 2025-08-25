import streamlit as st
from streamlit_chat import message

# Streamlit app layout
st.title("Chatbot Interface")

# Display messages
message("My message") 
message("Hello bot!", is_user=True)  # Aligns the message to the right
