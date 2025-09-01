from .prompt_builder import build_blog_prompt
import openai, time, os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_blog(question: str, answer: str, retries: int = 3) -> str:
    prompt = build_blog_prompt(question, answer)
    for attempt in range(retries):
        try:
            response = openai.chat.completions.create(  # <-- updated method
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content  # <-- updated access
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                raise e
