
# Langchain app
 Building a chatbot with Langchain.
Langchain is a framework for building llm Application 

For a Langhchain Chains, there are three components:
LLMs, Prompts,Output Parsers.

I will use any llm for the backend, since langchain support any  variety of llm 

also groq model because it is free


## Author

- [@EmmanuelAwogbindin](https://www.linkedin.com/in/emmanuel-awogbindin-42174321b/)


## Installation

👨‍⚖️Install libraries

```bash
##create New Python Environment##
    1. python -m venv venv

## install all Required libraries and packages##
    2. pip install -r requirement.txt
```
    
![Logo](https://av-eks-lekhak.s3.amazonaws.com/media/__sized__/article_images/5_83DdPYD-thumbnail_webp-600x300.webp)

I can use any llm for the backend, since langchain support any  variety of llm 

also groq model because it is free

*Prompt is the first step in the chain, it takes dictionary of parameters and returns a string. In this case we are using `ChatPromptTemplate` to create custom prompt template. It takes tuples, where the first element is the role of themessage and the second element is the content of the message.

role can be `system`,`User`,`assistant`or `placeholder`    

*Chain: the chain takes the `prompt` and the  `llm ` and  `outputParser` and the  `response`. This is the most basic since we have a variable in the prompt that will be filled by the user and then the llm. In langchain every chain has the  function called `invoke` that takes dictionary of variables and returns its response

*outputParser
outputParser is used to parse the AI message in a `readable` format using the `StrOutputParser`.
## API Reference

#### Get all API keys

```http    
  Langchain settings Page
  Grok Console
```
Links to get them

[Langchain API key](Smith.langchain.com/settings)

[groq console API key](console.groq.com/docs/models)

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

if you are setting it directly

`os.environ['LANGCHAIN_API_KEY']=<your_api_key>`

`os.environ['LANGCHAIN_TRACING_V2']=true`

`os.environ['LANGCHAIN_PROJECT']=<your_project_name>`

if you are using .env file (this's what i use):

`LANGCHAIN_API_KEY=<your_api_key>`

`LANGCHAIN_TRACING_V2=true`

`LANGCHAIN_PROJECT="BID-Chat"`

`GROQ_API_KEY=<your_api_key>`
## Feedback

If you have setup all the libraries and the environment, yo can head over to [langchain smith project](smith.langchain.com/project), to see how the chain is performing 

## Deployment

To deploy this project run

```bash
  streamlit run streamlit/app.py
```

