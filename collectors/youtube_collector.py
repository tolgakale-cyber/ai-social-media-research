import os

from dotenv import load_dotenv
from googleapiclient.discovery import build


load_dotenv()


def youtube_verilerini_topla(arama_konusu):
    api_anahtari = os.getenv("YOUTUBE_API_KEY")

    if not api_anahtari:
        raise ValueError("YOUTUBE_API_KEY bulunamadı.")

    youtube = build(
        "youtube",
        "v3",
        developerKey=api_anahtari,
    )

    print(f"YouTube araştırması başlatılıyor: {arama_konusu}")

    istek = youtube.search().list(
        part="snippet",
        q=arama_konusu,
        type="video",
        maxResults=5,
    )

    yanit = istek.execute()

    veriler = []

    for oge in yanit.get("items", []):
        snippet = oge["snippet"]

        veriler.append(
            {
                "video_id": oge["id"]["videoId"],
                "başlık": snippet["title"],
                "kanal": snippet["channelTitle"],
                "yayın_tarihi": snippet["publishedAt"],
                "açıklama": snippet["description"],
            }
        )

    return veriler
def youtube_yorumlarini_topla(video_id, maksimum_yorum=10):
    api_anahtari = os.getenv("YOUTUBE_API_KEY")

    if not api_anahtari:
        raise ValueError("YOUTUBE_API_KEY bulunamadı.")

    youtube = build(
        "youtube",
        "v3",
        developerKey=api_anahtari,
    )

    istek = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=maksimum_yorum,
        order="relevance",
        textFormat="plainText",
    )

    yanit = istek.execute()

    yorumlar = []

    for oge in yanit.get("items", []):
        yorum = oge["snippet"]["topLevelComment"]["snippet"]

        yorumlar.append(
            {
                "yorum": yorum["textDisplay"],
                "beğeni": yorum["likeCount"],
                "yayın_tarihi": yorum["publishedAt"],
            }
        )

    return yorumlar