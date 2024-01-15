import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")


print(api_key)