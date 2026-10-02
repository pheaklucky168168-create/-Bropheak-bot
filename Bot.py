import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

# ដាក់ Telegram Bot Token របស់អ្នកនៅទីនេះ
API_TOKEN = '8872378600:AAHKQ0xMbiDnHhHxyowP_88bI2GXPQt0IG8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# ១. បង្កើតប៊ូតុង Reply Keyboard នៅខាងក្រោម (BUY NOW)
main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(KeyboardButton("🛒 BUY NOW"))

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "សួស្តី! សូមស្វាគមន៍មកកាន់ហាងលក់ទំនិញស្វ័យប្រវត្តិរបស់យើង។",
        reply_markup=main_kb
    )

# ២. ពេលអតិថិជនចុចប៊ូតុង BUY NOW
@dp.message_handler(lambda message: message.text == "🛒 BUY NOW")
async def process_buy_now(message: types.Message):
    inline_kb = InlineKeyboardMarkup(row_width=1)
    inline_kb.add(InlineKeyboardButton("🎯 AIM HACK V2", callback_data="category_aim_hack"))
    
    await message.answer("Choose a category:", reply_markup=inline_kb)

# ៣. ពេលអតិថិជនចុចលើ AIM HACK V2 -> បង្ហាញជម្រើសរយៈពេល និងស្តុក
@dp.callback_query_handler(text="category_aim_hack")
async def process_aim_hack(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    product_kb = InlineKeyboardMarkup(row_width=1)
    product_kb.add(
        InlineKeyboardButton("1H - $0.50 [Stock: 154]", callback_data="buy_1h"),
        InlineKeyboardButton("3H - $0.75 [Stock: 123]", callback_data="buy_3h"),
        InlineKeyboardButton("⬅️ Back", callback_data="back_to_menu")
    )
    
    caption = "🎯 **AIM HACK V2**\n\nSelect a product:"
    await bot.send_message(callback_query.from_user.id, caption, reply_markup=product_kb, parse_mode="Markdown")

# ៤. ពេលអតិថិជនជ្រើសរើស 1H -> បង្ហាញវិធីសាស្ត្រទូទាត់ប្រាក់ (ABA KHQR)
@dp.callback_query_handler(text="buy_1h")
async def process_buy_1h(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    payment_kb = InlineKeyboardMarkup(row_width=1)
    payment_kb.add(
        InlineKeyboardButton("🟥 ABA KHQR", callback_data="show_qr_aba"),
        InlineKeyboardButton("⬅️ Back", callback_data="category_aim_hack")
    )
    
    await bot.send_message(
        callback_query.from_user.id,
        "💰 ជ្រើសរើសវិធីទូទាត់ខាងក្រោម",
        reply_markup=payment_kb
    )

# ៥. ពេលអតិថិជនចុចលើ ABA KHQR -> បង្ហាញ QR Code និងវិក្កយបត្រ (តាមរូបភាពតេស្ត)
@dp.callback_query_handler(text="show_qr_aba")
async def process_show_qr(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    
    order_id = "#ORD-0XMBX2FS"
    # យករូបភាព QR Code គំរូមកបង្ហាញ
    qr_image_url = "https://via.placeholder.com/300.png?text=KHQR+0.50USD" 
    
    text_invoice = (
        f"📋 Order **{order_id}**\n\n"
        f"ទំនិញ៖ **1H**\n"
        f"ចំនួនទឹកប្រាក់៖ **0.50 ដុល្លារ**\n\n"
        f"📱 សេនលេខកូដ QR ដើម្បីបង់ប្រាក់៖\n"
        f"1. បើកកម្មវិធីធនាគាររបស់អ្នក\n"
        f"2. សេន QR ខាងលើ\n"
        f"3. បំពេញការទូទាត់\n"
        f"4. រង់ចាំការបញ្ជាក់ដោយស្វ័យប្រវត្តិ\n\n"
        f"⏱ រយៈពេលផុតកំណត់៖ 3 នាទី\n\n"
        f"✅ ការទូទាត់នឹងត្រូវបានផ្ទៀងផ្ទាត់ដោយស្វ័យប្រវត្តិ!"
    )
    
    cancel_kb = InlineKeyboardMarkup()
    cancel_kb.add(InlineKeyboardButton("❌ Cancel", callback_data="cancel_order"))
    
    await bot.send_photo(
        callback_query.from_user.id,
        photo=qr_image_url,
        caption=text_invoice,
        reply_markup=cancel_kb,
        parse_mode="Markdown"
    )

# ប៊ូតុងបោះបង់ (Cancel)
@dp.callback_query_handler(text="cancel_order")
async def cancel_order(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="បានបោះបង់ការបញ្ជាទិញ!")
    await callback_query.message.delete()

@dp.callback_query_handler(text="back_to_menu")
async def back_to_menu(callback_query: types.CallbackQuery):
    await callback_query.message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
