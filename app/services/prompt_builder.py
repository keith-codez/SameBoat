from .context_loader import load_context

ANCHOR_FILE = "app/context/ANCHOR.txt"
TEMPLATE_FILE = "app/context/blog_template.txt"

def load_anchor_tone() -> str:
    with open(ANCHOR_FILE, "r", encoding="utf-8") as f:
        return f.read()

def load_template() -> str:
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        return f.read()

def build_blog_prompt(question: str, answer: str) -> str:
    context = load_context()
    tone = load_anchor_tone()
    template = load_template()

    return f"""
You are an expert content writer. Write a clear, engaging blog article in British English.

FAQ Question: {question}
FAQ Answer: {answer}

Tone of Voice:
{tone}

Additional Context:
{context}

Writing Guide (Template to follow loosely, not word-for-word):
{template}

Instructions:
- Write a human-friendly blog article in plain prose (ready for Word docs).
- Structure naturally with headings and short paragraphs.
- Do not repeat the FAQ in Q&A form – weave it into the narrative.
- Avoid JSON or Markdown formatting.
- At the end, include:
   • A "Tags" section with 3 to 5 relevant tags.  
   • A "References" section with 2 to 4 realistic sources (websites, reports, or articles).
"""
