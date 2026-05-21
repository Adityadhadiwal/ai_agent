# AI Agent System (CrewAI + Groq)

## Overview
This project demonstrates a simple multi-agent AI system where a frontend agent interacts with a backend agent to generate content.

## Features
- Multi-step agent interaction
- CrewAI integration
- Groq LLM for fast inference
- React chat UI

## Tech Stack
- Frontend: React (Vite)
- Backend: FastAPI
- AI: CrewAI + Groq (LLaMA3)

## Flow
1. User gives topic
2. Backend asks clarifying questions
3. Agents process input
4. Final content generated

## Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload