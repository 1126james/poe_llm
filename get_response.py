import asyncio
import uuid
import fastapi_poe as fp
import time
import os
from prompts import *

# Replace <api_key> with your actual API key, ensuring it is a string.
api_key = os.getenv('API_KEY')

# Define the role for the AI assistant
prompt = SUGGEST_TRANSFORMATIONS_PROMPT

# List of models on POE
# GPT4o, Claude-3.5-Sonnet, Llama-3.1-405B, Gemini-1.5-Pro, Llama-3.1-Nemotron, Mistral-Large-2
poe_bots = ['GPT4o',
            'Claude-3.5-Sonnet',
            'Llama-3.1-405B',
            'Gemini-1.5-Pro',
            'Llama-3.1-Nemotron',
            'Mistral-Large-2']
# Create an asynchronous function to get the final response
async def get_final_response(api_key, query_request):
    response = await fp.get_final_response(request=query_request, bot_name=poe_bots[0], api_key=api_key)
    return response

user_id = f"u-{uuid.uuid4().hex}"
conversation_id = f"c-{uuid.uuid4().hex}"

# Start the conversation loop
while True:
    user_input = input("User: ")
    if user_input.lower() == 'exit':
        break

    # Construct the user message
    user_message = fp.ProtocolMessage(
        role='user',
        content = str(user_input),
        content_type = 'text/markdown',
        timestamp = int(time.time() * 1000000),
        message_id = ""
    )
    # Construct messages
    system_message = fp.ProtocolMessage(
        role="system",
        content=prompt,
        content_type = 'text/markdown',
        timestamp = int(time.time() * 1000000),
        message_id = ""
    )

    # Create a QueryRequest object
    query_request = fp.QueryRequest(
        version = '1.0',
        type = 'query',
        query=[system_message, user_message],
        user_id = user_id,
        conversation_id = conversation_id,
        message_id = ""
    )

    response = asyncio.run(get_final_response(api_key, query_request))
    print(f"Jennie: {response}")