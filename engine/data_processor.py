import json
import html
import os
from datetime import datetime, timezone


def veriyi_json_kaydet(veriler, kaynak, arama_konusu):
    os.makedirs("data", exist_ok=True)

    zaman = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    dosya_adi = f"data/{kaynak.lower()}_{zaman}.json"

    veri_paketi = {
        "kaynak": kaynak,
        "arama_konusu": arama_konusu,
        "toplanma_tarihi": datetime.now(timezone.utc).isoformat(),
        "veri_sayisi": len(veriler),
        "veriler": veriler,
    }

    with open(dosya_adi, "w", encoding="utf-8") as dosya:
        json.dump(
            veri_paketi,
            dosya,
            ensure_ascii=False,
            indent=4,
        )

    print(f"Veriler kaydedildi: {dosya_adi}")

    return dosya_adi


def metni_temizle(metin):
    if not isinstance(metin, str):
        return metin

    temiz_metin = html.unescape(metin)
    temiz_metin = " ".join(temiz_metin.split())

    return temiz_metin