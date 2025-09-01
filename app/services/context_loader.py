import os

CONTEXT_DIR = "app/context"

def load_context() -> str:
    context_texts = []
    for filename in os.listdir(CONTEXT_DIR):
        if filename.endswith(".txt") and filename not in ["ANCHOR.txt", "blog_template.txt"]:
            path = os.path.join(CONTEXT_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                context_texts.append(f.read())
    return "\n\n".join(context_texts)
