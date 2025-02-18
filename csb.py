import streamlit as st

st.title("Customer Service Chatbot")

# Adding custom styling to the iframe for better design
st.markdown("""
    <style>
        .iframe-container {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f7f7f7;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            margin-top: 30px;
        }
        iframe {
            border-radius: 8px;
            border: 2px solid #ececec;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            width: 350px;
            height: 500px;
        }
    </style>
    <div class="iframe-container">
        <iframe src="https://tawk.to/chat/67b4befc9db312190dfc49e9/1ikd0k2uq" 
        allowTransparency="true"></iframe>
    </div>
""", unsafe_allow_html=True)
