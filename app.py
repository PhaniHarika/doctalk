import streamlit as st
from rag_engine import (
    extract_text_from_pdfs,
    split_text_into_chunks,
    build_vector_store,
    build_conversation_chain
)

st.set_page_config(
    page_title="DocTalk",
    page_icon="📄",
    layout="centered"
)

# ── Session state ─────────────────────────────────
if "conversation" not in st.session_state:
    st.session_state.conversation = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False
if "chunk_count" not in st.session_state:
    st.session_state.chunk_count = 0

# ── Sidebar ───────────────────────────────────────
with st.sidebar:
    st.title("📄 DocTalk")
    st.caption("Chat with your PDFs using AI")
    st.divider()

    uploaded_files = st.file_uploader(
        "Upload PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("⚡ Process PDFs", type="primary"):
        if uploaded_files:
            with st.spinner("Reading and indexing..."):
                raw_text = extract_text_from_pdfs(uploaded_files)
                chunks = split_text_into_chunks(raw_text)
                vector_store = build_vector_store(chunks)
                st.session_state.conversation = build_conversation_chain(vector_store)
                st.session_state.pdf_processed = True
                st.session_state.chunk_count = len(chunks)
            st.success(f"✅ {len(chunks)} chunks indexed!")
        else:
            st.warning("Please upload at least one PDF first.")

    if st.session_state.pdf_processed:
        st.divider()
        st.metric("Chunks indexed", st.session_state.chunk_count)
        if st.button("🔄 Clear Chat"):
            st.session_state.chat_history = []
            st.rerun()

# ── Main ──────────────────────────────────────────
st.title("📄 DocTalk")
st.caption("Upload a PDF · Ask anything · Get answers instantly")
st.divider()

if not st.session_state.pdf_processed:
    st.info("👈 Upload a PDF from the sidebar and click **Process PDFs** to get started!")

else:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_question = st.chat_input("Ask anything about your PDF...")

    if user_question:
        with st.chat_message("user"):
            st.write(user_question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.conversation.invoke(user_question)
            st.write(response)

        st.session_state.chat_history.append({"role": "user", "content": user_question})
        st.session_state.chat_history.append({"role": "assistant", "content": response})