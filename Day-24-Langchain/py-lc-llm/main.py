import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from constant.defs import get_defs
from helper.helpers import to_markdown

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

integration = get_defs("GoogleAI")
model = integration[0]

llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key) # For OpenAI this is OpenAI()

# prompt = PromptTemplate.from_template(f"Write a {language} that will {task}")
# chain = LLMChain(llm=llm, prompt=prompt)

if __name__ == "__main__":
    language = "python"
    task = "print numbers from 1 to 10"
    prompt = f"Write a {language} that will {task}"
    # response = chain.invoke({"language": language, "task": task})
    response = llm.invoke(input=prompt)
    print(response.content)