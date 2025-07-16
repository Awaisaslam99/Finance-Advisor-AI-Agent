# 💹 FinVisor AI Agent

An intelligent financial research and market analysis agent built using **Phi Agents**, **Groq LLM**, **YFinance**, and **DuckDuckGo**. This modular AI assistant can summarize analyst recommendations, retrieve real-time stock fundamentals, and gather the latest company news — enhanced with web search capabilities. Built with a clean MVC architecture for clarity and scalability.

---

## 🚀 Features

- 🧠 Uses **Groq LLM (LLaMA3)** for ultra-fast, accurate responses
- 💼 Summarizes analyst recommendations and financial fundamentals
- 📊 Retrieves stock prices, ratios, company news, and insights
- 🌐 Augments with real-time web search using DuckDuckGo
- ⚙️ Modular architecture (MVC) for easy expansion
- 🧪 Supports CLI or interactive playground UI

---

## 🧠 Tech Stack

| Layer         | Tool / Framework              |
|---------------|-------------------------------|
| LLM           | Groq LLaMA 3 (70B)             |
| Agent Engine  | [Phi Agents](https://github.com/phidatahq/phi) |
| Financial Data| YFinanceTools (Yahoo Finance) |
| Web Context   | DuckDuckGo Tool               |
| Environment   | Python + dotenv               |

---

## 🧭 Project Structure

finvisor-ai-agent/
├── app.py # CLI agent interface
├── playground.py # Interactive playground app
├── controller/
│ └── agent_controller.py # Agent team initializer
├── model/
│ └── models.py # Groq + tools config
├── .env # API keys
├── requirements.txt # Dependencies
└── README.md # You are here

---

## ⚙️ Setup & Run

### 1. Clone the Repo

```bash
git clone https://github.com/Awaisaslam99/finvisor-ai-agent.git
cd finvisor-ai-agent


Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

Create .env file
env
Copy
Edit
OPENAI_API_KEY=your_openai_key
PHI_API_KEY=your_phi_api_key

▶️ Run the Agent (CLI)
bash
Copy
Edit
python app.py


📄 License
MIT License — Free for personal and professional use.

🙋 Author
Made with 💸 by Awais Aslam
