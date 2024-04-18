from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import YoutubeLoader
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

load_dotenv()

youtube_url = input("Enter the Youtube URL you want to interact with!! ")
print("Working")
def get_youtube_transcript(url):
    loader = YoutubeLoader.from_youtube_url(url)
    documents = loader.load()
    return documents

documents = get_youtube_transcript(youtube_url)
transcript_text = documents[0]

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
            response = llm.invoke(f"{interact} : {transcript_text}")
            print(response.content)
        else:
            return None
asking_question()