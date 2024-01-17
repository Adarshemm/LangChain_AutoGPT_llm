Overview
This repository contains a Streamlit web application leveraging LangChain, OpenAI, and Wikipedia to generate responses to user queries. The application features prompt templates, memory management, and chains of large language models (LLMs) to facilitate detailed conversations and script generation.

Installation
Ensure you have the necessary dependencies installed. Run the following command:

bash
Copy code
pip install streamlit langchain openai wikipedia chromadb tiktoken
Setup
Obtain an API key from OpenAI and store it in the API_Key.py file.
Install the required packages.
Run the Streamlit app:
bash
Copy code
streamlit run LangChain_AutoGPT_llm.py
Usage
Launch the Streamlit app using the provided command.
The app's UI will prompt you to ask a question.
Enter a query, and LangChain will generate a response, leveraging prompt templates and memory.
Components
Prompt Templates
The app utilizes prompt templates for structured interactions. Two templates, title_template and script_template, allow users to request information or scripts on a specified topic.

Memory Management
ConversationBufferMemory manages the chat history for specific topics. This ensures continuity and context-aware responses.

Large Language Models (LLMs)
LangChain employs OpenAI's large language model with adjustable temperature for generating diverse and contextually relevant responses.

Chains
The app features different chains for handling various stages of interaction. title_chain generates titles based on user queries, while script_chain generates detailed scripts.

Examples
Asking for Title:

User Prompt: "What is artificial intelligence?"
LangChain Response: "Artificial Intelligence - The science of training machines to perform tasks that typically require human intelligence."
Generating Script:

User Prompt: "Write me a script on Artificial Intelligence."
LangChain Response: A script on Artificial Intelligence, leveraging information from Wikipedia.
Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or fix any issues.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy using LangChain GPT Test App! If you have any questions or feedback, feel free to reach out.
P.S Thanks to Nicholas Renotte for this crash course