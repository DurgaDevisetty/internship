import streamlit as st
from openai import OpenAI

st.sidebar.title('Generative AI ')
st.header('Code Reviewer')

f = open('my_key.txt')
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

query = st.sidebar.text_area('Enter Query : ')
if st.sidebar.button('Submit'):
    st.balloons()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "analyze the submitted code and identify potential bugs, errors, or areas of improvement"},
            {"role": "user", "content": query}
        ]
    )
    st.write(response.choices[0].message.content)
