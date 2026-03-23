from langchain_core.prompts import PromptTemplate

debugger_prompt = PromptTemplate(
    input_variables=["code", "language"],
    template="""
You are an expert senior software engineer and debugger.

Analyze the following code carefully.

Tasks:
1. Identify all bugs and issues
2. Explain clearly
3. Provide corrected code
4. Suggest improvements

IMPORTANT:
- Return ONLY valid JSON
- Do NOT include markdown or extra text
- Ensure JSON is properly formatted

Format:
{{
  "issues": ["..."],
  "explanation": "...",
  "fixed_code": "...",
  "improvements": ["..."]
}}

Code:
{code}

Language:
{language}

Return response in this JSON format:
{{
  "issues": [],
  "explanation": "",
  "fixed_code": "",
  "improvements": []
}}
"""
)