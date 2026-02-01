from telegram.ext import ApplicationBuilder
from .handlers import register_handlers

async def start_bot(token):
    app = ApplicationBuilder().token(token).build()
    register_handlers(app)

    await app.initialize()
    await app.start()
    print("🤖 Bot is running on Colab")
