def cosmic_style():
    return """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        .stApp {
            background-color: #050816;
            color: #e0e6ff;
            font-family: 'Orbitron', sans-serif;
        }
        h1, h2, h3, label, .stMarkdown {
            color: #a8c0ff !important;
        }
        .stSidebar {
            background-color: #0a0f2d;
        }
        .stButton>button {
            background-color: #1e2a47;
            color: white;
            border-radius: 12px;
            padding: 0.6em 1.2em;
            font-size: 1em;
            border: 1px solid #3a4b8a;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #3a4b8a;
            transform: scale(1.05);
        }
    </style>
    """
