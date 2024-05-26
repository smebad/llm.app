import streamlit as st
from langchain.llms import OpenAI

# Function to generate LLM response
def generate_response(input_text, openai_api_key):
    if not openai_api_key:
        st.warning('Please enter your OpenAI API key!')
        return
    
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text)
    st.info(response)

# Addin some styling to the layout
st.title('🤖🔗 TextMosaic: Unleash the Power of Language')
openai_api_key = st.sidebar.text_input('OpenAI API Key')
st.sidebar.markdown("[Get OpenAI API Key](https://platform.openai.com/signup)")
st.sidebar.markdown("[How to use the API Key?](https://platform.openai.com/docs/guides/authentication)")

#  User input form
with st.form('my_form'):
    text = st.text_area('Enter text:', '...')
    submitted = st.form_submit_button('Submit')

# Generate response on submit
if submitted:
    generate_response(text, openai_api_key)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Created by: [Syed Muhammad Ebad](https://github.com/smebad)")
st.sidebar.markdown("Contact: [Email](mailto:mohammadebad1@hotmail.com)")
