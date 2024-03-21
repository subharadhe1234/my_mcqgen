import os
import json
import pandas as pd
import traceback

from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file,get_table_data
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import streamlit as st
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain

with open('D:\progect\mcqgen\Response.json', 'r') as file:
   RESPONSE_JSON = file.read()

st.title('MCQ Creator Application with langchain')

with st.form('user_input'):
   uploaded_file=st.file_uploader('uplode a file')
   mcq_count=st.number_input('No of MCQs')
   tone=st.text_input('Complexity Level Of Questions')
   subject=st.text_input('Insert Subkect')
   button=st.form_submit_button('create MCQs')

   if button and uploaded_file is not None and mcq_count and subject and tone:
      with st.spinner('loading....'):
          
        try:
            text= read_file(uploaded_file)
            with get_openai_callback() as cb:
                response=generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject":subject,
                        "tone": tone,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                    )
        except Exception as e:
            traceback.print_exception(type(e),e,e.__traceback__)
            st.error("Error")
        else:
            print(f"Total Tokens:{cb.total_tokens}")
            print(f"Prompt Tokens:{cb.prompt_tokens}")
            print(f"Completion Tokens:{cb.completion_tokens}")
            print(f"Total Cost:{cb.total_cost}")
            if isinstance(response,dict):
                quiz=response.get('quiz',None)
                if quiz is not None:
                    logging.info(quiz)
                    table_data=get_table_data(quiz)
                    if table_data is not None:
                        logging.info(table_data)
                        df=pd.DataFrame(table_data)
                        logging.info(df)
                        df.index=df.index+1
                        st.table(df)
                        st.text_area(label="Review",value=response['review'])
                    else:
                        st.error("error is in your table")
                else:
                    st.write(response)


             
           
         
              
            


















