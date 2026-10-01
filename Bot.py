import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

# ដាក់ Token របស់អ្នកផ្ទាល់នៅទីនេះ
TOKEN = "8894788925:AAEAnqAAYuyGYH6_y04Av4xmBBTNhG83k90"

# បើកប្រព័ន្ធ Logging ដើម្បីងាយស្រួលតាមដានដំណើរបូត
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ពាក្យបញ្ជា /start និងបង្ហាញម៉ឺនុយប៊ូតុងដើម
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("📦 Stock", callback_data="stock"),
            InlineKeyboardButton("🛒 BUY NOW", callback_data="buy_now"),
        ],
        [
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "👋 Welcome to Bropheak Bot!\n\n"
        "🛍 សូមជ្រើសរើស Menu ខាងក្រោម៖",
        reply_markup=reply_markup,
    )

# ការគ្រប់គ្រងពេលអតិថិជនចុចលើប៊ូតុងផ្សេងៗ
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == "stock":
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="📦 **បញ្ជីស្តុកដែលមានស្រាប់៖**\n\n• AIM HACK V2 (ទំនេរ: 10)\n• Esign Certificate (ទំនេរ: 5)",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    elif query.data == "buy_now":
        # ម៉ឺនុយជ្រើសរើសធនាគារទូទាត់ប្រាក់ (ABA KHQR & ធនាគារផ្សេងៗ)
        keyboard = [
            [InlineKeyboardButton("💳 ABA KHQR", callback_data="pay_khqr")],
            [
                InlineKeyboardButton("📱 ABA", callback_data="pay_aba"),
                InlineKeyboardButton("🟢 Wing", callback_data="pay_wing"),
            ],
            [
                InlineKeyboardButton("💙 Acleda", callback_data="pay_acleda"),
                InlineKeyboardButton("🟠 TrueMoney", callback_data="pay_truemoney"),
            ],
            [InlineKeyboardButton("⬅️ Back", callback_data="back_to_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="🛒 **ជ្រើសរើសផលិតផល និងវិធីទូទាត់ប្រាក់៖**\n\n"
                 "🎮 **Game:** AIM HACK V2 - 0.50 USD\n\n"
                 "👇 សូមជ្រើសរើសធនាគារសម្រាប់ទូទាត់ខាងក្រោម៖",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    elif query.data == "pay_khqr" or query.data == "pay_aba":
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="buy_now")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="📲 **សូមស្កេន QR Code ដើម្បីទូទាត់ប្រាក់៖**\n\n"
                 "• ចំនួនទឹកប្រាក់: **0.50 USD**\n"
                 "• ពេលទូទាត់រួច ប្រព័ន្ធនឹងផ្ញើ Key ជូនស្វ័យប្រវត្តិ។",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    elif query.data == "help":
        keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data="back_to_menu")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="ℹ️ **ជំនួយ (Help)៖**\n\nសម្រាប់បញ្ហាទិញ Key ឬចង់សាកសួរព័ត៌មាន សូមទាក់ទង Admin ផ្ទាល់។",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )
    elif query.data == "back_to_menu":
        keyboard = [
            [
                InlineKeyboardButton("📦 Stock", callback_data="stock"),
                InlineKeyboardButton("🛒 BUY NOW", callback_data="buy_now"),
            ],
            [
                InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text="👋 Welcome to Bropheak Bot!\n\n"
                 "🛍 សូមជ្រើសរើស Menu ខាងក្រោម៖",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

def main() -> None:
    # បង្កើត Application សម្រាប់ Bot ( phiên bản v20+)
    application = Application.builder().token(TOKEN).build()

    # បញ្ចូល Handler សម្រាប់ /start និងប៊ូតុងអន្តរកម្ម
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # ចាប់ផ្តើមដំណើរការបូត
    application.run_polling()

if __name__ == "__main__":
    main()
