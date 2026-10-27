import discord
from discord.ext import commands
import random
import os

# BOT AYARLARI
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# SPOR TARIHI OLAYLARI
olaylar = [
    {
        "spor": "Basketbol",
        "yil": 1992,
        "baslik": "ABD Rüya Takimi",
        "aciklama": (
            "ABD, Barcelona Olimpiyatlari'nda basketbolda altin madalya "
            "kazandi."
        )
    },
    {
        "spor": "Basketbol",
        "yil": 1998,
        "baslik": "Chicago Bulls sampiyonlugu",
        "aciklama": (
            "Chicago Bulls, NBA Finalleri'nde Utah Jazz'i yenerek "
            "sampiyon oldu."
        )
    },
    {
        "spor": "Futbol",
        "yil": 2022,
        "baslik": "Arjantin Dünya Kupasi sampiyonu",
        "aciklama": (
            "Arjantin, finalde Fransa'yi penalti atislari sonucunda "
            "yenerek kupayi kazandi."
        )
    },
    {
        "spor": "Olimpiyatlar",
        "yil": 2008,
        "baslik": "Usain Bolt'un rekoru",
        "aciklama": (
            "Usain Bolt, Pekin Olimpiyatlari'nda 100 metreyi 9.69 "
            "saniyede kosarak dunya rekoru kirdi."
        )
    },
    {
        "spor": "Formula 1",
        "yil": 2021,
        "baslik": "Verstappen'in ilk sampiyonlugu",
        "aciklama": (
            "Max Verstappen, Abu Dhabi Grand Prix'sini kazanarak "
            "ilk Formula 1 dunya sampiyonlugunu aldi."
        )
    },
    {
        "spor": "Tenis",
        "yil": 2022,
        "baslik": "Nadal'in Avustralya Açik sampiyonlugu",
        "aciklama": (
            "Rafael Nadal, finalde Daniil Medvedev'i yenerek "
            "Avustralya Açik'i kazandi."
        )
    },
    {
        "spor": "Voleybol",
        "yil": 2023,
        "baslik": "Türkiye Avrupa sampiyonu",
        "aciklama": (
            "Türkiye A Milli Kadin Voleybol Takimi, ilk kez "
            "Avrupa sampiyonlugunu kazandi."
        )
    }
]


@bot.event
async def on_ready():
    print(f"Bot giris yapti: {bot.user}")
    print(f"Toplam spor olayi: {len(olaylar)}")
    print("Komutlari kullanmaya hazir!")


@bot.command()
async def olay(ctx, *, kategori=None):

    bulunan_olaylar = olaylar

    if kategori:
        bulunan_olaylar = [
            bilgi
            for bilgi in olaylar
            if bilgi["spor"].casefold() == kategori.casefold()
        ]

    if not bulunan_olaylar:
        kategoriler = sorted({
            bilgi["spor"]
            for bilgi in olaylar
        })

        await ctx.send(
            "Bu kategoride olay bulamadim.\n"
            "Mevcut kategoriler: " + ", ".join(kategoriler)
        )
        return

    secilen_olay = random.choice(bulunan_olaylar)

    await ctx.send(
        f"🏆 {secilen_olay['baslik']}\n"
        f"Spor: {secilen_olay['spor']}\n"
        f"Yil: {secilen_olay['yil']}\n"
        f"Aciklama: {secilen_olay['aciklama']}"
    )


@bot.command()
async def yardim(ctx):
    await ctx.send(
        "**Spor Tarihi Merkezi - Yardim**\n\n"
        "`!olay` - Rastgele bir spor tarihi olayi gosterir.\n"
        "`!olay Basketbol` - Basketbol olayi gosterir.\n"
        "`!olay Futbol` - Futbol olayi gosterir.\n"
        "`!olay Tenis` - Tenis olayi gosterir.\n"
        "`!olay Formula 1` - Formula 1 olayi gosterir.\n"
        "`!olay Olimpiyatlar` - Olimpiyat olayi gosterir.\n"
        "`!olay Voleybol` - Voleybol olayi gosterir."
    )


token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError(
        "DISCORD_TOKEN bulunamadi. "
        "PowerShell terminalinde tokeni ayarlamalisin."
    )

bot.run(token)
