import json
import os

from dotenv import load_dotenv
from google import genai


load_dotenv(override=True)


def gemini_analiz_yap(veriler):
    api_anahtari = os.getenv("GEMINI_API_KEY")

    if not api_anahtari:
        raise ValueError("GEMINI_API_KEY bulunamadı.")

    client = genai.Client(api_key=api_anahtari)

    veri_metni = json.dumps(
        veriler,
        ensure_ascii=False,
        indent=2,
    )

    prompt = f"""
Sen bir sosyal medya araştırma analistisin.

Aşağıda sosyal medya kaynaklarından toplanmış yapılandırılmış veriler
bulunuyor.

Görevin:
1. Ana konuları belirle.
2. Tekrar eden görüşleri belirle.
3. Kullanıcıların dikkat çektiği sorunları belirle.
4. Öne çıkan olumlu ve olumsuz görüşleri ayır.
5. Dikkat çeken eğilimleri belirt.
6. Verilerde yeterli kanıt olmayan noktaları kesin gerçek gibi sunma.

Sonucu Türkçe ve düzenli bir araştırma analizi olarak hazırla.

VERİLER:
{veri_metni}
"""

    yanit = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )

    analiz = yanit.text

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/gemini_analiz.json",
        "w",
        encoding="utf-8",
    ) as dosya:
        json.dump(
            {
                "model": "Gemini",
                "gorev": "Sosyal medya trend analizi",
                "analiz": analiz,
            },
            dosya,
            ensure_ascii=False,
            indent=4,
        )

    print("Gemini analizi oluşturuldu.")
    print("Rapor: reports/gemini_analiz.json")

    return analiz