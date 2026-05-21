from crewai import Task, Crew
from agents import create_content_agent


class AgentOrchestrator:

    def __init__(self):
        self.content_agent = create_content_agent()

    def ask_style(self):
        return {
            "agent": "Clarification Agent",
            "message": "How should this content feel?",
            "options": ["LinkedIn", "Casual", "Technical"]
        }

    def ask_depth(self):
        return {
            "agent": "Clarification Agent",
            "message": "How deep should we go?",
            "options": ["Quick", "Detailed"]
        }

    def generate_content(self, session):

        task = Task(
            description=f"""
            Write a high-quality blog.

            Topic: {session['task']}
            Style: {session['style']}
            Depth: {session['depth']}

            Make it engaging, structured, and relevant.
            """,
            agent=self.content_agent
        )

        crew = Crew(
            agents=[self.content_agent],
            tasks=[task]
        )

        result = crew.kickoff()

        return {
            "agent": "Content Agent",
            "result": result
        }

    def handle(self, user_input, session):

        # Step 1: Initial input
        if not session:
            session["task"] = user_input
            return {
                "agent": "Intent Agent",
                "message": "Got your request. Let’s refine it..."
            }

        # Step 2: Capture style
        if not session.get("style"):
            session["style"] = user_input
            return {
                "agent": "Clarification Agent",
                "message": "Nice choice. Now select depth."
            }

        # Step 3: Capture depth
        if not session.get("depth"):
            session["depth"] = user_input

        # Step 4: Generate output
        return self.generate_content(session)