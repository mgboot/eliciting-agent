# Eliciting Agent

An intelligent form-filling assistant powered by Azure OpenAI and the Agent Framework library. This application creates a conversational AI agent that helps users complete complex forms through natural, interactive chat conversations rather than rigid step-by-step procedures.

## Overview

The Eliciting Agent transforms the tedious process of filling out forms into an engaging, dynamic conversation. Instead of presenting users with overwhelming form fields or following a rigid sequence, the agent intelligently adapts the conversation flow, identifies missing information, and asks for it in a friendly, conversational manner that feels natural and responsive.

## Features

- **Dynamic Conversational Interface**: Interactive chat that adapts to user responses and conversation flow
- **Intelligent Data Elicitation**: Agent contextually identifies missing fields and asks for them conversationally
- **Universal JSON Form Support**: Works with virtually any JSON-based form structure
- **Adaptive Conversation Flow**: No rigid procedures - the agent responds naturally to how users provide information
- **Azure OpenAI Integration**: Leverages advanced language models for natural, human-like conversations
- **Function Calling**: Agent can read, write, and manage form state dynamically during chat

## Prerequisites

- Python 3.11+
- Azure OpenAI service access
- Azure CLI (for authentication)

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd eliciting-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install agent-framework azure-identity python-dotenv pydantic
   ```

3. **Configure environment**:
   - Copy `sample.env` to `.env`
   - Configure your Azure OpenAI credentials

4. **Authenticate with Azure CLI**:
   ```bash
   az login
   ```

## Usage

1. **Customize your form**: Edit `data/myform.json` with your desired form structure, or use one of the templates from `data/samples/`
2. **Run the application**:
   ```bash
   python aoai_app.py
   ```
3. **Start chatting**: Engage in a natural conversation where the agent will guide you through completing the form

## Form Flexibility

The application works with virtually any JSON-based form structure. The `data/samples/` directory contains multiple example templates that you can copy into `data/myform.json` to get started with different types of forms. The agent automatically adapts to whatever JSON structure you provide - no code changes required!

## How It Works

1. **Form Loading**: The application loads any JSON form structure from `data/myform.json`
2. **Agent Initialization**: Creates a conversational chat agent with three key functions:
   - `read()`: Retrieves current form state
   - `write(path, value)`: Updates specific form fields
   - `mark_done()`: Marks the form as complete
3. **Interactive Chat**: The agent engages in natural conversation, dynamically responding to user input and guiding form completion
4. **Contextual Completion**: Agent conversationally determines when all required fields are filled and naturally concludes the process

## Conversational Experience

Unlike traditional forms, this agent creates a chat-based experience where:
- Users can provide information in any order
- The conversation flows naturally based on context
- The agent asks follow-up questions conversationally
- Information can be clarified or corrected through dialogue
- The process feels like talking to a helpful assistant, not filling out a form

## Sample Templates

The `data/samples/` directory contains example form structures that demonstrate the versatility of the system. Simply copy any template to `data/myform.json` to try different form types, or create your own JSON structure.

## Architecture

- **`aoai_app.py`**: Main application with interactive chat loop
- **`form.py`**: Form class with read/write/completion functionality
- **`data/myform.json`**: Active form structure (customizable)
- **`data/samples/`**: Template forms for different use cases
- **Agent Framework**: Handles Azure OpenAI integration and function calling

## Customization

To adapt this for any form type:
1. Replace `data/myform.json` with your JSON form structure (or copy from templates)
2. Optionally modify the agent instructions in `aoai_app.py` for domain-specific guidance
3. The system automatically handles any JSON structure through conversational interaction

---

This project demonstrates how AI agents can create more intuitive, conversational interfaces for data collection, transforming rigid forms into engaging chat experiences.