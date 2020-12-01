import os, time, asyncio, discord

client = discord.Client()

token = os.environ["TOKEN"]

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

    while True:
        time.sleep(0.8)

        channel = client.get_channel(780344500408549376)
        await channel.send("24시간 도배 ^^")


client.run(token, bot=False)
