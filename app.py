import os
import streamlit as st
from google import genai
from google.genai import types

try:
    API_KEY = st.secrets["GOOGLE_API_KEY"]
except (KeyError, FileNotFoundError):
    API_KEY = os.environ.get("GOOGLE_API_KEY", "")

PROMPT = (
    "You are a random photograph generator. First, think of a random category of photography — "
    "for example portrait, street, food, architecture, sports action, macro, aerial, underwater, "
    "wildlife, landscape, nightlife, fashion, photojournalism, still life, interior design, "
    "industrial, vintage, weather, astronomy, automotive, concert, wedding, travel documentary, "
    "abstract texture — but do NOT limit yourself to these. Come up with any kind of real-world "
    "photograph that could exist. Then generate a single photorealistic image in that category. "
    "It must look indistinguishable from a real photograph. Be creative and specific — avoid "
    "generic or cliché compositions. Every image should be completely different from the last."
)


def generate_image():
    client = genai.Client(api_key=API_KEY)
    response = client.models.generate_content(
        model="gemini-2.5-flash-image",
        contents=[PROMPT],
        config=types.GenerateContentConfig(
            response_modalities=["TEXT", "IMAGE"],
        ),
    )
    for part in response.parts:
        if part.inline_data is not None:
            return part.inline_data.data, part.inline_data.mime_type
    return None, None


# --- UI ---

st.set_page_config(page_title="Random Image Generator", layout="centered")

st.markdown(
    """
    <style>
    .stApp { max-width: 800px; margin: 0 auto; }
    div[data-testid="stImage"] img {
        border-radius: 12px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.18);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Random Image Generator")
st.caption("Powered by Nano Banana (Gemini 2.5 Flash Image)")

if not API_KEY:
    st.warning("Set the `GOOGLE_API_KEY` environment variable to use this app.")
    st.stop()

if st.button("Generate Random Image", type="primary", use_container_width=True):
    with st.spinner("Generating image..."):
        try:
            image_data, mime_type = generate_image()
            if image_data:
                st.image(image_data, use_container_width=True)
                ext = "png" if "png" in (mime_type or "") else "jpg"
                st.download_button(
                    label="Download Image",
                    data=image_data,
                    file_name=f"random_image.{ext}",
                    mime=mime_type or "image/png",
                    use_container_width=True,
                )
            else:
                st.error("No image was returned. Try again.")
        except Exception as e:
            st.error(f"Error: {e}")
