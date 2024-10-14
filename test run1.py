import discord
from discord.ext import commands, tasks
import requests
import os

TOKEN = 'DISCORD_TOKEN'
CHANNEL_ID = DISCORD_CHANNEL_ID  # 메시지를 보낼 채널 ID

# 90개 국가의 국기 이모티콘 (flags dictionary)
FLAGS = {
    "Argentina": "🇦🇷",
    "Australia": "🇦🇺",
    "Austria": "🇦🇹",
    "Belgium": "🇧🇪",
    "Brazil": "🇧🇷",
    "Canada": "🇨🇦",
    "Chile": "🇨🇱",
    "China": "🇨🇳",
    "Colombia": "🇨🇴",
    "Czech Republic": "🇨🇿",
    "Czechia": "🇨🇿",
    "Denmark": "🇩🇰",
    "Dominican Republic": "🇩🇴",
    "Ecuador": "🇪🇨",
    "Egypt": "🇪🇬",
    "Finland": "🇫🇮",
    "France": "🇫🇷",
    "Germany": "🇩🇪",
    "Greece": "🇬🇷",
    "Hong Kong": "🇭🇰",
    "Hungary": "🇭🇺",
    "Iceland": "🇮🇸",
    "India": "🇮🇳",
    "Indonesia": "🇮🇩",
    "Ireland": "🇮🇪",
    "Israel": "🇮🇱",
    "Italy": "🇮🇹",
    "Japan": "🇯🇵",
    "Malaysia": "🇲🇾",
    "Mexico": "🇲🇽",
    "Netherlands": "🇳🇱",
    "New Zealand": "🇳🇿",
    "Norway": "🇳🇴",
    "Philippines": "🇵🇭",
    "Poland": "🇵🇱",
    "Portugal": "🇵🇹",
    "Russia": "🇷🇺",
    "Saudi Arabia": "🇸🇦",
    "Singapore": "🇸🇬",
    "South Africa": "🇿🇦",
    "South Korea": "🇰🇷",
    "Spain": "🇪🇸",
    "Sweden": "🇸🇪",
    "Switzerland": "🇨🇭",
    "Taiwan": "🇹🇼",
    "Thailand": "🇹🇭",
    "Turkey": "🇹🇷",
    "United Kingdom": "🇬🇧",
    "United States": "🇺🇸트('')
        response.raise_for_status()  # 잘못된 응답에 대해 예외 발생
        data = response.json()
        stock_message = ""
        for item in data:
            flag = FLAGS.get(item['country'], "")
            stock_message += f"{flag} '{item['country']}', 'slots': {item['slots']},\n"
        return stock_message.rstrip(",\n")  # 마지막 쉼표와 개행 문자 제거
    except requests.RequestException as e:
        print(f'API 요청 중 오류 발생: {e}')
        return None

@bot.event
async def on_message(message):
    # 봇 자신이 보낸 메시지는 무시
    if message.author == bot.user:
        return

    # 멘션된 경우
    if bot.user in message.mentions:
        stock_message = await fetch_stock_data()
        if stock_message:
            await message.channel.send(stock_message)
        else:
            await message.channel.send('재고를 확인하는 중 오류가 발생했습니다.')

bot.run(TOKEN)
