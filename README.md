# MCQ-Creator-App

## Overview

This repository contains a Python script for creating multiple-choice questions (MCQs) from a given text. The script uses a combination of natural language processing and machine learning techniques to process documents, extract relevant information, and generate questions with options and answers.
Features
- Document Loading: Load PDF documents from a specified directory.
- Document Splitting: Split documents into smaller chunks for easier processing.
- Embedding Generation: Generate embeddings for queries using Sentence Transformer models.
- Indexing with Pinecone: Create and use a Pinecone index for document similarity search.
- Question Answering: Leverage a pre-trained language model for answering questions based on the documents.
- MCQ Generation: Generate multiple-choice questions from the text using OpenAI's GPT model.

## Requirements
- Python 3.x
- PyPDF2
- Sentence Transformers
- Pinecone
- LangChain
- OpenAI GPT
- Regular Expressions (re)
- JSON

## Installation

Before running the script, ensure you have all the required packages installed. You can install them using pip:

```
pip install PyPDF2 sentence-transformers pinecone-client langchain openai
```


## Usage
- Load Documents: Place your PDF documents in a directory and specify the directory path in the script.
-  Run the Script: Execute the script to process the documents and generate MCQs.
-  MCQ Output: The script will output the generated MCQs in a structured format.

## Configuration

- Set your Pinecone API key in the script.
- You may need to adjust the chunk size and overlap for document splitting based on your document's size and complexity.
- The Sentence Transformer model can be changed as per your requirement.

## Example
```
directory = '.'
documents = load_docs(directory)
docs = split_docs(documents)

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
query_result = embeddings.embed_query("Hello Buddy")

pinecone.init(api_key='YOUR_API_KEY', environment="gcp-starter")
index_name = "mcq-creator"
index = Pinecone.from_documents(docs, embeddings, index_name=index_name)

answer = get_answer("How is India's economy?")
```



