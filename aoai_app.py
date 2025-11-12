# Copyright (c) Microsoft. All rights reserved.

import asyncio
from datetime import datetime, timezone
from random import randint
from typing import Annotated

from agent_framework import ChatAgent
from agent_framework.azure import AzureOpenAIChatClient
from azure.identity import AzureCliCredential
from pydantic import Field
from dotenv import load_dotenv
import json

from form import Form

load_dotenv()

"""
Azure OpenAI Chat Client with Function Tools

Interactive chat agent with weather and time function calling abilities.
"""

async def conversation() -> None:
    """Interactive conversation with console input."""
    print("=== Interactive Chat with Weather and Time Functions ===")
    print("Type 'quit' or 'exit' to end the conversation\n")

    # Read JSON from myform.json
    try:
        with open('data/myform.json', 'r') as file:
            sample_data = json.load(file)
        print("Successfully loaded myform.json")
    except FileNotFoundError:
        print("Warning: myform.json file not found")
        sample_data = {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in myform.json")
        sample_data = {}
    f = Form(sample_data)

    # Create agent with tools
    agent = ChatAgent(
        chat_client=AzureOpenAIChatClient(credential=AzureCliCredential()),
        instructions="You are a helpful assistant that elicits data points ONE BY ONE from the user in order to help fill out the form. Pay attention to where the missing values are and ask for them. You are helpful and friendly in your manner of collecting information, and you mark the form done when it is complete. You always engage the user in a conversational format with complete sentences, never listing out parts of the form. Your job is to smooth the connection between the user and the form data.",
        tools=[f.read, f.write, f.mark_done],
    )

    # Create a new thread for the conversation
    thread = agent.get_new_thread()

    print("Agent: Hello! I'm your helpful assistant. I'll help you fill out this form.")

    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("Agent: Goodbye! Have a great day!")
                break
            
            if not user_input:
                print("Agent: Please enter a message.")
                continue

            # Get response from agent using the thread
            response = await agent.run(user_input, thread=thread)
            print(f"Agent: {response.text}")

        except KeyboardInterrupt:
            print("\n\nAgent: Goodbye! Conversation interrupted.")
            break
        except Exception as e:
            print(f"Agent: Sorry, I encountered an error: {e}")


async def main() -> None:
    await conversation()


if __name__ == "__main__":
    asyncio.run(main())
