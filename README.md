# LangChain Chat Application Repository

## Overview

This repository features a Python-based chat application utilizing LangChain, a library for building language model applications. The focus is on creating a conversational interface using OpenAI's language models, with a special emphasis on incorporating conversation history and dynamic prompting.

### Features

- **OpenAI Chat Model**: Leverages `ChatOpenAI` for language model interactions.
- **Conversation Memory**: Implements `ConversationSummaryMemory` to maintain a history of the conversation.
- **Dynamic Prompting**: Uses `ChatPromptTemplate` and `HumanMessagePromptTemplate` for creating responsive and context-aware prompts.
- **Environment Variable Management**: Utilizes `dotenv` for loading environment configurations.

### How It Works

1. **Environment Setup**: Loads necessary environment variables.
2. **Chat Model Initialization**: Sets up the OpenAI chat model with verbose output.
3. **Memory Management**: Initializes conversation memory to store and recall past messages.
4. **Prompt Configuration**: Configures dynamic prompts to include previous messages and current input.
5. **Interactive Chat Loop**: Continuously accepts user input and generates responses based on the conversation context.

### File Structure

- `.env`: Environment configuration file (not included in the repository, to be created by the user).
- Python scripts: Contains the main script with the above-mentioned components.

### How to Use

1. **Install Dependencies**: Ensure Python and necessary libraries (`dotenv`, `langchain`) are installed.
2. **Clone Repository**: Download this repository to your local environment.
3. **Environment Setup**: Create a `.env` file with required configurations (e.g., API keys).
4. **Run the Script**: Execute the main Python script to start the interactive chat application.
5. **Interact with the Chatbot**: Engage in a conversation, with the application dynamically using past interactions to inform responses.

## Chat With Your Text File with Chroma Embeddings

### Overview

This repository contains a Python-based project utilizing LangChain, a library for building language model applications, and Chroma, a vector storage system. The primary focus of this repository is to leverage natural language processing (NLP) and machine learning techniques for document retrieval and question answering based on the contents of a text file (`facts.txt`).

### Features

- **Document Loading and Processing**: Utilizes `TextLoader` for loading documents and `CharacterTextSplitter` for segmenting text.
- **Embedding Generation**: Employs `OpenAIEmbeddings` to create embeddings from text.
- **Chroma Vector Store**: Uses Chroma for storing and retrieving document embeddings.
- **Question-Answering and Retrieval**: Implements retrieval-based question answering using LangChain's `RetrievalQA` and `ChatOpenAI` models.

### File Structure

- `emb`: Directory containing Chroma's binary and SQLite3 data files.
- `facts.txt`: The source text file for document loading and processing.
- `main.py`: Python script for initializing and querying the Chroma database.
- `prompt.py`: Python script for executing the question-answering chain.

### How It Works

#### main.py

1. **Initialization**: Loads environment variables and initializes embeddings and text splitter.
2. **Document Loading**: Loads and splits the `facts.txt` document.
3. **Chroma Database Creation**: Creates a Chroma database from the processed documents.
4. **Similarity Search**: Performs similarity searches in the database to find relevant information to a query.

#### prompt.py

1. **Chat Model Initialization**: Sets up the ChatOpenAI model.
2. **Chroma Database Integration**: Integrates Chroma as a retriever.
3. **RetrievalQA Chain**: Creates a `RetrievalQA` chain combining the chat model and Chroma retriever.
4. **Execution**: Runs the chain to answer queries based on the text data.

### How to Use

1. **Prepare Environment**: Ensure Python and necessary libraries (`dotenv`, `langchain`) are installed.
2. **Clone Repository**: Clone this repository to your local machine.
3. **Load Data**: Place your desired text file as `facts.txt` in the root directory.
4. **Run main.py**: Execute `main.py` to create and populate the Chroma database.
5. **Query Using prompt.py**: Run `prompt.py` to ask questions and get answers based on the text data.

### Applications

- This setup is ideal for developing advanced chatbots and conversational agents that require memory and context understanding. It's particularly suited for applications such as customer service bots, interactive learning tools, and personal assistants. The integration of LangChain with OpenAI's models ensures a sophisticated and human-like conversational experience.
- This setup is ideal for applications requiring efficient retrieval and processing of information from large text files, such as knowledge bases, FAQ systems, and educational tools. The integration of LangChain and Chroma allows for quick and accurate retrieval of information, making it a powerful tool for developers and researchers in the field of NLP and AI.