from engine.config import SEKTÖR, VERİ_KAYNAKLARI, YAPAY_ZEKÂ_MODELLERİ
from collectors.youtube_collector import (
    youtube_verilerini_topla,
    youtube_yorumlarini_topla,
)
from engine.data_processor import veriyi_json_kaydet, metni_temizle
from engine.gemini_analyzer import gemini_analiz_yap


def main():
    print("AI Social Media Research Automation")
    print(f"Sektör: {SEKTÖR}")

    print("\nVeri kaynakları:")
    for kaynak in VERİ_KAYNAKLARI:
        print(f"- {kaynak}")

    print("\nYapay zekâ modelleri:")
    for model in YAPAY_ZEKÂ_MODELLERİ:
        print(f"- {model}")

    print("\nYouTube verileri toplanıyor...")

    youtube_verileri = youtube_verilerini_topla(SEKTÖR)

    print(f"Toplanan YouTube videosu: {len(youtube_verileri)}")

       

    for video in youtube_verileri:
        video["başlık"] = metni_temizle(video["başlık"])
        video["açıklama"] = metni_temizle(video["açıklama"])

        video_id = video["video_id"]

        try:
            yorumlar = youtube_yorumlarini_topla(
                video_id,
                maksimum_yorum=10,
            
            )
            for yorum in yorumlar:
                yorum["yorum"] = metni_temizle(yorum["yorum"])
        except Exception as hata:
            print(
                f"Yorumlar alınamadı: "
                f"{video['başlık']} - {hata}"
            )
            yorumlar = []

        video["yorumlar"] = yorumlar

        print(
            f"Yorum toplandı: "
            f"{video['başlık']} ({len(yorumlar)})"
        )

    veriyi_json_kaydet(
        youtube_verileri,
        kaynak="YouTube",
        arama_konusu=SEKTÖR,
    )

    print("\nYouTube araştırma verileri başarıyla hazırlandı.")

    print("\nGemini analizi başlatılıyor...")

    try:
        gemini_analiz_yap(youtube_verileri)
        print("Gemini araştırma analizi başarıyla tamamlandı.")
    except Exception as hata:
        print(f"Gemini analizi yapılamadı: {hata}")

if __name__ == "__main__":
    main()