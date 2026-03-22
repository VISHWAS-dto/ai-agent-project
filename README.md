# Build_AI_Agent with Groq + Tavily Search

## Overview

This project is an **AI-powered agent** built using **LangChain + LangGraph + Groq LLM**, integrated with **Tavily Search API** to provide real-time, intelligent responses.

The agent can:

* Answer user queries intelligently 
* Perform web search when needed 
* Combine LLM reasoning with external tools 

---

## Tech Stack

* **Python**
* **LangChain**
* **LangGraph**
* **Groq (LLaMA 3.3 70B)**
* **Tavily Search API**

---

## Features

*  Smart AI assistant using Groq LLM
*  Tool-enabled agent (search capability)
*  Real-time information retrieval
*  Clean and modular code structure

---

## Project Structure

```
.
├── app.py                # Main AI agent code
├── ai_model.ipynb        # Experimentation notebook
├── requirements.txt      # Dependencies
├── .env                  # API keys (not uploaded)
```

---

## Setup Instructions

### 1 Clone the repository

```bash
git clone https://github.com/VISHWAS-dto/ai-agent-project.git
cd ai-agent-project
```

---

### 2 Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4 Add API keys

Create a `.env` file and add:

```
GROQ_API_KEY=your_groq_api_key  # It is Free 
TAVILY_API_KEY=your_tavily_api_key
```

---

### 5 Run the project

```bash
python app.py
```

---

##  Example Usage

```
Input: "Ask Any type of Question like LLM models"
Output: AI-generated response with real-time insights
```

---

## Security Note

* API keys are stored in `.env`
* `.env` is excluded from GitHub using `.gitignore`

---

## Future Improvements

* Add web UI (Streamlit/React)
* Deploy on cloud (Render/Streamlit Cloud)
* Add memory to agent
* Multi-tool integration

---

## Author

**Vishwas Shankar**

---

## If you like this project

Give it a Star on GitHub!
