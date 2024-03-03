import streamlit as st
from chat import get_response
st.write('<style>body { background-color: white; }</style>', unsafe_allow_html=True)
st.title("🤖 Tourist Chat Bot App")


chat_placeholder = st.empty()
user_input = st.text_input("You:")
if user_input:
  bot_response = get_response(user_input)
  st.write(f"Bot: {bot_response}")