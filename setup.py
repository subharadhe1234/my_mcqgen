from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='RAdhe Radhe',
    author_email='subhadippratihar09@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)