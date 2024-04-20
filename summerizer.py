from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
)


youtube_url = input("Enter the Youtube URL you want to interact with!! ")
def get_youtube_transcript(url):
    loader = YoutubeLoader.from_youtube_url(url)
    documents = loader.load()
    return documents[0]

# documents = get_youtube_transcript(youtube_url)
# transcript_text = documents[0]

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
)

def asking_question():
    while True:
        interact = input("What you want to know about the video?")
        if interact != 'q':
            response = llm.invoke(f"{interact} : {get_youtube_transcript(url=youtube_url)}")
            print(response.content)
        else:
            return None
asking_question()