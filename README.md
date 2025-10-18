# Gemma2 Chatbot Web App


# 🤖 Gemma2 Chatbot Web App (Offline LLM using Ollama)

This is a simple and powerful **AI chatbot web application** built using the **Gemma2 model** from **Ollama** and **Streamlit** for the frontend. The chatbot runs **completely offline** (no API required) and generates responses locally.

---

## ✅ Features

- 🚀 Uses **Gemma2 27B** model through **Ollama**
- 🖥️ Built with **Streamlit** for clean UI
- ⚡ Runs **offline** – no API keys or internet required
- 🧩 Easy to customize and extend
- 💻 Local system deployment

---

## 📦 Requirements

| Dependency       | Version          |
|------------------|------------------|
| Python           | 3.8+             |
| Ollama           | Latest           |
| Streamlit        | Latest           |
| Gemma2 model     | gemma2:27b       |

---

## 🔧 Installation

### Clone this repository
```bash
1. git clone https://github.com/chethanbits/Gemma2-Chatbot-Web-App.git
cd Gemma2-Chatbot-Web-App

2. Install Python dependencies
pip install -r requirements.txt

3. Install and run Ollama
   Download Ollama from https://ollama.ai  and install it.
   Then pull the Gemma2 model:  ollama pull gemma2:27b
   Start the model: ollama run gemma2:27b

4. Run the Streamlit app
   Open a second terminal in the project directory and run:
   streamlit run app.py
   Open your browser at http://localhost:8501
   to use the chatbot.

🛠️ Project Structure
Gemma2-Chatbot-Web-App/
│── app.py                # Streamlit UI
│── requirements.txt      # Dependencies
│── README.md             # Documentation

🧩 Customization
   Change AI behavior inside app.py
   Modify prompt or chat memory
   Replace model name to other Ollama-supported LLMs
   Add extra features like voice input, history, or authentication

❗ Troubleshooting
Problem	Solution
    ModuleNotFoundError         	Run pip install -r requirements.txt
    Ollama not running	          Start it manually from terminal
    Model not found             	Run ollama pull gemma2:27b
    Streamlit not opening	       Visit http://localhost:8501 manually

📜 License
    This project is licensed under the MIT License — feel free to modify and use it.

⭐ Support
    If you like this project, give it a star ⭐ on GitHub!
    Made with ❤️ using Gemma2 + Ollama + Streamlit
