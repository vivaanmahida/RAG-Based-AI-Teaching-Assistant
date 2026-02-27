import streamlit as st
from Process_incoming import process_query

st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 RAG-Based AI Teaching Assistant")
st.markdown("Ask questions from Sigma Web Development Course videos.")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display old messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input box
user_input = st.chat_input("Ask your question here...")

if user_input:
    # Show user message
    st.chat_message("user").write(user_input)
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Processing spinner
    with st.spinner("Thinking..."):
        try:
            response, sources = process_query(user_input)
        except Exception as e:
            response = f"⚠️ Error: {str(e)}"

    # Show assistant response
    st.chat_message("assistant").write(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Optional: Show source chunks
    with st.expander("📚 Retrieved Video Chunks"):
        st.dataframe(
            sources[["title", "number", "start", "end"]]
        )