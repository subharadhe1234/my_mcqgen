import os
import json
import pandas as pd
import traceback
import PyPDF2
from src.mcqgenerator.logger import logging

def read_file(file):
    if file.name.endswith('.pdf'):
        logging.info(file.name.endswith(".pdf"))
        
        try:
            pdf_reader=PyPDF2.PdfFileReader(file)
            logging.info(pdf_reader)
            text=''
            for page in pdf_reader.pages:
                text+=page.extract_text
                logging.info(text)
                return text
        except Exception as e:
            logging.info(e)
            raise Exception('error reading the PDF file ')
    elif file.name.endswith('.txt'):
        logging.info(file.name.endswith('.txt'))
        logging.info(file.read().decode('utf-8'))
        return file.read().decode('utf-8')
    else :
        logging.info('unsupported file formate only pdf and text file supported')
        raise Exception('unsupported file formate only pdf and text file supported')

def get_table_data(quiz_str):
    logging.info(quiz_str)
    try:
        quiz_dict=json.loads(quiz_str)
        logging.info(quiz_dict)
        quiz_table_data = []
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                    ]
                )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": f"ans: {correct}"})
        return quiz_table_data
    except Exception as e:
        traceback.print_exception(type(e),e,e.__traceback__)
        return False





















