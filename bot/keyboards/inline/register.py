from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

keyboard = InlineKeyboardBuilder()
cancel_btn = InlineKeyboardButton(
    text="Register",
    callback_data="register_data"
)

keyboard.add(cancel_btn)
