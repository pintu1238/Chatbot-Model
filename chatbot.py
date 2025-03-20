import streamlit as st
from openai import OpenAI

# Streamlit UI
st.header("GNA DeepSeek Model Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# API Key (store securely)
API_KEY = "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"

# Function to get response from DeepSeek API
def get_deepseek_response(messages):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=API_KEY,
    )

    response = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "your-site.com",  # Replace with your actual site URL
            "X-Title": "Your Site Name",  # Replace with your actual site name
        },
        extra_body={},
        model="deepseek/deepseek-r1-zero:free",
        messages=messages
    )

    return response.choices[0].message.content

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
question = st.text_input("Enter your question:")

# Button to send message
if st.button("Check Answer"):
    if question.strip():
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": question})

        # Get AI response
        answer = get_deepseek_response(st.session_state.messages)

        # Add AI response to history
        st.session_state.messages.append({"role": "assistant", "content": answer})

        # Refresh page to show new messages
        st.rerun()
    else:
        st.warning("Please enter a question first.")
