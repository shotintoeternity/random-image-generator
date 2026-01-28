# Random Image Generator

A Streamlit app that generates truly random photorealistic images using Google's Nano Banana (Gemini 2.5 Flash Image) API. Each click produces a completely unique image across a wide range of photography categories — portraits, architecture, wildlife, food, street photography, and beyond.

## Live Demo

[random-image-generator.streamlit.app](https://random-image-generator.streamlit.app)

## Setup

1. Get a Google AI API key from [ai.google.dev](https://ai.google.dev)
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your API key and run:
   ```
   export GOOGLE_API_KEY="your-key-here"
   streamlit run app.py
   ```

## Streamlit Cloud Deployment

Add this to your Streamlit Cloud secrets (Advanced settings):

```toml
GOOGLE_API_KEY = "your-key-here"
```
