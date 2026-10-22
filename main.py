import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION, OWNER_ID, STREAM_URL
from pyrogram import filters, enums




logging.basicConfig(level=logging.INFO)
log = logging.getLogger("sukuna-x-music")

# A user session is recommended for voice-chat streaming.
# If STRING_SESSION is set, use it; otherwise try the bot token client.
if STRING_SESSION:
    app = Client("sukuna_radio", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION)
else:
    app = Client("sukuna_radio_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

calls = PyTgCalls(app)
current_chat = None

@app.on_message(filters.command(["start", "help"]) & filters.private)
async def start_command(_, message: Message):
    await message.reply_text(
        "🎧 **Sukuna X Music Radio**\n\n"
        "Add me to your group and make sure I can access the voice chat.\n"
        "`/radio` — start the configured stream in this group voice chat\n"
        "`/stopradio` — stop streaming\n"
        "`/radiohelp` — show help\n\n"
        "Set `STREAM_URL` to a direct audio stream URL in your environment."
    )

@app.on_message(filters.command(["radiohelp", "help_radio"]))
async def radio_help(_, message: Message):
    await message.reply_text(
        "🎵 **Radio commands**\n"
        "`/radio` — start the stream in the current group's voice chat\n"
        "`/stopradio` — stop the stream\n\n"
        "Before using `/radio`, start a voice chat in the group. "
        "Use a direct audio stream URL that you are allowed to rebroadcast."
    )

@app.on_message(filters.command("radio") & filters.group)
async def radio_command(_, message: Message):
    global current_chat
    if not STREAM_URL:
        await message.reply_text("Set the STREAM_URL environment variable first.")
        return
    chat_id = message.chat.id
    try:
        await calls.play(chat_id, MediaStream(STREAM_URL))
        current_chat = chat_id
        await message.reply_text("📻 Radio stream started.")
    except Exception as exc:
        log.exception("Could not start stream")
        await message.reply_text(
            "Couldn't start the radio. Make sure a voice chat is already active, "
            "the stream URL is direct/reachable, and the account has permission to join.\n"
            f"Error: `{type(exc).__name__}: {exc}`"
        )

@app.on_message(filters.command("stopradio") & filters.group)
async def stop_radio(_, message: Message):
    global current_chat
    try:
        await calls.leave_call(message.chat.id)
        current_chat = None
        await message.reply_text("⏹️ Radio stopped.")
    except Exception as exc:
        await message.reply_text(f"No active stream found, or stop failed: `{type(exc).__name__}`")
@app.on_message(filters.command("channelpost") & filters.private)
async def channel_post(_, message: Message):
    # Only the configured owner can post
    if message.from_user.id != OWNER_ID:
        await message.reply_text("⛔ You are not authorized.")
        return

    text = message.text.split(maxsplit=1)

    if len(text) < 2:
        await message.reply_text(
            "Usage:\n/channelpost Your message here"
        )
        return

    post_text = text[1]

    try:
        await app.send_message(
            CHANNEL_USERNAME,
            post_text
        )
        await message.reply_text("✅ Message posted to your channel!")
    except Exception as exc:
        log.exception("Channel post failed")
        await message.reply_text(
            f"❌ Could not post: {type(exc).__name__}: {exc}"
        )

async def main():
    await app.start()
    await calls.start()
    log.info("Sukuna X Music is online")
    # Keep the process alive for Render/Docker/worker hosting.
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
