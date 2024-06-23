
from langchain_openai import ChatOpenAI
# from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st 
import os 

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Jesteś autorem bajek, wierszy i fraszek. Napisz śmieszną fraszkę o zwierzatku, na 4 wersy. Niech będzie zabawny, ale nie prześmiewczy. Weż pod uwagę dane o zwierzęciu podane poniżej."),
        ("user","Question: {question}")
    ]
)

# streamlit
st.title("Langchain Chat with OpenAI")
input_text = st.text_input("Opisz swojego zwierzaka, a ja napiszę o nim wierszyk.","""imie: Bajtek
gatunek: pies
rasa: mieszaniec
charakterystyka: szybki, kochany, przywiązany, oddany, lubi patyki i spacery, lubi mięsko i wino""")

# OpenAI LLM
# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-4o")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
