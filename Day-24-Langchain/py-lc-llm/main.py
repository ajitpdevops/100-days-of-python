import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import openai
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from constant.defs import get_defs
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers")
parser.add_argument("--language", default="python")
parser.add_argument("--provider", default="google")
args = parser.parse_args()

load_dotenv()
# api_key = os.getenv("GOOGLE_API_KEY")

integration = get_defs("GoogleAI")
model = integration[0]

provider = args.provider

if provider == 'google':
    llm = ChatGoogleGenerativeAI(model='gemini-pro') # For OpenAI this is OpenAI()
elif provider == 'openai':
    llm = OpenAI()

code_prompt = PromptTemplate(
    template="Write a {language} code, that will {task}",
    input_variables=['language', 'task']
    )

test_prompt = PromptTemplate(
    template="write a test in {language} for the following code {code}",
    input_variables=['language', 'code']
)

code_chain = LLMChain(
    llm=llm,
    prompt=code_prompt,
    output_key="code"
)

test_chain = LLMChain(
    llm=llm,
    prompt=test_prompt,
    output_key='test',
)

chain = SequentialChain(
    chains=[code_chain, test_chain],
    input_variables=['language', 'task'],
    output_variables=['test', 'code']
)

result = chain.invoke({
    "language": args.language,
    "task": args.task
})


# print(result)
# print(f"Text Key: {result['text']}")
print(">>>>>> GENERATED CODE >>>>>>>>")
print(result['code'])

print(">>>>>> GENERATED TEST >>>>>>>>")
print(result['test'])