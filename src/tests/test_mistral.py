import os
from dotenv import load_dotenv
from mistralai import Mistral

# -----------------------------------------------------------------------
#                               SETUP
# -----------------------------------------------------------------------
load_dotenv(".env.local")
MISTRAL_API_KEY = os.environ["MISTRAL_API_KEY"]

client  = Mistral(api_key=MISTRAL_API_KEY)
model  = "mistral-large-latest"

# -----------------------------------------------------------------------
#                              TEST
# -----------------------------------------------------------------------
resp = client.chat.complete(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)

print(resp.choices[0].message.content)