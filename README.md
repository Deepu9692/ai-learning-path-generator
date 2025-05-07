# 🧠 AI Learning Path Generator

This is an AI-powered Streamlit app that generates personalized weekly study plans based on your goals using GPT-4 and recommends learning resources using SerpAPI.

## 🚀 Features
- Personalized AI-generated learning plans
- Customizable by skill level and time commitment
- Web search integration for up-to-date learning resources

---

## 🛠️ Setup Instructions (Local)

### 1. Clone or Download
```bash
git clone https://github.com/your-username/ai-learning-path-generator.git
cd ai-learning-path-generator
```

Or just unzip the provided zip file and navigate into it.

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API Keys
Create a `.env` file and add:
```
OPENAI_API_KEY=your_openai_key
SERPAPI_API_KEY=your_serpapi_key
```

### 5. Run the App
```bash
streamlit run app.py
```

---

## 🌐 Deployment Instructions (Streamlit Cloud)

1. Push code to a GitHub repository.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click “New App”
4. Connect your repo and select `app.py` as the main file.
5. Set Secrets:
```
OPENAI_API_KEY = "your_openai_key"
SERPAPI_API_KEY = "your_serpapi_key"
```
6. Click **Deploy**.

Your app will be live in a few minutes 🎉

---

## 📄 Requirements
- Python 3.8+
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- [SerpAPI Key](https://serpapi.com/)

---

## 🤖 Tech Stack
- GPT-4 (OpenAI)
- SerpAPI (Google Search API)
- Streamlit (Web App Framework)
- Python + dotenv

---

<<<<<<< HEAD
## 🧑‍💻 Made with 💡 by [Your Name]
=======
## 🧑‍💻 Made with 💡 by [L.Deepak Reddy]
>>>>>>> ff9081ec37034b3eab735f75df3e16764bfda674
