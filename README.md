# CV Evaluator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![LLaMA](https://img.shields.io/badge/LLaMA-3.1-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

CV Evaluator, aday özgeçmişlerini (PDF) kullanıcı tanımlı ve ağırlıklandırılabilir kriterlere göre yerel LLM (LLaMA 3.1) ile analiz eden bir ön eleme sistemidir. Geleneksel anahtar kelime eşleştirmesinin yetersiz kaldığı durumlarda anlamsal analiz yaparak manuel CV tarama yükünü ortadan kaldırır ve nesnel bir uygunluk puanı sunar.

## Özellikler (Features)
- **PDF Metin Çıkarımı:** Yüklenen PDF formatındaki özgeçmişleri otomatik olarak okur ve ayrıştırır.
- **Ağırlıklı Kriter Tanımlama:** İlan gereksinimlerine göre esnek kriterler belirleme ve her kritere önem katsayısı (ağırlık) atama imkânı sunar.
- **Toplu İşleme Desteği:** Birden fazla CV dosyasını eşzamanlı yükleyerek tek oturumda toplu tarama gerçekleştirir.
- **LLM ile Semantik Analiz:** Yerel LLaMA 3.1 modeli ve katı sistem istemi (system prompt) ile adayın niteliklerini anlamsal olarak denetler; düşük sıcaklık (`temperature: 0.1`) değeriyle tutarlı sonuç üretir.
- **Yapılandırılmış Skorlama:** Aday adı, genel eşleşme yüzdesi (%0-100) ve eşleşen kriterleri liste halinde anında raporlar.
- **Gizlilik Odaklı Mimari:** Belgeler üçüncü taraf API'lere gönderilmez; analiz yerel Ollama motoru üzerinden yürütülür ve geçici dosyalar işlem sonrasında silinir.

##  Teknolojiler & Mimari (Tech Stack)
- **Frontend / Backend:** Vanilla JavaScript, HTML5, CSS3 / Python 3.9+, Flask
- **AI / LLM:** Ollama, LLaMA 3.1 (Prompt Engineering, 4K Context Window)
- **Kütüphaneler:** PyPDF2 (PDF Ayrıştırma), Werkzeug (Güvenli Dosya Yönetimi)
- **Mimari / Veri Akışı:** İstemci-Sunucu (Client-Server) MVC mimarisi; PDF ayrıştırma, yerel LLM çıkarımı ve JSON çıktısı üreten veritabanından bağımsız (stateless) boru hattı (pipeline).

##  Kurulum (Getting Started)
```bash
# 1. Depoyu klonlayın
git clone https://github.com/malisevdinoglu/CV-Evulator-in-LLM-.git
cd CV-Evulator-in-LLM-

# 2. Sanal ortam oluşturun ve aktif edin
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate

# 3. Bağımlılıkları yükleyin
pip install flask PyPDF2 ollama werkzeug

# 4. Ollama üzerinde LLaMA 3.1 modelini hazır edin
ollama run llama3.1

# 5. Uygulamayı başlatın
python cv.py
```

Uygulama çalıştıktan sonra tarayıcınızdan `http://localhost:5000` adresine gidin. Sistemin çalışabilmesi için yerel Ollama servisinin arka planda aktif olması gerekmektedir.
