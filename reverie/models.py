"""
allow different model API
"""

# from litellm import completion
from langchain_community.llms import Tongyi
import os
import json

## set ENV variables
# os.environ["OPENAI_API_KEY"] = "openai key"
# os.environ["COHERE_API_KEY"] = "cohere key"
# os.environ["ANTHROPIC_API_KEY"] = "anthropic key"



with open("./reverie/config.json","r") as fp:
    settings = json.load(fp)
    os.environ["DASHSCOPE_API_KEY"] = settings["DASHSCOPE_API_KEY"]

messages = [{"content": "Hello, how are you?", "role": "user"}]

# # openai call
# response = completion(model="gpt-3.5-turbo", messages=messages)

# # cohere call
# response = completion(model="command-nightly", messages=messages)

# # anthropic
# response = completion(model="claude-2", messages=messages)

# # Tongyi 
llm = Tongyi()
llm.model_name = 'qwen-max'
response = llm.invoke(messages)