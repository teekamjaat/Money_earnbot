from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your bot token
BOT_TOKEN = "8066854204:AAFYhX1MipAK65MO0uH1o_R_b_nWFjLyeGM"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Image URL or File ID
    photo_url = "https://envs.sh/eRh.jpg"  # Replace with your own image URL or local file path
    
    # Caption text
    caption = "👋 Welcome to the Earning Bot!\n\nFollow the steps below to start earning rewards:"

    # Define buttons
    keyboard = [
        [InlineKeyboardButton("💬 Chat With Admin", url="https://t.me/Refrell_Earing_Support"),
         InlineKeyboardButton("🔗 Click Here to Refer", url="https://t.me/share/url?url=https://t.me/MoneyEarningg_Bot/Money")],
        [InlineKeyboardButton("📢 Join Update Channel", url="https://t.me/+fEs3x8dYqx0xY2U1")],
        [InlineKeyboardButton("🚀 Start Earnings Now", url="https://t.me/MoneyEarningg_Bot/Money")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send photo with caption and buttons
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=photo_url,
        caption=caption,
        reply_markup=reply_markup
    )

# Main function
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling()
