import asyncio
import uuid
import fastapi_poe as fp
import time
import os

# Replace <api_key> with your actual API key, ensuring it is a string.
api_key = os.getenv('API_KEY')

# Define the role for the AI assistant
role_description = """
You are an 18-year-old gamer girl, named Jennie.
You are a gaming friend of the user.
Keep the conversation natural and not like novel, and keep it short.
Respond to the user in an entertaining, fun, and sometimes a very little bit of flirty yet shy tone.

### Convert all actions originally in * to [ ],
### Such as from *giggles shyly* to [giggles shyly]
### Example 2: from *smiles brightly* to [smiles brightly]
""".strip()

# Create an asynchronous function to get the final response
async def get_final_response(api_key, query_request):
    response = await fp.get_final_response(request=query_request, bot_name="Claude-3-Haiku", api_key=api_key)
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
        content=role_description,
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