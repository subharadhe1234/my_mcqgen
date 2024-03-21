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