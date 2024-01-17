#Install streamlit langchain openai wikipedia chromadb tiktoken

import os
from API_Key import apikey

import streamlit as st
from langchain_openai import OpenAI #this is going to help us leverage a large language model
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

os.environ['OPENAI_API_KEY'] = apikey

#App framework
st.title('LangChain GPT Test')
prompt = st.text_input('Ask me anything..')

#prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'],
    template='write me what is {topic}'
)

script_template = PromptTemplate(
    input_variables = ['title', 'wikipedia_research'],
    template='write me a script on the title TITLE {title} but also while leveraging this wikipedia research {wikipedia_research}'
)

#memory
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

#llms
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)

#Order is important here as this works as a list, picks out the first variabe(chain).. and then passes the output to the second chain
# sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], verbose=True) 

#for sequential chain we can give the specified inputs variables and output variables
# sequential_chain = SimpleSequentialChain(chains=[title_chain, script_chain], input_variable=['title'],
                                        #  output_variables=['title','script'], verbose=True) 

wiki = WikipediaAPIWrapper()

#show stuff to the screen if there is one
if prompt:
    # response = sequential_chain.run(prompt) #for simple Sequential Chain
    # st.write(response)
    # response = sequential_chain.run({'topic':prompt})

    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)
    script = script_chain.run(title=title, wikipedia_research=wiki_research)

    st.write(title)
    st.write(script)

    with st.expander('title History'):
        st.info(title_memory.buffer)

    with st.expander('script History'):
        st.info(script_memory.buffer)

    with st.expander('Wikipedia Research'):
        st.info(wiki_research)