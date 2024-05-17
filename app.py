import streamlit as st
import os
from streamlit.components.v1 import html
from typing import List
from langchain_community.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain import PromptTemplate
from PIL import Image

# Configuration of the app : PremAI
os.environ['REPLICATE_API_TOKEN'] = st.secrets["REPLICATE_API_TOKEN"]
max_tokens = st.secrets["max_tokens"]


if max_tokens == None:
    max_tokens = 1500

# Loading the model
model_id = "snowflake/snowflake-arctic-instruct"


# Adding UI/UX
image = Image.open('logo.jpg')
st.set_page_config(page_title="Prem Doctor")
st.image(image, caption='')

html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

with st.sidebar:
    st.markdown("""
    # About 
    Prem Doctor is a helper tool built on [LangChain](https://langchain.com) and [Snowflake Arctic](https://huggingface.co/Snowflake/snowflake-arctic-instruct) to analyze, detect and answer people's health questions, without exposing their information to third parties or storing it.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How does it work
    Just write the health problem you have and wait for the answer.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by [Néstor Campos](https://www.linkedin.com/in/nescampos/)
    """,
    unsafe_allow_html=True,
    )

st.markdown("""
    # Prem Doctor
    """)

st.markdown("""
#### Enter the information of the disease or health problem that afflicts you, and if possible, your age or some other condition or state in order to analyze and give you a better answer. YOUR DATA IS NOT STORED, SO YOU CAN TRUST THAT THIS REMAINS BETWEEN US ;)
""")


illness = st.text_area("Describe your ailment or disease in detail to help you.", placeholder="Describe your ailment or disease in detail to help you.")


def generate_arctic_response(question):
  if get_num_tokens(question) >= max_tokens:
    st.error("Conversation length too long. Please keep it under 3072 tokens.")
    st.button('Clear chat history', on_click=clear_chat_history, key="clear_chat_history")
    st.stop()

  for event in replicate.stream(model_id,input={"prompt": prompt_str,"temperature": 0.3,"top_p": 0.9,}):
    yield str(event)

#if illness:
if st.button("Ask Prem Doctor"):
  healthhelper_template = """You are a bot that helps with health problems.
    As an assistant, you must answer all health-related questions, resolve any medical ailments, or indicate the type of doctor the person should see.
    The person will write their symptoms to you and you will have to generate a possible diagnosis or diseases they may have.
    When you get the info from the person, give the best possible diagnosis. If necessary, tell the person to be more precise in describing their problem.
    Deliver the best result from the information you have available.
    Finally, tell the person that they need to see a real doctor to be sure of their problem and, if possible, what type of doctor they should see.
  Question: {question}"""

  answer = generate_arctic_response(illness)

  st.text(f"Answer from Prem Doctor:\n\n{answer}\n\n")
