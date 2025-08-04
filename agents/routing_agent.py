from agents.data_processing_agent import summarize_text
from agents.communication_agent import chat_response

def route_task(task_type: str, content: str) -> str:
    if task_type == "summarize":
        return summarize_text(content)
    elif task_type == "chat":
        return chat_response(content)
    else:
        return "Unknown task type"