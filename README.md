<br>

# Link Genie : Building social network with AI 👬

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fchaeyeon2367%2Fllm-app-LinkGenie&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

<br>

LinkGenie is a full-stack web application that leverages the power of Large Language Models (LLMs) to streamline LinkedIn outreach. It allows users to search for LinkedIn profiles by name and retrieve relevant information. LinkGenie then utilizes LLMs to personalize a "connection link" with the retrieved information, facilitating conversation starters. This allows users to initiate meaningful conversations with their desired connections.

<br>

![ScreenRecording2024-06-20at01 41 2622-ezgif com-video-to-gif-converter](https://github.com/chaeyeon2367/llm-app-DocumentationAssistant/assets/63314860/c7b9f621-9c6d-4dfe-a5c0-c30bcc1ce351)

<br>

## Key Features 💡

**1. LinkedIn Data Scraping**
  - Proxycurl API Integration: Efficiently scrapes LinkedIn data about a person, gathering valuable information for networking purposes.
    
**2. Advanced Search Capabilities**
  - Tavily API: Employed as a search API, providing high-quality, real-time knowledge optimized for RAG and LLMs.
    
**3. LangChain Integration**
  - Chains and Agents: Utilizes LangChain's chains and agents, including custom agents, to efficiently handle and process data.
  - Tools and Custom Tools: Implements both standard and custom tools within the application to enhance its functionality.
  - Output Parsers: Uses output parsers to format and display the retrieved information in a user-friendly manner.
    
**4. Flask API Integration**
  - Backend Development: Employs Flask API to build the backend of the application, ensuring smooth and efficient data handling and processing.

<br>

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`
<br>

`PROXYCURL_API_KEY`
<br>

`TAVILY_API_KEY` 
<br>

`LANGCHAIN_API_KEY` 
<br>

`LANGCHAIN_TRACING_V2=true` 
<br>

`LANGCHAIN_PROJECT=Link Genie` 
<br>

<br>

## Getting Started

1. Clone the repository to your local environnement
   
  ```
  git clone https://github.com/chaeyeon2367/llm-app-LinkGenie.git
  ```

2. Go to the project directory
   
  ```
  cd llm-app-LinkGenie
  ```

3. Install dependencies

  ```
  pipenv install
  ```

4. Start the flask server

  ```
  pipenv run app.py
  ```

<br>

## Running Tests

To run tests, run the following command

  ```
  pipenv run pytest .
  ```

<br>

## 🔗 Links 

<a href="https://www.linkedin.com/in/chaeyeonshim0930/" target="_blank"><img src="https://github.com/chaeyeon2367/llm-app-DocumentationAssistant/assets/63314860/1e8d7a85-e9da-4240-a318-143183d10fe8" width="40" height="40"></a>

<br>

## Resources

https://github.com/hwchase17/chat-langchain-readthedocs

https://github.com/emarco177/ice_breaker

