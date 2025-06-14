from telegram import Update
from telegram.ext import ContextTypes

from bot.translate import translate


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        rf"Olar {user.mention_html()}!"
        "\n"
        "Bem vindo ao Dinofauro Fex Bot!\n"
        "\n"
        "Digite alguma mensagem para mim que eu enviarei as \"tradufõef\".\n"
        "Se precisar de alguma ajuda, só chamar o comando /help.",
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Precisando de ajuda?\n"
        "\n"
        "Comandos:\n"
        "/start - Inicia o bot\n"
        "/help - Mostra tudo que você precisa saber (Você está aqui!)\n"
        "/about - Informações sobre o bot e os desenvolvedores\n"
        "\n"
        "O bot atualmente funciona no 'modo echo':\n"
        "Ao enviar uma mensagem para o bot, que não seja um "
        "comando (palavra que não comece com '\\') ele retornará a mensagem 'traduzida'."
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Essa é a primeira versão teste do bot. "
        "Caso tenha algum feedback, mande para o desenvolvedor:\n"
        "@exaGeraldo"
    )

async def translation(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(translate(update.message.text))