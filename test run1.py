import discord
from discord.ext import commands, tasks
import requests

TOKEN = 'DISCORD TOKEN'
CHANNEL_ID = CHANNEL_ID  # 메시지를 보낼 채널 ID

# 90개 국가의 국기 이모티콘
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
    "United States": "🇺🇸",
    "Vietnam": "🇻🇳",
    "Nigeria": "🇳🇬",
    "Kenya": "🇰🇪",
    "Bangladesh": "🇧🇩",
    "Pakistan": "🇵🇰",
    "Peru": "🇵🇪",
    "Ukraine": "🇺🇦",
    "Venezuela": "🇻🇪",
    "Romania": "🇷🇴",
    "Serbia": "🇷🇸",
    "Croatia": "🇭🇷",
    "Bulgaria": "🇧🇬",
    "Slovakia": "🇸🇰",
    "Slovenia": "🇸🇮",
    "Estonia": "🇪🇪",
    "Lithuania": "🇱🇹",
    "Latvia": "🇱🇻",
    "Luxembourg": "🇱🇺",
    "Cyprus": "🇨🇾",
    "Malta": "🇲🇹",
    "Georgia": "🇬🇪",
    "Azerbaijan": "🇦🇿",
    "Armenia": "🇦🇲",
    "Kazakhstan": "🇰🇿",
    "Uzbekistan": "🇺🇿",
    "Kyrgyzstan": "🇰🇬",
    "Turkmenistan": "🇹🇲",
    "Tajikistan": "🇹🇯",
    "Nepal": "🇳🇵",
    "Sri Lanka": "🇱🇰",
    "Myanmar": "🇲🇲",
    "Laos": "🇱🇦",
    "Cambodia": "🇰🇭",
    "Brunei": "🇧🇳",
    "Mongolia": "🇲🇳",
    "Papua New Guinea": "🇵🇬",
    "Fiji": "🇫🇯",
    "Solomon Islands": "🇸🇧",
    "Vanuatu": "🇻🇺",
    "Samoa": "🇼🇸"
}

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'봇이 준비되었습니다! {bot.user}')
    send_stock.start()  # 봇이 준비되면 반복 작업 시작

@tasks.loop(hours=0.5)  # 0.5시간 마다 반복
async def send_stock():
    try:
        response = requests.get# 스포티 파이 API 국가 체크 사이트('')
        data = response.json()
        stock_message = ""
        for item in data:
            flag = FLAGS.get(item['country'], "")
            stock_message += f"{flag} '{item['country']}', 'slots': {item['slots']},\n"
        stock_message = stock_message.rstrip(",\n") + ""  # 마지막 쉼표와 개행 문자 제거 후 닫는 중괄호 추가
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(stock_message)
    except Exception as e:
        print(f'재고 체크 중 오류 발생: {e}')

bot.run(TOKEN)
