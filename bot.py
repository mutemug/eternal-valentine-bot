import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8504832659:AAFuf5I8rk5HgYZnoUWepjCiRPkhe6bhFsg"
SITE_URL = "https://mutemug.github.io/Eternal-Valentine/"
SCENE_1 = "https://raw.githubusercontent.com/mutemug/Eternal-Valentine/main/scene1.png"
SCENE_2 = "https://raw.githubusercontent.com/mutemug/Eternal-Valentine/main/scene1.png"
SCENE_3 = "https://raw.githubusercontent.com/mutemug/Eternal-Valentine/main/scene3.png"
SCENE_4 = "https://raw.githubusercontent.com/mutemug/Eternal-Valentine/main/scene4.png"
SCENE_5 = "https://raw.githubusercontent.com/mutemug/Eternal-Valentine/main/scene5.png"
SCENE_6 = "https://raw.githubusercontent.com/mutemug/Eternal-Valentine/main/scene6.png"


bot = telebot.TeleBot(TOKEN)

user_hearts = {}
quest_completed = set()


# -------- START --------
@bot.message_handler(commands=['start'])
def start(message):

    if message.chat.id in quest_completed:
        bot.send_message(message.chat.id,
                         "You have already completed this quest, brave mage. 💖")
        return

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("🔮 Investigate the mist", callback_data="investigate"),
        InlineKeyboardButton("⚔️ Prepare a defensive spell", callback_data="spell")
    )

    bot.send_photo(
        message.chat.id,
        SCENE_1,
        caption=
        "🌫 *The City in the Rose Mist*\n\n"
        "The wandering mage arrives at the gates of an unfamiliar city.\n"
        "A strange pink mist floats through the streets…\n\n"
        "“A curse?” — he whispers.",
        parse_mode="Markdown",
        reply_markup=markup
    )


# -------- CALLBACKS --------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == "investigate":

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🎵 Follow the music", callback_data="music"))

        bot.edit_message_media(
            telebot.types.InputMediaPhoto(
                SCENE_2,
                caption=
                "You step into the mist cautiously.\n\n"
                "It smells of roses… and warm sugar.\n"
                "Instead of screams — you hear laughter.\n"
                "Instead of chaos — music."
            ),
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif call.data == "spell":

        markup = InlineKeyboardMarkup()
        markup.add(
            InlineKeyboardButton("😳 Lower your staff", callback_data="reveal"),
            InlineKeyboardButton("🎭 Ask what is happening", callback_data="reveal")
        )

        bot.edit_message_media(
            telebot.types.InputMediaPhoto(
                SCENE_3,
                caption=
                "Arcane energy gathers at your fingertips.\n\n"
                "The mist swirls — then pops like sparkling dust.\n"
                "A group of townsfolk stare at you.\n\n"
                "“Are you… rehearsing?”"
            ),
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    elif call.data in ["music", "reveal"]:

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("💌 Approach the crowd", callback_data="climax"))

        bot.edit_message_media(
            telebot.types.InputMediaPhoto(
                SCENE_4,
                caption=
                "Lanterns glow above the streets.\n"
                "Petals fall from balconies.\n\n"
                "💗 Festival of Eternal Hearts 💗\n\n"
                "The pink mist?\nIt’s festival magic."
            ),
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    # -------- КУЛЬМИНАЦИЯ --------
    elif call.data == "climax":

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("✨ Accept the gift", callback_data="finish"))

        bot.edit_message_media(
            telebot.types.InputMediaPhoto(
                SCENE_5,
                caption=
                "An elderly woman smiles at you.\n\n"
                "“You looked ready to save us, brave mage.”\n\n"
                "She presses something warm into your palm.\n\n"
                "💞 *10 Crystal Hearts shimmer softly.*\n\n"
                "“Even heroes deserve to celebrate love.”",
                parse_mode="Markdown"
            ),
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )

    # -------- ФИНАЛ --------
    elif call.data == "finish":

        user_hearts[call.message.chat.id] = user_hearts.get(call.message.chat.id, 0) + 10
        quest_completed.add(call.message.chat.id)

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("🔓 Discover", url=SITE_URL))

        bot.edit_message_media(
            telebot.types.InputMediaPhoto(
                SCENE_6,
                caption=
                "✨ *Quest Complete: The City in the Rose Mist*\n\n"
                "💖 You received *10 Hearts!*\n\n"
                "Perhaps… you should see what they can unlock.",
                parse_mode="Markdown"
            ),
            call.message.chat.id,
            call.message.message_id,
            reply_markup=markup
        )


bot.infinity_polling()