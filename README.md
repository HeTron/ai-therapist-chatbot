# 🧠 Sage — Your AI Therapist

Sage is a virtual therapist chatbot designed to provide a calming, supportive, and reflective space for users to talk. Built using LangChain, OpenAI, and Streamlit, Sage mimics the tone and flow of a thoughtful mental health professional — with empathetic responses and guided questions.

---

## 🌐 Live Demo

Try Sage live on Streamlit Cloud:  
👉 [https://hetron-ai-therapist-chatbot.streamlit.app](https://hetron-ai-therapist-chatbot.streamlit.app)

[![View App](https://img.shields.io/badge/Live%20App-Streamlit-blue?logo=streamlit)](https://hetron-ai-therapist-chatbot.streamlit.app)

---

## 🚀 Overview

- ✨ Empathetic therapist persona created through prompt engineering
- 🔁 Conversational memory to recall past messages in the session
- 🛠️ Built with OpenAI’s GPT-3.5-turbo via LangChain
- 💻 Simple and clean Streamlit UI
- 🔒 API key stored securely using `.env`

---

## 📁 Project Structure

```
ai-therapist-chatbot/ 
├── app.py # Streamlit app 
├── src/ 
│ ├── chain.py # LangChain logic and memory 
├── prompts/ 
│ └── therapist.txt # Persona prompt template 
├── .env.example # API key template 
├── requirements.txt 
└── README.md
```


---

## 🛠️ How to Run Locally

1. Clone the repo  
2. Create a `.env` file using `.env.example`:
OPENAI_API_KEY=your-api-key-here
3. Install requirements:

```bash
pip install -r requirements.txt
```
4. Launch the chatbot:
```
streamlit run app.py
```

## 💡 Notes
This project was created as a portfolio piece to demonstrate how LLMs can be guided to reflect human empathy and thoughtful tone. While not a replacement for professional therapy, Sage shows how language models can be shaped into emotionally intelligent interfaces.

## 📎 Links
[💻 Live App](https://hetron-ai-therapist-chatbot.streamlit.app)

[📁 GitHub Repository](https:/github.com/HeTron/ai-therapist-chatbot)

[🌐 Portfolio Site](https://aibotcoder.com/portfolio.html)