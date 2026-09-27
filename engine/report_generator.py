import json
import os
from datetime import datetime, timezone


def final_rapor_olustur(
    analiz,
    kaynak,
    arama_konusu,
    veri_sayisi,
):
    os.makedirs("reports", exist_ok=True)

    zaman = datetime.now(timezone.utc)

    rapor = {
        "rapor_turu": "AI Sosyal Medya Araştırma Raporu",
        "sektor": arama_konusu,
        "veri_kaynagi": kaynak,
        "analiz_modeli": "Gemini",
        "veri_sayisi": veri_sayisi,
        "olusturulma_tarihi": zaman.isoformat(),
        "analiz": analiz,
    }

    dosya_adi = (
        f"reports/final_rapor_"
        f"{zaman.strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(
        dosya_adi,
        "w",
        encoding="utf-8",
    ) as dosya:
        json.dump(
            rapor,
            dosya,
            ensure_ascii=False,
            indent=4,
        )

    print(f"Final araştırma raporu oluşturuldu: {dosya_adi}")

    return dosya_adi