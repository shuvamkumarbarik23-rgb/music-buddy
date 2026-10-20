import os

def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

API_ID = int(_required("API_ID"))
API_HASH = _required("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
STRING_SESSION = os.getenv("STRING_SESSION", "").strip()
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
STREAM_URL = os.getenv("STREAM_URL", "").strip()

if not BOT_TOKEN and not STRING_SESSION:
    raise RuntimeError("Set BOT_TOKEN or STRING_SESSION. Voice-chat streaming may require a user session.")
