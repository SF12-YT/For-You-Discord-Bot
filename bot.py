import discord
from bs4 import BeautifulSoup
import requests
import collections
import random

images = []
videos = []
quote = []

URLImg = ["https://images.search.yahoo.com/search/images;_ylt=AwrxhdeaAXteHUMAu4IN5gt.?p=selena+gomez+beautiful&ei=UTF-8&fr=yfp-t&fr2=p%3As%2Cv%3Ai", "https://images.search.yahoo.com/search/images;_ylt=AwrwJRipAXteg1kAcdYN5gt.;_ylu=X3oDMTBsZ29xY3ZzBHNlYwNzZWFyY2gEc2xrA2J1dHRvbg--;_ylc=X1MDMjExNDcwOTAwNQRfcgMyBGFjdG4DY2xrBGNzcmNwdmlkA2pjUkozREV3TGpKQ1J5aXpYbnJ4TGdRY05UZ3VNUUFBQUFCdUdGR1cEZnIDeWZwLXQEZnIyA3NhLWdwBGdwcmlkA1ZxbmQxN2xEUlRxUVA2Y3U3NXoxTUEEbl9zdWdnAzAEb3JpZ2luA2F1LmltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzIxBHF1ZXJ5A3NlbGVuYSUyMGdvbWV6JTIwY3V0ZQR0X3N0bXADMTU4NTExOTY4OQ--?p=selena+gomez+cute&fr=yfp-t&fr2=sb-top-au.images.search&ei=UTF-8&n=60&x=wrt", "https://images.search.yahoo.com/search/images;_ylt=AwrwJQ3JAXteP1AAwlEN5gt.;_ylu=X3oDMTBsZ29xY3ZzBHNlYwNzZWFyY2gEc2xrA2J1dHRvbg--;_ylc=X1MDMjExNDcwOTAwNQRfcgMyBGFjdG4DY2xrBGNzcmNwdmlkA0V2a1lMakV3TGpKQ1J5aXpYbnJ4TGdYcE5UZ3VNUUFBQUFCdl9ia2YEZnIDeWZwLXQEZnIyA3NhLWdwBGdwcmlkA3ZUYkhxc3ViU3RDeFNPQ3B0QmhqekEEbl9zdWdnAzAEb3JpZ2luA2F1LmltYWdlcy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzI1BHF1ZXJ5A3NlbGVuYSUyMGdvbWV6JTIwYWRvcmFibGUEdF9zdG1wAzE1ODUxMTk3MjM-?p=selena+gomez+adorable&fr=yfp-t&fr2=sb-top-au.images.search&ei=UTF-8&n=60&x=wrt"]
URLYT = "https://www.youtube.com/user/SelGomez/videos?view=64&flow=grid"
URLQ = ["https://www.goodreads.com/author/quotes/4039819.Selena_G_mez?page=1", "https://www.goodreads.com/author/quotes/4039819.Selena_G_mez?page=2"]
URLQ = random.choice(URLQ)
URLImg = random.choice(URLImg)
pageImg = requests.get(URLImg)
pageYT = requests.get(URLYT)
pageQ = requests.get(URLQ)
resultsYT =  BeautifulSoup(pageYT.content, 'html.parser')
resultsImg =  BeautifulSoup(pageImg.content, 'html.parser')
resultsQ = BeautifulSoup(pageQ.content, 'html.parser')

for result in resultsYT.find_all('a'):
     if result.has_attr('href'):
        if '/watch?v=' in result['href']:
          result = result['href']
          videos.append("https://www.youtube.com" + result)

for result in resultsImg.find_all('img'):
     src = result.get('src')
     images.append(src)

for result in resultsQ():
     div = result.find('div', attrs = {'class':'quoteText'})
     try:
        quote.append(div.text)
     except  AttributeError:
        pass
print(quote)

TOKEN = 'NjkxOTg3OTUwNDA1MTU2ODg3.XnrMMQ.p9lslKk-CbUyPSuxr1-AAQDluxc'

client = discord.Client()
embed = discord.Embed()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!SG image'):
        try:
            ranimg = random.choice(images)
            img = embed.set_image(url=ranimg)
            await message.channel.send(embed=img)
        except HTTPException:
            ranimg = random.choice(images)
            img = embed.set_image(url=ranimg)
            await message.channel.send(embed=img)

    elif message.content.startswith('!SG video'):
        ranvid = random.choice(videos)
        await message.channel.send(ranvid)

    elif message.content.startswith('!SG quote'):
        ranquote = random.choice(quote)
        embed = discord.Embed(title="**Selena Gomez Quotes!**", description=ranquote, color=0xfc88ff)
        await message.channel.send(embed = embed)

client.run(TOKEN)