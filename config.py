import os

def _required(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

API_ID = int(_required("31862898"))
API_HASH = _required("c0e5fa94ba15a7d8fd4a883c21db2afe")
BOT_TOKEN = os.getenv("8781475628:AAFhetyDEYXHod7RVnalPN8SCVhCjKEp9gg", "").strip()
STRING_SESSION = os.getenv("BQHmMHIAV8Htpyl8gXYIMbE8o0TGdvRaEEfBNLaCUfNPkpE_8b5xonEjOr2XEUNVWjEjCZvjBkgA6vkpR8ONrEt8BH33N6Ukz3uGcEo1YLEmnrUZ6_7elxNeQ3t5R2UPO4VZ1nBEMoIinKMcnWwv04UTvWmSS3DZhqStLzCmt-4IFb1JSELXm9HqdR8V2X6iUnLfThF4ZWhGLyOq7HdALSu3BEji-l5tSZhzhCWyC49pHSaN4d4WuYMWff4ktjXin7NuVdL9fXBrYGFHA9DdpzgGAFsWQn9yg5VlB3dyf1trfqS75ckwXLqPWQ2jow85ynpEVJyOI0M-UOzB1vQ4c5zA_GoCZgAAAAILnKT9AA", "").strip()
OWNER_ID = int(os.getenv("8734813395", "0"))
STREAM_URL = os.getenv("https://eu8.fastcast4u.com/proxy/clyedupq/stream", "").strip()

if not BOT_TOKEN and not STRING_SESSION:
    raise RuntimeError("Set BOT_TOKEN or STRING_SESSION. Voice-chat streaming may require a user session.")
