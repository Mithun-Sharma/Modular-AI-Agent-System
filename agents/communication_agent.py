from utils.openai_utils import call_openai

def chat_response(message: str) -> str:
    prompt = f"You are a helpful assistant. Answer the user's question:\n\n{message}"
    response = call_openai(prompt)
    return response