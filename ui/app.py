import streamlit as st
import sys
import os

# -----------------------------------
# Project Path Setup
# -----------------------------------

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from services.support_service import process_question
from dashboard.dashboard_view import show_dashboard

# -----------------------------------
# Page Config
# -----------------------------------

st.set_page_config(
    page_title="Agentic Support Hub",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# Sidebar Navigation
# -----------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Support Assistant",
        "Dashboard"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    """
    ### 👨‍💻 Developer

    **Abhishek Gupta**

    AI Engineer | Full Stack Developer

    Agentic Support Hub MVP
    """
)

st.sidebar.caption(
    "Powered by Python, Ollama, RAG & Streamlit"
)

# ====================================================
# SUPPORT ASSISTANT PAGE
# ====================================================

if page == "Support Assistant":

    st.title("🤖 Agentic Support Hub")

    st.markdown(
        """
        Ask questions related to:

        - ChatGPT Enterprise
        - Codex
        - OpenAI API
        - Partner U
        - Hackathon Enablement
        - Access & Troubleshooting
        """
    )

    st.markdown("---")

    question = st.text_input(
        "Enter your question:"
    )

    if st.button(
        "Submit",
        use_container_width=True
    ):

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            with st.spinner(
                "Processing your request..."
            ):

                result = process_question(
                    question
                )

            # Status Message

            if result["escalated"]:

                st.warning(
                    "Case created and escalated for human review."
                )

            else:

                st.success(
                    "Case created and resolved by AI."
                )

            st.markdown("---")

            # Case Information

            col1, col2 = st.columns(2)

            with col1:

                st.markdown(
                    "### 📌 Case ID"
                )

                st.code(
                    result["case_id"]
                )

            with col2:

                st.markdown(
                    "### 🏷 Product"
                )

                st.write(
                    result["product"]
                )

            st.markdown(
                "### 📖 Knowledge Article"
            )

            st.info(
                result["article"]
            )

            # Confidence

            confidence = result["confidence"]

            st.markdown(
                "### 🎯 Confidence Score"
            )

            if confidence >= 0.70:

                st.success(
                    f"{confidence}"
                )

            elif confidence >= 0.50:

                st.warning(
                    f"{confidence}"
                )

            else:

                st.error(
                    f"{confidence}"
                )

            # Resolution

            st.markdown(
                "### 📋 Resolution Status"
            )

            if result["escalated"]:

                st.error(
                    "⚠ Escalated To Human Support"
                )

            else:

                st.success(
                    "✅ AI Resolved"
                )

            # AI Response

            st.markdown(
                "### 🤖 AI Response"
            )

            st.write(
                result["response"]
            )

# ====================================================
# DASHBOARD PAGE
# ====================================================

elif page == "Dashboard":

    show_dashboard()