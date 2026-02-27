import streamlit as st
from Process_incoming import process_query

st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 RAG-Based AI Teaching Assistant")
st.markdown("Ask questions from Sigma Web Development Course videos.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "sources" not in st.session_state:
    st.session_state.sources = None

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input = st.chat_input("Ask your question here...")

if user_input:

    st.chat_message("user").write(user_input)
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.spinner("Thinking..."):
        try:
            response, sources = process_query(user_input)
            st.session_state.sources = sources
        except Exception as e:
            response = f"⚠️ Error: {str(e)}"
            st.session_state.sources = None

    st.chat_message("assistant").write(response)
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

# Show table only if sources exist
if st.session_state.sources is not None:
    with st.expander("📚 Retrieved Video Chunks"):
        st.dataframe(
            st.session_state.sources[["title", "number", "start", "end"]]
        )