import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(question: str, answer: str) -> str:
    prompt = f"""
    You are an assistant that reformulates FAQs.

    Question: {question}
    Answer: {answer}

    Generate a clearer, concise response for a public FAQ page.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()
