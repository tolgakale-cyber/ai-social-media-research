from engine.config import SEKTÖR, VERİ_KAYNAKLARI, YAPAY_ZEKÂ_MODELLERİ
from collectors.youtube_collector import youtube_verilerini_topla
from engine.data_processor import veriyi_json_kaydet


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

    veriyi_json_kaydet(
        youtube_verileri,
        kaynak="YouTube",
        arama_konusu=SEKTÖR,
    )

    print("\nAraştırma verileri başarıyla hazırlandı.")


if __name__ == "__main__":
    main()