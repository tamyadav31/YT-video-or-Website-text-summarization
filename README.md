# YT-video-or-Website-text-summarization

## Overview

**YT-video-or-Website-text-summarization** is an automatic summarization tool that uses advanced natural language models to generate concise summaries from YouTube videos or any web page. Users provide a URL, and the application intelligently scrapes the content or fetches video transcripts, then produces a clear, 300-word summary using a state-of-the-art large language model, all through a user-friendly Streamlit interface.

---

## Features

- **YouTube Support:** Extracts and summarizes both video transcripts and descriptions, with multiple fallback mechanisms if the transcript is unavailable.
- **Webpage Summarization:** Scrapes, loads, and summarizes text from any accessible URL.
- **LLM-Powered Summaries:** Utilizes Groq's `Gemma-7b-It` model (via Langchain) to produce human-readable, accurate summaries.
- **Streamlit App:** Clean, interactive frontend for one-click summarization.
- **Robust Input Handling:** Thorough validation for API keys and URLs, including error management and user feedback.
- **Fallback & Robustness:** Falls back gracefully to multiple data extraction methods if the primary fails.

---

## Technology Stack

- **Python 3.x**
- [LangChain](https://github.com/langchain-ai/langchain) & [LangChain-Groq](https://github.com/langchain-ai/langchain)
- **Groq LLMs** (`Gemma-7b-It`)
- **Streamlit** (UI)
- **YoutubeTranscriptAPI**, **PyTube** (YouTube data extraction)
- **UnstructuredURLLoader** (Web scraping)
- **python-dotenv** (Environment variables)

---

## Installation

1. **Clone the repository**
git clone https://github.com/tamyadav31/YT-video-or-Website-text-summarization.git
cd YT-video-or-Website-text-summarization

text

2. **Create and activate a virtual environment**
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

text

3. **Install dependencies**
pip install -r requirements.txt

text

4. **Set up your Groq API key**
- Obtain your GROQ API key.
- You can provide it in the sidebar at runtime or add it to a `.env`:
  ```
  GROQ_API_KEY=your_groq_api_key
  ```

---

## Usage

1. **Start the Streamlit app**
streamlit run app.py

text

2. **In the app:**
- Enter your *GROQ API key* in the sidebar.
- Enter the URL of a YouTube video or any public website.
- Click **Summarize Content from YouTube or Website**.
- View your 300-word, LLM-generated summary instantly.

---

## Code Structure

| File        | Description                                                         |
|-------------|---------------------------------------------------------------------|
| `app.py`    | Main Streamlit application. Handles URLs, data loading, LLM, output |
| `requirements.txt` | List of required Python dependencies                        |
| `README.md` | (This document)                                                     |

---

## Acknowledgements

- [LangChain](https://www.langchain.com/)
- [Groq](https://www.groq.com/)
- [PyTube](https://pytube.io/en/latest/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)

---

## License

Distributed under the MIT License.

---

_Build by automating comprehension: summarize any YouTube or website content, instantly._
