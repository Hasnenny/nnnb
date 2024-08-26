
import telebot

bot = telebot.TeleBot("7163792001:AAF0-3OYkxmhBqWtmpERCXHTNq_3zD8l5B0")

admins = [7031471363]  #ايديك هنا بس شيل ايدي وحط ايديك
#\===================/#
@bot.message_handler(func=lambda message: message.reply_to_message is not None and message.text.startswith('تق') and message.from_user.id in admins)
def restrict_user(message):
    user_id = message.reply_to_message.from_user.id
    bot.restrict_chat_member(message.chat.id, user_id, until_date=0)
    bot.send_message(message.chat.id, f"""تم تقييد العضو  {message.reply_to_message.from_user.first_name} 
بواسطة الادمن الجميل 🥹""")

@bot.message_handler(func=lambda message: message.reply_to_message is not None and message.text.startswith('رف') and message.from_user.id in admins)
def unrestricted_user(message):
    user_id = message.reply_to_message.from_user.id
    bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
    bot.send_message(message.chat.id, f"""تم رفع التقييد {message.reply_to_message.from_user.first_name} 
بواسطة الجميل الادمن الجميل 🥹""")

print("""تم تفعيل البوت 
ارفع البوت مشرف في مجموعتك مع صلاحية حذف الرسائل ومبروك
لا تنسى حسابي تلي : @dudrd""")
bot.polling()
