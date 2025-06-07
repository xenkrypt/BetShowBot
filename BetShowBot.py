from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

url = "http://localhost:11434"
llama_model = "Llama3.2:1b"
betshowbot_model = "BetShowBot"

llm_filter = ChatOllama(
    base_url=url,
    model=llama_model,
    temperature=0.5,
    num_predict=2000
)

llm_responder = ChatOllama(
    base_url=url,
    model=betshowbot_model,
    temperature=0.5,
    num_predict=2000
)

def filter(history, q):
    try:

        # context = "\n".join(history) + "\nUser query: " + q
        # prompt = f"Is the last message or context health-related or queries for the BetShow application (REPLY WITH LONY ONE WORD, TRUE OR FALSE in Uppercase)?: {context}"
        # response = llm_filter.invoke(prompt)
        # if "TRUE" in response.content:
        #     print(response.content)
        #     return True
        # print(response.content)
        # return False
        with open("keywordsB.txt", "r") as f:
            keywords = set(word.strip().lower() for word in f.readlines() if word.strip())

        quer = set(q.lower().split())
        if keywords & quer:
            return True
        return False
    except Exception as e:
        print(f"Error during filtering: {e}")
        return False

def responder(prompt):
    try:
        response = llm_responder.invoke(prompt)
        return response.content
    except Exception as e:
        return f"Error: {str(e)}"

def load_history():
    try:
        with open('history.txt', 'r') as file:
            history = file.readlines()
        return [line.strip() for line in history]
    except FileNotFoundError:
        return []

def append_to_history(content):
    with open('history.txt', 'a') as file:
        file.write(content + '\n')

def caller():
    print("Welcome to BetshowBot! How can I assist you today?")
    history = load_history()

    while True:
        inp = input("User: ")
        if inp == "/break":
            break
        append_to_history(f"User: {inp}")

        if filter(history, inp):
            print("BetShowBot: This query is related to healthcare.")
            response = responder("For this given query respond with the available solutions or facts and give assistance :" + inp)
            append_to_history("BetShowBot: This query does seem to be healthcare-related.")
        else:
            response = responder("For this given unrelated query do not respond with unnecessary facts or solutions for non related questions, just politely respond that you cannot help with unrelated queries:" + inp)      
            print("BetShowBot: This query does not seem to be healthcare-related.")
            append_to_history("BetShowBot: This query does not seem to be healthcare-related.")
            
        append_to_history(f"BetShowBot: {response}")
        print("BetShowBot Response:", response)

if __name__ == "__main__":
    caller()
