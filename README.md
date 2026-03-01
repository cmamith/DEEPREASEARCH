# Deep Research Project

An AI-powered deep research tool that plans, performs web searches, and writes detailed reports.

## Setup

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables:**
   Ensure your `.env` file has the following:
   *   `OPENAI_API_KEY`: Your OpenAI API key.
   *   `SENDGRID_API_KEY`: Your SendGrid API key.
   *   `SENDER_EMAIL`: The verified sender email in your SendGrid account.
   *   `RECIPIENT_EMAIL`: The email address where you want to receive reports.

> [!IMPORTANT]
> **SendGrid Verification**: You MUST verify your `SENDER_EMAIL` in your SendGrid dashboard (Settings -> Sender Authentication). SendGrid will reject emails if the sender address is not verified.

## Running

Launch the research assistant:
```bash
python3 deep_research.py
```

Click the local link (e.g., `http://127.0.0.1:7860`) to open the UI.