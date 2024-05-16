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
    
    return transcript


def delete_data():
    f = open("storing_transcript.txt", "w")
    f.close()

def reading_doc():
    f = open("storing_transcript.txt", "r")
    return f.read()

def storing_data(llm_AI_message):
    llm_AI_message = str(llm_AI_message)
    f = open("storing_transcript.txt", "w")

    content_start = llm_AI_message.find("content=' ") + len("content=' ")
    content_end = llm_AI_message.find("' response_metadata")
    content = llm_AI_message[content_start:content_end]

    return f.write(content)



if __name__ == '__main__':
    questions = input("Enter what you want to know about the video: ")
    transcript = youtube_transcript('https://www.youtube.com/watch?v=0IAPZzGSbME&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O')
    reading_data = reading_doc()
    user_input = f"{questions} {reading_data}"
    llm = load_llm(user_input=user_input)
    storing_data(llm)
    print(llm)
    # content = load_llm().invoke(" Write me a peom")
    # print(content.content)
    
    
