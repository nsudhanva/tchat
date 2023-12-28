# LangChain Text File Chat

## Overview

This repository showcases a Python-based chat application using LangChain, a library for building applications with language models. It emphasizes creating a conversational interface using OpenAI's language models, focusing on conversation history and dynamic prompting.

## Key Features

- **Language Model Interaction**: Uses `ChatOpenAI` for engaging with OpenAI's language models.
- **Conversation Tracking**: Employs `ConversationSummaryMemory` to keep track of conversation history.
- **Responsive Prompts**: Utilizes `ChatPromptTemplate` and `HumanMessagePromptTemplate` for dynamic and context-aware prompt generation.
- **Configuration Management**: Manages settings via `dotenv`, facilitating environment variable handling.

## How It Works

1. **Setup**: Initializes with necessary environment variables.
2. **Model Configuration**: Prepares the OpenAI chat model with detailed output options.
3. **Memory Initialization**: Sets up a system to store and recall conversation histories.
4. **Prompt Handling**: Configures prompts to dynamically incorporate previous dialogues and new inputs.
5. **Chat Interface**: Runs an interactive loop, processing user inputs and generating contextually relevant responses.

## Repository Structure

- `LICENSE`: License agreement for the repository.
- `README.md`: Descriptive documentation of the project.
- `facts`: Directory containing the main components for the chat application.
  - `emb`: Subdirectory for Chroma's binary and SQLite3 data files.
  - `facts.txt`: Text file serving as the primary data source for document processing.
  - `main.py`: Script for initializing and querying the Chroma database.
  - `prompt.py`: Script for executing the question-answering chain.
  - `redundant_filter_retriever.py`: Script for filtering redundant information from retrieved results.
- `main.py`: Main script for running the chat application.


## Usage Instructions

1. **Install Dependencies**: Set up Python and required libraries (`dotenv`, `langchain`).
2. **Clone the Repository**: Download the repository to your machine.
3. **Configure Environment**: Create and configure a `.env` file with necessary settings.
4. **Run the Application**: Execute `main.py` to start the chat application.
5. **Engage with the Chatbot**: Interact with the chatbot, which uses past interactions for context-aware responses.

### For Chroma Embeddings

- **Document Handling**: Process and segment the `facts.txt` document.
- **Database Creation**: Build a Chroma database from segmented documents.
- **Information Retrieval**: Utilize the database for similarity searches related to queries.
- **Query Handling**: Use `prompt.py` to ask questions and receive answers based on `facts.txt`.

### Applications

- Suitable for advanced chatbots and conversational agents needing memory and contextual understanding.
- Ideal for information retrieval from extensive text files, enhancing FAQ systems, knowledge bases, and educational tools. 

This streamlined approach, combining LangChain and Chroma, offers efficient, context-aware, and sophisticated conversational experiences and data retrieval.