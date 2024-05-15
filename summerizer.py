import os
from dotenv import load_dotenv
from langchain.schema import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

password = os.getenv('ENV', 'local')
dotenv = f".env.{password}"
load_dotenv(dotenv_path=dotenv)


def load_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    return llm


def youtube_transcript(url):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
    load = loader.load()
    document = {load[0]}
    transcript = document["page_content"]
    print(transcript)


if __name__ == '__main__':
    # content = load_llm().invoke(" Write me a peom")
    # print(content.content)
    youtube_transcript('https://www.youtube.com/watch?v=0IAPZzGSbME&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O')