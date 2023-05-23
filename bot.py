import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        if user_message =='who created you?':
            await message.channel.send('',file=discord.File('download.jpg'))

        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN ='MTAzNzAyNjY4MzMyMjEwNTk0MA.GY7k64.5vqDtxJP9bQUtM_LPHLePh8uadq72MRhTEixIQ'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
