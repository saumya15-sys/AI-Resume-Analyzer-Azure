from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("FOUNDRY_API_KEY"),
    base_url=os.getenv("FOUNDRY_ENDPOINT")
)

def analyze_resume(resume_text):

    prompt = f"""
Analyze this resume.

Return:

1. Professional Summary

2. Technical Skills

3. Strengths

4. Missing Skills

5. Suitable Job Roles

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model=os.getenv("FOUNDRY_MODEL"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content