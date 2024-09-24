import os 
from openai import AzureOpenAI
import numpy as np   
from dotenv import load_dotenv 

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("openai_api_endpoint"),
    azure_deployment=os.getenv("openai_completions_deployment"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY2"),
    api_version=os.getenv("openai_api_version")
)

model = os.environ['AZURE_OPENAI_DEPLOYMENT']

# Create your first prompt
prompt = "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something that current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance, sometimes even reaching competitiveness with prior state-of-the-art fine-tuning approaches.\n\ntl;dr"
print(prompt)

response = client.chat.completions.create(
  model=model,
  messages = [{"role":"system", "content":"You are a helpful assistant."},
               {"role":"user","content":prompt},])

print(response.choices[0].message.content)