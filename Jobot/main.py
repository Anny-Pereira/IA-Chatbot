import discord
from neuralintents import GenericAssistant

token = 'OTM4NDA1NDUyNTg3MzU2MTcw.Yfp0Lg.eZuJwIM5zrWtHl532ur_7S2fkR4'

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()

print("Bot rodando malandro...")

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$jobot"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)

client.run(token)