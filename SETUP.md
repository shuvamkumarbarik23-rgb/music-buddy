Sukuna X Music — Render setup
Render service
- Create a Background Worker.
- Runtime: Python.
- Build command: pip install -r requirements.txt
- Start command: python main.py
- Python version: 3.11 is suitable.
Environment variables
Add these under the Render service's Environment tab. Use the actual values; do not include quotes.
- API_ID: numeric Telegram API ID from my.telegram.org
- API_HASH: Telegram API hash from my.telegram.org
- BOT_TOKEN: bot token from @BotFather (if using bot-token mode)
- STRING_SESSION: optional compatible user session; voice-chat streaming may require a user session
- STREAM_URL: optional direct, reachable audio stream URL
- OWNER_ID: optional numeric Telegram user ID
Keep API hashes, bot tokens, and session strings private. Do not commit real credentials to GitHub.
Deploy
1. Put main.py, config.py, and requirements.txt in the repository root.
2. Commit and push the files to GitHub.
3. In Render, use Manual Deploy → Clear build cache & deploy to avoid reusing old dependencies.
4. Test /start in Telegram. Start a group voice chat before trying /radio.
Notes
- The requirements use py-tgcalls[pyrogram], which installs the PyrogramMod adapter expected by this PyTgCalls release. Do not separately pin the original Pyrogram==2.0.106 alongside it.
- Successful deployment does not guarantee a voice-chat stream will start. Telegram permissions, session type, an active voice chat, and a direct playable audio URL all matter.
- .env.example is a template only. On Render, enter values in the Environment settings.
