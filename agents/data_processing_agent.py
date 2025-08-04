from utils.openai_utils import call_openai

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following text:\n\n{text}"
    response = call_openai(prompt)
    return response