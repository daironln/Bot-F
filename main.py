from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

BOT_TOKEN = ''

async def start(update: Update, context):
    args = context.args
    if args:
        custom_data = args[0]
        await update.message.reply_text(f"Datos recibidos: {custom_data}")
    else:
        await update.message.reply_text("¡Bienvenido al juego!")

    keyboard = [
        [InlineKeyboardButton("Jugar", callback_data='play_game')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Haz clic para jugar:", reply_markup=reply_markup)

async def play_game(update: Update, context):
    query = update.callback_query
    await query.answer()
    
    print(query.from_user.id)
    print(query.from_user.get_profile_photos)

    game_url = f""
    await query.message.reply_game(
        game_short_name='',
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Abrir Juego", url=game_url)]])
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(play_game))

app.run_polling()
