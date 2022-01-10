from pyrogram import Client, filters


@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"Sticker ID is \n <code>{message.reply_to_message.sticker.file_id}</code>\n\nUnique ID is\n\n<code>{message.reply_to_message.sticker.file_unique_id}</code>", reply_markup=BUTTONS, quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")
