import requests
import streamlit as st

headers = {"Authorization": f"Bearer {st.secrets.API_TOKEN}"}
        # [{"Context":"Please summarize this into a job description."}]
API_URL = f"https://api-inference.huggingface.co/models/{st.secrets.MODEL}"

@st.cache_data
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Add title and subtitle to the main interface of the app
st.title("Aware Wolf: Service Update Scanner")
st.subheader("See what's up with when they lay it down")
st.markdown(":blue[Summarize those pesky ToC and PP updates at the Click of a Button!]")

# Add sidebar to the app
st.sidebar.markdown("### Competitive Intelligence Solutions for your Business!")
st.sidebar.markdown("#### :blue[Developed @ AgentC Laboratories]")
st.sidebar.markdown("##### :gray[Copyright 2024. Artificial Intelligentsia, LLC.]")
st.sidebar.markdown("##### :gray[All rights reserved.]")

# Add two columns to the app
col1, col2 = st.columns(2)
with col1:
    text_input = st.text_area("Paste that update word salad below and activate the Aware Wolf...", height=200)
    context = "\n\n#### Please summarize this dense legalese, regarding updates to service terms and data privacy, into simple terms that laypeople can understand. ###"
    # focus = "\n\n## Please be sure to highlight any peculiar changes and/or odd data handling practices, including, but not limited to third party handling and potential ways to protect your data. ##\n\n"
    # sale = "\n\n# Please suggest any potential open source alternatives to the software described in the request that the user may be able to use instead. #\n\n"
    text_input = text_input + context # + focus + sale
with col2:
    submit = st.button("Activate the Aware Wolf")
    if text_input and submit:
        out = query({"inputs": text_input})
        out = st.write(out, height=200, label="Summary:")