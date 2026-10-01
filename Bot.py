from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

# ១. ប៊ូតុងម៉ឺនុយជ្រើសរើសធនាគារទូទាត់ប្រាក់ (Payment Menu)
def payment_keyboard():
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
    return Zahlung_markup if 'Zahlung_markup' else InlineKeyboardMarkup(keyboard)

# 2. ប៊ូតុង Menu ជាប់នៅផ្នែកខាងក្រោម (Reply Keyboard ដូចពាក្យ BUY NOW)
def persistent_menu():
    keyboard = [[KeyboardButton("🛒 BUY NOW")]]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# ៣. ទម្រង់សារបង្ហាញពេលទូទាត់ប្រាក់ជោគជ័យ និងទទួលបាន Key ស្វ័យប្រវត្តិ
success_message = (
    "✅ **Payment verified!**\n"
    "🎮 **Game:** 🛡 AIM HACK V2\n"
    "⏱ **Duration:** 1H\n"
    "💰 **Amount Paid:** 0.50 USD\n"
    "🔑 **Your Keys:** `TRLL-6D71-6B4E-6076`\n\n"
    "🕒 **Time:** 01-10-2026 06:38 AM\n"
    "✅ **Status:** Completed (Auto)\n"
    "🎉 **Thank you for your purchase!**"
)
