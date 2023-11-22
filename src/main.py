import os

from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (HumanMessagePromptTemplate, ChatPromptTemplate)

load_dotenv()

OPEN_API_KEY = os.environ.get("OPENAI_API_KEY")

PROMPT_COUNTRY_INFO = """
    Provide information about {country}.
    """

def main():
    chat_model = ChatOpenAI(openai_api_key=OPEN_API_KEY)

    # get user input
    country = input("Enter the name of a country: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(country = country)

    response = chat_model(chat_prompt_with_values.to_messages())
    print(response)

if __name__ == "__main__":
    main()