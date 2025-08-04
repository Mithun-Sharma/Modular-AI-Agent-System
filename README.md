# Modular AI Agent System with Multi-Agent Architecture and FastAPI

## Overview
This project demonstrates a modular AI system using FastAPI, LangGraph-style routing, and OpenAI's GPT-4o-mini model.

## Features
- **Data Processing Agent**: Text summarization
- **Communication Agent**: Responds to user queries
- **Routing Agent**: Decides which agent handles which task
- **API Layer**: FastAPI

---

## Setup & Run (VSCode or Colab)

### 1. Create a `.env` file in your project root:
```
OPENAI_API_KEY=your_openai_api_key
```

### 2. Install dependencies:
```
pip install -r requirements.txt
```

> Make sure you also install:
```
pip install python-dotenv
```

### 3. Run the FastAPI server:
```
uvicorn main:app --reload
```

### 4. Open API Docs:
Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Example API Usage

### POST /agent/

**Request:**
```json
{
  "task_type": "summarize",
  "content": "Large texts go here..."
}
```

**OR**

```json
{
  "task_type": "chat",
  "content": "What is modular AI architecture?"
}
```

---

## How It Works

- `utils/openai_utils.py` loads the API key using `python-dotenv` from your `.env` file.
- The routing agent decides whether the input is for summarization or chatbot response.
- Each agent uses OpenAI's `gpt-4o` model to perform its task.

## Notes

- Ensure your OpenAI API key is active and has access to `gpt-4o-mini`.
- You must restart the server if you change the `.env` file.clear

