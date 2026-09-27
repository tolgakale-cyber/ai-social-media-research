import json
import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv(override=True)


def sentez_analizi_yap(chatgpt_analiz, gemini_analiz):
    api_anahtari = os.getenv("OPENAI_API_KEY")

    if not api_anahtari:
        raise ValueError("OPENAI_API_KEY bulunamadı.")

    client = OpenAI(api_key=api_anahtari)

    prompt = f"""
Sen bir araştırma sentez analistisin.

Aynı sosyal medya verisi iki farklı yapay zekâ modeli tarafından
analiz edildi.

Görevin bu iki analizi karşılaştırmak ve tek, tutarlı bir araştırma
sonucu oluşturmaktır.

Kurallar:
1. İki modelin ortak bulgularını belirle.
2. Modellerin farklılaştığı noktaları belirt.
3. Öne çıkan ana konuları ve eğilimleri özetle.
4. Kullanıcıların olumlu ve olumsuz görüşlerini ayır.
5. Dikkat çeken sorunları belirt.
6. Verilerin sınırlılıklarını açıkça belirt.
7. Analizlerde yeterli kanıt olmayan iddiaları kesin gerçek gibi sunma.
8. Yeni bilgi uydurma; yalnızca verilen iki analize dayan.
9. Sonucu Türkçe ve profesyonel bir araştırma raporu biçiminde hazırla.

CHATGPT ANALİZİ:
{chatgpt_analiz}

GEMINI ANALİZİ:
{gemini_analiz}
"""

    yanit = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt,
    )

    sentez = yanit.output_text

    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/sentez_analizi.json",
        "w",
        encoding="utf-8",
    ) as dosya:
        json.dump(
            {
                "gorev": "Çoklu model araştırma sentezi",
                "kaynak_modeller": ["ChatGPT", "Gemini"],
                "sentez": sentez,
            },
            dosya,
            ensure_ascii=False,
            indent=4,
        )

    print("Çoklu model sentez analizi oluşturuldu.")
    print("Rapor: reports/sentez_analizi.json")

    return sentez