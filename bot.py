import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8262043958:AAGJv8tr6dnJSCKM0zG4BWGLdvF1vmd-dDQ"

LEAD_MAGNET = """
🔥 AI AUTOBUILD KIT 🔥

Вот твой бесплатный набор:

⚡ 20 команд для Claude Code
   → Копируй и используй сразу

📋 Мой шаблон контент-пайплайна
   → Как генерировать неделю контента за 10 минут

🎯 Шаблон анализа конкурентов
   → Исследуй любого конкурента за 5 минут

🔧 5 кастомных навыков для Claude Code
   → Включая генератор заголовков и репостер

📜 Гайд по быстрому старту
   → Начни за 5 минут

═══════════════════════════════

📸 Подпишись на Instagram:
https://instagram.com/ТВОЙ_USERNAME

💬 Подпишись на Threads:
https://threads.net/ТВОЙ_USERNAME

═══════════════════════════════

Есть вопросы? Просто напиши мне в DM!
"""

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    name = user.first_name or "друг"

    welcome = f"""
👋 Привет, {name}!

Добро пожаловать в AI Autobuild Kit!

Это бесплатный набор для тех кто хочет автоматизировать свою работу с помощью Claude Code и AI.

🎁 Чтобы получить набор:
Напиши /getkit

Давай начнём! 🚀
"""
    await update.message.reply_text(welcome)


async def getkit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user

    logger.info(f"Лид: {user.username} ({user.id})")

    with open("leads.txt", "a") as f:
        f.write(f"{user.username} - {user.id}\n")

    await update.message.reply_text(LEAD_MAGNET)

    follow_up = """
🎉 Готово!

Проверь что внутри — всё бесплатно.

Не забудь подписаться на мой Instagram для ежедневных советов по AI!

Если есть вопросы — пиши в ответ!
"""
    await update.message.reply_text(follow_up)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
📋 Команды бота:

/start — Начать
/getkit — Получить набор
/help — Помощь

Есть вопросы? Просто напиши мне!
""")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getkit", getkit))
    app.add_handler(CommandHandler("help", help_cmd))

    print("🤖 Бот запущен!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
