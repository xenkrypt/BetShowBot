# BetShow Bot - An Ollama based Chatbot for medical queries and appointment management

## Overview

BetShowBot is a simple command-line chatbot built using **LangChain** and **Ollama**. It uses two language models to filter user queries and generate responses based on whether the query is related to a predefined domain (such as healthcare or BetShow application support).

The chatbot maintains a conversation history and uses keyword-based filtering to determine if a user's query should be answered or politely declined.

## Features

* **Keyword-Based Query Filtering**

  * Loads keywords from a text file (`keywordsB.txt`).
  * Checks whether the user's query contains any relevant keywords.
  * Classifies queries as related or unrelated to the supported domain.

* **AI-Powered Responses**

  * Uses an Ollama-hosted language model to generate responses.
  * Provides helpful answers for relevant queries.
  * Politely refuses unrelated questions.

* **Conversation History**

  * Stores user interactions in `history.txt`.
  * Loads previous conversation history when the application starts.

* **Local LLM Integration**

  * Connects to locally hosted Ollama models.
  * Uses:

    * `Llama3.2:1b` for filtering (optional implementation).
    * `BetShowBot` for generating responses.

## Project Structure

```text
project/
│
├── main.py            # Main chatbot application
├── keywordsB.txt      # List of domain-specific keywords
├── history.txt        # Stores conversation history
├── .env               # Environment variables
└── requirements.txt   # Project dependencies
```

## Workflow

1. User enters a query.
2. The query is checked against keywords from `keywordsB.txt`.
3. If the query is relevant:

   * The chatbot generates an informative response using the BetShowBot model.
4. If the query is unrelated:

   * The chatbot politely informs the user that it cannot assist with the request.
5. The conversation is stored in the history file.

## Technologies Used

* Python
* LangChain
* Ollama
* Llama 3.2
* Dotenv

## Future Improvements

* Replace keyword matching with AI-based intent classification.
* Utilize conversation history for contextual responses.
* Add support for multiple domains.
* Store chat history in a database instead of text files.
* Build a web interface using Flask, FastAPI, or Streamlit.

## Purpose

The goal of BetShowBot is to provide a lightweight, domain-specific AI assistant that can answer relevant user queries while filtering out unrelated requests, ensuring focused and accurate assistance.
