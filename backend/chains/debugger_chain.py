import os
import json
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from prompts.debugger_prompt import debugger_prompt

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3
)

debugger_chain = debugger_prompt | llm | StrOutputParser()


def run_debugger(code: str, language: str):
    response = debugger_chain.invoke({
        "code": code,
        "language": language
    })

    # 🔥 Try parsing JSON safely
    try:
        parsed = json.loads(response)
        return parsed
    except:
        return {
            "issues": [],
            "explanation": response,
            "fixed_code": "",
            "improvements": []
        }