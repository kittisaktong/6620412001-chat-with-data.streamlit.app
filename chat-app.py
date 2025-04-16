import streamlit as st
import pandas as pd

# Config
st.set_page_config(
    page_title="Chat with Data 📊💬",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Title
st.title("💬 chat.app")
st.caption("Talk with your data like never before.")

st.markdown("---")

# Cached file loader for performance
@st.cache_data(show_spinner=False)
def load_csv(file):
    try:
        return pd.read_csv(file)
    except Exception as e:
        st.error(f"Failed to load CSV: {e}")
        return None

# File uploaders
st.subheader("📚 Upload Data Dictionary")
data_dict_file = st.file_uploader(
    "Drag and drop your Data Dictionary (CSV)", 
    type=["csv"], 
    key="data_dict",
    help="Max size: 200MB"
)

st.subheader("💳 Upload Transaction Data")
transaction_file = st.file_uploader(
    "Drag and drop your Transaction Data (CSV)", 
    type=["csv"], 
    key="transaction_data",
    help="Max size: 200MB"
)

# Display previews if uploaded
if data_dict_file:
    st.success("✅ Data Dictionary uploaded!")
    data_dict_df = load_csv(data_dict_file)
    if data_dict_df is not None:
        st.write("🔍 **Preview:**")
        st.dataframe(data_dict_df)

if transaction_file:
    st.success("✅ Transaction Data uploaded!")
    transaction_df = load_csv(transaction_file)
    if transaction_df is not None:
        st.write("🔍 **Preview:**")
        st.dataframe(transaction_df)

st.markdown("---")
st.info("Once both files are uploaded, analysis and chat features will be enabled.")
