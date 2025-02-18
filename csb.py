import streamlit as st

st.title("Customer Service Chatbot")

# Embed Tawk.to widget using iframe
st.markdown("""
    <iframe src="https://tawk.to/chat/67b4befc9db312190dfc49e9/1ikd0k2uq" 
    width="350" height="500" style="border:none;overflow:hidden" 
    allowTransparency="true"></iframe>
""", unsafe_allow_html=True)
