from fastapi import FastAPI from telegram import Update, BotCommand from telegram.ext import ( ApplicationBuilder, CommandHandler, ContextTypes, ) import os import logging

Enable logging

logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO ) logger = logging.getLogger(name)

Create FastAPI app

app = FastAPI()

Your Telegram bot token (replace this with your actual token)

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

Start command handler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): welcome_text = ( "🎬 Welcome to Sidharth AI Studio! 🤖\n\n" "Main hoon aapka full-time AI content creator assistant.\n\n" "Yeh commands try karo:\n" "👉 /script [topic] – Reels ya Shorts ke liye script\n" "👉 /image [prompt] – AI-generated image\n" "👉 /title [desc] – YouTube title + hashtags\n" "👉 /idea – Daily content idea\n" "👉 /caption [desc] – Insta caption with hashtags\n\n" "Let's create something amazing! 💡" ) await update.message.reply_text(welcome_text, parse_mode="Markdown")

Initialize bot

@app.on_event("startup") async def startup_event(): application = ( ApplicationBuilder() .token(BOT_TOKEN) .build() )

application.add_handler(CommandHandler("start", start))

await application.bot.set_my_commands([
    BotCommand("start", "Start the bot"),
    BotCommand("script", "Get video script for a topic"),
    BotCommand("image", "Generate image from a prompt"),
    BotCommand("title", "Generate YouTube title and hashtags"),
    BotCommand("idea", "Get a daily content idea"),
    BotCommand("caption", "Get Instagram caption with hashtags"),
])

await application.initialize()
await application.start()
logger.info("Bot started...")

Root endpoint for FastAPI

@app.get("/") async def root(): return {"message": "SidharthContentBot backend is running."}

