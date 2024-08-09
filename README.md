# Gemma2 Chatbot Web App

This project is a web-based chatbot built using the Ollama Gemma2 model, running offline. The chatbot is designed to respond to user queries through a simple and interactive web interface.

## Features
- Utilizes the Ollama Gemma2 model for generating responses offline.
- Built with Streamlit for an easy-to-use web interface.
- Simple and modular codebase for easy customization.
- Can be deployed locally.

## Requirements

Make sure you have Python 3.8+, Ollama, and Streamlit installed.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repo/gemma2-chatbot.git
    cd gemma2-chatbot
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Gemma2 model:**
    Download and run the Gemma2 model using Ollama:
    ```bash
    ollama run gemma2:27b
    ```

4. **Run the Streamlit web app:**
    In a separate terminal, execute:
    ```bash
    streamlit run app.py
    ```

## Usage

Open your web browser and navigate to `http://localhost:8501` to interact with the chatbot.

## Customization

You can modify the chatbot by editing the `app.py` file. For example, you can change the model parameters, add new functionalities, or integrate the chatbot with other APIs.

## Troubleshooting

If you encounter any issues, ensure that all dependencies are installed correctly and that the Ollama Gemma2 model is running in the background.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
