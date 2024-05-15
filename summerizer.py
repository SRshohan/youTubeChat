import os
from dotenv import load_dotenv
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


def load_llm(user_input):
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        },
    )
    return llm.invoke(user_input)


def youtube_transcript(url):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
    load = loader.load()
    doc = load[0]
    transcript = doc.page_content
    with open("storing_transcript.txt", "w") as file:
        file.write(transcript)


def delete_data():
    open("storing_transcript.txt", "w").close()


if __name__ == '__main__':
    # content = load_llm().invoke(" Write me a peom")
    # print(content.content)
    youtube_transcript('https://www.youtube.com/watch?v=0IAPZzGSbME&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O')
    delete_data()
