from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from flask import Flask, request

TOKEN = os.getenv("8315139979:AAGJ43FwdBZMtU5zTMYTauC10I3Oaf0Q4uM")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Exemple : https://ton-projet.up.railway.app

app = Flask(name)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut avec Webhook p
telegram_app = ApplicationBuilder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), telegram_app.bot)
    telegram_app.update_queue.put_nowait(update)
    return "OK"

@app.route("/")
def index():
    return "Bot en ligne avec Webhook"

Setup du Webhook au dC)marrage
@app.before_first_request
def set_webhook():
    telegram_app.bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")

if name == "main":app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))
