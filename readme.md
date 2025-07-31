# 🤖 AI Tool Agent

A smart, friendly AI agent built with **LangChain**, powered by **Groq’s LLaMA3**, and equipped with real-world tools like:

- 📐 Calculator
- 🌦️ Weather Info
- 📚 Wikipedia Lookup
- 📂 File Reader (TXT, PDF, DOCX)

This project uses LangChain’s `AgentExecutor` and `create_react_agent` with `RunnableSequence` support to decide when and how to use each tool — just like an intelligent assistant would!

---

## 🌟 Features

✅ Uses Groq’s blazing-fast LLaMA3-8B-8192  
✅ Step-by-step reasoning using ReAct Agent  
✅ Natural language interface via CLI  
✅ Modular tools using `@tool` decorator  
✅ Clean, friendly explanations after tool use

---

## 📂 Project Structure

```
.
├── main.py              # CLI entry point
├── agent_logic.py       # Agent setup (LLM + tools + agent)
├── llm_setup.py         # LLM + Prompt setup
├── calculator.py        # Math tool (uses Math.js)
├── weather.py           # Weather tool (OpenWeatherMap API)
├── wikipedia.py         # Wikipedia lookup tool
├── file.py              # File reader (PDF, DOCX, TXT)
├── .env                 # API key storage
└── requirements.txt     # Dependencies
```

---

## 🛠️ Setup Instructions

### 1. 🔽 Clone the Repo
```bash
git clone https://github.com/novaivo/AI-AGENT-using-LCEL-
cd ai-tool-agent
```

### 2. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. 🔑 Add API Keys

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key
```

(Optional) Edit weather API key inside `weather.py`.

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

## 💡 Example Prompts

| Prompt | What Happens |
|--------|---------------|
| `What is 25 * 12?` | Uses calculator tool |
| `What's the weather in Karachi?` | Calls weather tool |
| `Who is Alan Turing?` | Uses Wikipedia API |
| `Read file: resume.pdf` | Reads local PDF/DOCX/TXT |

---

## 🧰 Powered By

- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/) LLaMA3 API
- [OpenWeatherMap](https://openweathermap.org/)
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page)
- [Math.js API](https://api.mathjs.org/)
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF
- [python-docx](https://python-docx.readthedocs.io/en/latest/) for Word docs

---

## 📄 License

MIT License.  
Feel free to use, modify, and build on this project!

---

## ✨ Future Improvements

- Add memory support  
- Web UI with Streamlit or Gradio  
- Add more tools (email, search, reminders, etc.)  
- Logging and analytics

---

## 👩‍💻 Author

Made with 💖 by [marse]  
GitHub: [github.com/novaivo](https://github.com/novaivo)
