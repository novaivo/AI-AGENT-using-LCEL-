# 🤖 AI Tool Agent

A smart, friendly AI agent built with **LangChain**, powered by **OpenRouter’s Meta LLaMA3**, and equipped with real-world tools like:

- 📐 Calculator
- 🌦️ Weather Info
- 📚 Wikipedia Lookup
- 📂 File Reader (TXT, PDF, DOCX)
- 💬 WhatsApp Messaging (via Twilio)
- 📊 CSV Statistics Analyzer
- 🗄️ SQLite Query Executor

It uses LangChain’s `AgentExecutor` + `create_tool_calling_agent` with ReAct reasoning — just like a thinking assistant!

---

## 🌟 Features

✅ Uses blazing-fast `meta-llama/llama-3-8b-instruct` via OpenRouter  
✅ ReAct-based agent logic (step-by-step reasoning)  
✅ Clean explanations after tool use  
✅ CLI-based assistant  
✅ Modular tools built with `@tool` decorator  
✅ Smart tool selection by LLM

---

## 📂 Project Structure

```
.
├── main.py              # CLI entry point
├── agent_logic.py       # Agent setup (LLM + tools + executor)
├── llm_setup.py         # LLM + Prompt setup
├── calculator.py        # Math tool
├── weather.py           # Weather via OpenWeatherMap
├── wikipedia.py         # Wikipedia search
├── file.py              # File reader (PDF, DOCX, TXT)
├── csv_tool.py          # CSV statistics analyzer
├── whatsapp_tool.py     # WhatsApp messaging via Twilio
├── sqlite_tool.py       # SQL queries on .db files
├── requirements.txt     # Dependencies
└── .env                 # API Keys
```

---

## 🛠️ Setup Instructions

### 1. 🔽 Clone the Repo
```bash
git clone https://github.com/novaivo/AI-AGENT-using-LCEL-
cd AI-AGENT-using-LCEL-
```

### 2. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```


# 🔑 OpenRouter API (for LLaMA 3 via openrouter.ai)
openrouter_API_KEY=your_openrouter_key



# 🧠 LangSmith Observability (https://smith.langchain.com/)
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=SMART AI AGENT
LANGCHAIN_TRACING_V2=true


# Weather
weather_api_key=your_openweather_key



# Twilio WhatsApp
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
```

---

## 🚀 Run the Agent

```bash
python main.py
```

You’ll see:
```
🌟 Welcome to your AI Tool Buddy! 🤖✨
I'm ready to answer your questions using my smart toolbox! 🧠🔧
```

---

## 💬 Example Prompts

| Prompt | Tool Used |
|--------|-----------|
| `What is 25 * 12?` | Calculator |
| `What's the weather in Lahore?` | Weather |
| `Who was Nikola Tesla?` | Wikipedia |
| `Read file: notes.pdf` | File Tool |
| `Send WhatsApp to +923001234567 saying hello` | WhatsApp Tool |
| `Analyze: data.csv` | CSV Tool |
| `Tell howw many  touch screen laptop are there  in the  the " put ur database path here"` | SQLite Tool |

---

## 🔌 Tool Highlights

### 💬 WhatsApp Messaging (Twilio Sandbox)

```

> ⚠️ You and your team must join Twilio Sandbox by sending a `join <code>` message to Twilio’s test number.

```

---

### 📊 CSV Stats Tool
Get data insights like:
- Rows and columns
- Missing values
- Data types
- Statistical summary





---

## 🧰 Powered By

- [LangChain](https://www.langchain.com/)
- [OpenRouter LLaMA3](https://openrouter.ai/)
- [Twilio WhatsApp Sandbox](https://www.twilio.com/)
- [OpenWeatherMap](https://openweathermap.org/)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)
- [python-docx](https://python-docx.readthedocs.io/en/latest/)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [pandas](https://pandas.pydata.org/)

---

## ✨ Future Improvements

- Agent memory (long-term context)  
- Web UI with Streamlit  
- Notifications, alarms, search engine tools  
- GitHub Actions for auto-deploy

---

## 📄 License

MIT License — free to use, share, and build upon ✨

---


## 👩‍💻 Author

Made with 💖 by [marse]  
GitHub: [github.com/novaivo](https://github.com/novaivo)

---
