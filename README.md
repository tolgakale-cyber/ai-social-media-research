\# AI Social Media Research Automation



YouTube içeriklerini ve kullanıcı yorumlarını otomatik olarak toplayan, verileri temizleyip yapılandıran, ChatGPT ve Gemini ile çoklu-model analiz gerçekleştiren ve model bulgularını sentezleyerek final araştırma raporuna dönüştüren uçtan uca bir AI otomasyon sistemi.



\## Proje Amacı



Bu projeyi, sosyal medya üzerindeki içerik ve kullanıcı görüşlerini manuel olarak incelemek yerine otomatik bir araştırma iş akışı oluşturmak amacıyla geliştirdim.



Sistem YouTube üzerinden araştırma verilerini toplar, verileri temizler ve yapılandırır, iki farklı yapay zekâ modeliyle analiz eder ve bu analizleri tek bir araştırma sentezinde birleştirir.



\## Sistem Mimarisi



```text

Araştırma Konusu

&#x20;      ↓

YouTube Data API

&#x20;      ↓

Video + Yorum Toplama

&#x20;      ↓

Veri Temizleme

&#x20;      ↓

Yapılandırılmış JSON

&#x20;      ↓

┌─────────────────┬─────────────────┐

│    ChatGPT      │     Gemini      │

│    Analizi      │     Analizi     │

└────────┬────────┴────────┬────────┘

&#x20;        ↓

&#x20;  Çoklu-Model Sentezi

&#x20;        ↓

Final Araştırma Raporu

```



\## Özellikler



\- YouTube Data API üzerinden video araştırması

\- Videolara ait kullanıcı yorumlarının otomatik toplanması

\- Toplanan metinlerin temizlenmesi

\- Araştırma verilerinin yapılandırılmış JSON formatında saklanması

\- OpenAI API ile ChatGPT tabanlı araştırma analizi

\- Gemini API ile ikinci bağımsız araştırma analizi

\- İki modelin bulgularını karşılaştıran çoklu-model sentez katmanı

\- Ortak bulguların ve farklılaşan noktaların belirlenmesi

\- Olumlu ve olumsuz kullanıcı görüşlerinin ayrıştırılması

\- Veri sınırlılıklarının sentez raporunda belirtilmesi

\- Analizlerin ve sentezin final araştırma raporunda birleştirilmesi



\## Kullanılan Teknolojiler



\- Python

\- YouTube Data API

\- OpenAI API

\- Gemini API

\- JSON

\- python-dotenv

\- Git / GitHub



\## Proje Yapısı



```text

ai-social-media-research/

│

├── app.py

├── collectors/

│   └── youtube\_collector.py

│

├── engine/

│   ├── ai\_analyzer.py

│   ├── config.py

│   ├── data\_processor.py

│   ├── gemini\_analyzer.py

│   ├── report\_generator.py

│   └── synthesis\_analyzer.py

│

├── data/

├── reports/

├── .env

├── .gitignore

└── README.md

```



`data/`, `reports/` ve `.env` çalışma sırasında yerel olarak kullanılır ve Git deposuna dahil edilmez.



\## Çalışma Akışı



1\. Araştırma konusu belirlenir.

2\. YouTube Data API üzerinden ilgili videolar bulunur.

3\. Video bilgileri ve kullanıcı yorumları toplanır.

4\. Metin verileri temizlenir ve JSON formatında saklanır.

5\. Veriler ChatGPT tarafından analiz edilir.

6\. Aynı veriler Gemini tarafından bağımsız olarak analiz edilir.

7\. İki modelin analizleri çoklu-model sentez katmanında karşılaştırılır.

8\. ChatGPT analizi, Gemini analizi ve sentez sonucu final araştırma raporunda birleştirilir.



\## Çıktılar



Sistem çalışma sırasında aşağıdaki araştırma çıktılarının oluşturulmasını destekler:



```text

data/youtube\_TIMESTAMP.json



reports/chatgpt\_analiz.json

reports/gemini\_analiz.json

reports/sentez\_analizi.json

reports/final\_rapor\_TIMESTAMP.json

```



Bu dosyalar ham araştırma verisinden nihai sentez raporuna kadar sürecin farklı aşamalarını temsil eder.



\## Güvenlik



API anahtarları `.env` dosyasında tutulur ve `.gitignore` aracılığıyla Git deposunun dışında bırakılır.



Örnek ortam değişkenleri:



```text

YOUTUBE\_API\_KEY=...

OPENAI\_API\_KEY=...

GEMINI\_API\_KEY=...

```



Gerçek API anahtarları repository içerisinde paylaşılmamalıdır.



\## Geliştirici



\*\*Tolga Kale\*\*



GitHub: `tolgakale-cyber`

