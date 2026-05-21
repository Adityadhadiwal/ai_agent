from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from orchestrator import AgentOrchestrator

app = FastAPI(title="AI Agent System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory session store (can upgrade to DB later)
session_store = {}

# Create orchestrator instance
orchestrator = AgentOrchestrator()


@app.post("/chat")
def chat(data: dict):
    user_id = "user1"
    user_input = data.get("message")

    if not user_input:
        return {"agent": "System", "message": "Please enter a message."}

    if user_id not in session_store:
        session_store[user_id] = {}

    session = session_store[user_id]

    response = orchestrator.handle(user_input, session)

    return response


@app.get("/")
def health_check():
    return {"status": "running"}