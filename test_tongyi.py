import json
import os
import random
# import openai
import time

# from dotenv import load_dotenv, find_dotenv
# from litellm import completion
# from gpt4all import GPT4All, Embed4All
from langchain_community.llms import Tongyi

# from reverie.backend_server.persona.prompt_template.gpt_structure import temp_sleep
# from reverie.backend_server.utils import *

# openai.api_key = random.choice(openai_api_key)
# os.environ["http_proxy"] = "http://127.0.0.1:7890"
# os.environ["https_proxy"] = "https://127.0.0.1:7890"



import json

with open("./reverie/config.json","r") as fp:
    settings = json.load(fp)
    os.environ["DASHSCOPE_API_KEY"] = settings["DASHSCOPE_API_KEY"]  

def Tongyi_request(messages: object) -> object:
    """
      Given a prompt and a dictionary of GPT parameters, make a request to OpenAI
      server and returns the response.
      ARGS:
        prompts: a str prompt
        gpt_parameter: a python dictionary with the keys indicating the names of
                       the parameter and the values indicating the parameter
                       values.
      RETURNS:
        a str of Tongyi's response.
    """
    time.sleep(1)

    try:
        # llm call
        llm = Tongyi()
        llm.model_name = 'qwen-max'
        response = llm.invoke(messages)

        return response
    except Exception as e:
        return f"TongYi ERROR:{e}"
    

prompt = """
---
角色1: 阿牛作为小卖部的老板，平时会在自己的小卖部营业，进行工作比如收拾货架、进货、喝健力宝，
休息时会观看电视节目。他每天都会在小卖部里向其他居民出售零食和日常用品。

角色2: 龙哥是一个游手好闲的居民，偶尔会来小卖部吃东西，他最喜欢的零食是辣条和三鲜伊面。
阿牛会帮他把面泡好再吃。有时龙哥会去公园和学校闲逛。

历史行为: 
2个小时前，阿牛在打扫小卖部的卫生，并做了中午饭。
2分钟前龙哥来到阿牛的小卖部，他购买了一包辣条并和阿牛交流了关于小璐的故事，以及胖哥最近的行踪。

当前行为: 
阿牛吃完了泡面，打开了一包辣条并在电视机上进行游戏机的游玩。此时龙哥与他进行了聊天。
当前位置: 
阿牛的小卖部

(阿牛此时的想法: 胖哥不在，可以把藏了好久的火腿肠拿出来吃了。阿牛也很关心小璐最近的生活，想要知道她最近的生活。) 
(龙哥此时的想法: 家里的存货快没了，他必须要去村口超市购买一些。等下班后龙哥需要到小卖部买一包烟。) 

下面是他们的对话: 

阿牛:  "
---
以json格式输出以上提示词（prompt）的对应结果。输出结果必须以两重嵌套列表的格式，列表格式为: 
 [["<角色1>", "<对话>"],["<角色2>", "<对话>"] ...]
 
如果对话较长，可以输出多段对话，直到他们间的对话自然结束。

注意，你必须用同样的语言生成结果，尽量使用日常表达，将结果翻译成汉语交流中常用的东北腔。

这里是一个输出结果的json例子: 
{"output": "[["龙哥", "阿牛你帮我去泡个三鲜伊面"], ["阿牛", "行，等会啊"] ... ]"}
"""


# 大模型表现有时不稳定，乱序或乱码等问题目前还在想办法解决
def test():
    print(f"""localmodel result: {Tongyi_request(prompt)}""")


if __name__ == "__main__":
    test()
