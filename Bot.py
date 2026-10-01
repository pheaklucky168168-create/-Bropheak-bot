import os

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📦 Stock", callback_data="stock"),
            InlineKeyboardButton("🛒 BUY NOW", callback_data="buy"),
        ],
        [
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to Bropheak Bot!\n\n"
        "🛍️ សូមជ្រើសរើស Menu ខាងក្រោម៖",
        reply_markup=reply_markup,
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "stock":
        await query.edit_message_text(
            "📦 STOCK\n\n"
            "ឥឡូវនេះមិនទាន់មានទំនិញក្នុង Stock ទេ។\n"
            "សូមរង់ចាំ Admin បន្ថែម Stock។"
        )

    elif query.data == "buy":
        await query.edit_message_text(
            "🛒 BUY NOW\n\n"
            "សូមជ្រើសរើសទំនិញដែលអ្នកចង់ទិញ។\n\n"
            "🚧 Purchase system កំពុងរៀបចំ..."
        )

    elif query.data == "help":
        await query.edit_message_text(
            "ℹ️ HELP\n\n"
            "ប្រសិនបើអ្នកមានបញ្ហា សូមទាក់ទង Admin។"
        )


def main():
    if not TOKEN:
        raise ValueError("BOT_TOKEN is not configured.")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
