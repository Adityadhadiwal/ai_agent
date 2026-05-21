import { useState } from "react";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async (msg) => {
    if (!msg) return;

    setMessages(prev => [...prev, { sender: "user", text: msg }]);

    const res = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ message: msg })
    });

    const data = await res.json();

    setMessages(prev => [
      ...prev,
      {
        sender: "agent",
        text: data.message || data.result,
        options: data.options || []
      }
    ]);

    setInput("");
  };

  return (
    <div className="container">
      <h2>AI Agent System</h2>

      <div className="chat">
        {messages.map((m, i) => (
          <div key={i} className={`bubble ${m.sender}`}>
            <p>{m.text}</p>

            {m.options.map((opt, idx) => (
              <button key={idx} onClick={() => sendMessage(opt)}>
                {opt}
              </button>
            ))}
          </div>
        ))}
      </div>

      <div className="inputBox">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button onClick={() => sendMessage(input)}>Send</button>
      </div>
    </div>
  );
}

export default App;