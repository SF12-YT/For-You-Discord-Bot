import discord
from bs4 import BeautifulSoup
import requests
import collections
import random
import os

images = []
videos = []
quote = []
songs = ["Winter Wonderland", "Kiss & Tell", "I Won't Apologize", "Falling Down", "I Promise You", "Crush", "Naturally", "The Way I Loved You", "More", "As a Blonde", "I Don't Miss You at All", "Stop & Erase", "I Got U", "Tell Me Something I Don't Know", "New Classic", "Magic", "Send It On", "Whoa Oh! (Me vs. Everyone) (Remix)", "One and the Same", "Round & Round", "A Year Without Rain", "Rock God", "Off the Chain", "Summer's Not Hot", "Intuition", "Spotlight", "Ghost of You", "Sick of You", "Live Like There's No Tomorrow", "Un Año Sin Lluvia", "Who Says", "Dices", "Love You Like a Love Song", "Bang Bang Bang", "We Own the Night", "Hit the Lights", "Whiplash", "When the Sun Goes Down", "My Dilemma", "That's More Like It", "Outlaw", "Middle of Nowhere", "Fantasma de Amor", "Shake It Up", "Come & Get It", "Slow Down", "Birthday", "Stars Dance", "Like a Champion", "Forget Forever", "Save the Day", "B.E.A.T.", "Write Your Name", "Undercover", "Love Will Remember", "Nobody Does It Like You", "Music Feels Better", "Lover in Me", "I Like It That Way", "The Heart Wants What It Wants", "Bidi Bidi Bom Bom", "Do It", "I Want You to Know", "Good for You", "Same Old Love", "Revival", "Kill Em with Kindness", "We Don't Talk Anymore", "Hands", "Trust Nobody", "Hands to Myself", "Sober", "Camouflage", "Me & the Rhythm", "Survivors", "Body Heat", "Rise", "Me & My Girls", "Nobody", "Perfect", "Outta My Hands (Loco)", "Cologne", "It Ain't Me", "Only You", "Bad Liar", "Fetish", "Wolves", "Back to You", "Taki Taki", "I Can't Get Enough", "Anxiety", "Lose You to Love Me", "Look at Her Now", "Rare", "Dance Again", "Ring", "Vulnerable", "People You Know", "Let Me Get Me", "Crowded Room", "Kinda Crazy", "Fun", "Cut You Off", "A Sweeter Place", "Feel Me"]
albums = ["Kiss & Tell", "A Year Without Rain", "When the Sun Goes Down", "Stars Dance", "Revival", "Rare"]

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

TOKEN = os.environ['TOKEN']

client = discord.Client()
emb = discord.Embed()

@client.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name="!SG help", type=2))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!SG pic'):
        try:
            ranimg = random.choice(images)
            img = emb.set_image(url=ranimg)
            await message.channel.send(embed=img)
        except discord.errors.HTTPException:
            ranimg = random.choice(images)
            img = emb.set_image(url=ranimg)
            await message.channel.send(embed=img)
            
    elif message.content.startswith('!SG Pic'):
        try:
            ranimg = random.choice(images)
            img = emb.set_image(url=ranimg)
            await message.channel.send(embed=img)
        except discord.errors.HTTPException:
            ranimg = random.choice(images)
            img = emb.set_image(url=ranimg)
            await message.channel.send(embed=img)

    elif message.content.startswith('!SG video'):
        ranvid = random.choice(videos)
        await message.channel.send(ranvid)
        
    elif message.content.startswith('!SG Video'):
        ranvid = random.choice(videos)
        await message.channel.send(ranvid)

    elif message.content.startswith('!SG quote'):
        ranquote = random.choice(quote)
        embed = discord.Embed(title="**Selena Gomez Quotes!**", description=ranquote, color=0xfc88ff)
        await message.channel.send(embed = embed)
        
    elif message.content.startswith('!SG Quote'):
        ranquote = random.choice(quote)
        embed = discord.Embed(title="**Selena Gomez Quotes!**", description=ranquote, color=0xfc88ff)
        await message.channel.send(embed = embed)

    elif message.content.startswith('!SG song'):
        ransng = random.choice(songs)
        await message.channel.send(ransng)
        
    elif message.content.startswith('!SG Song'):
        ransng = random.choice(songs)
        await message.channel.send(ransng)

    elif message.content.startswith('!SG album'):
        ranalb = random.choice(albums)
        await message.channel.send(ranalb)
        
    elif message.content.startswith('!SG Album'):
        ranalb = random.choice(albums)
        await message.channel.send(ranalb)
        
    elif message.content.startswith('!SG help'):
        embed = discord.Embed(title="**Commands Help!**", description="**Every command starts with an !SG** \n Use *video* to get a **Selena Gomez video** \n Use *quote* to get a **Selena Gomez quote** \n Use *song* to get a **Selena Gomez song** \n Use *album* to get a **Selena Gomez album**", color=0xfc88ff)
        await message.channel.send(embed = embed)

    elif message.content.startswith('!SG Help'):
        embed = discord.Embed(title="**Commands Help!**", description="**Every command starts with an !SG** \n Use *video* to get a **Selena Gomez video** \n Use *quote* to get a **Selena Gomez quote** \n Use *song* to get a **Selena Gomez song** \n Use *album* to get a **Selena Gomez album**", color=0xfc88ff)
        await message.channel.send(embed = embed)
  
client.run(TOKEN)
