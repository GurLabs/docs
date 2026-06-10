import os

files = {
    # TR Root & Corporate
    "tr/index.mdx": {
        "title": "GurLabs Dokümantasyon",
        "description": "GurLabs premium LeaderOS temaları (OynaTR, Arena) ve özel web proje çözümleri için resmi dokümantasyon ve yardım merkezi.",
        "content": "# GurLabs Dokümantasyonlarına Hoş Geldiniz\n\nProfesyonel web satışı ve premium LeaderOS temaları için ihtiyacınız olan tüm rehberlere buradan ulaşabilirsiniz."
    },
    "tr/kurumsal/biz-kimiz.mdx": {
        "title": "Biz Kimiz? | GurLabs",
        "description": "GurLabs yenilikçi teknoloji stüdyosu hakkında detaylı bilgi edinin. Vizyonumuz, misyonumuz ve profesyonel web satış serüvenimiz.",
        "content": "# Biz Kimiz?\n\nGurLabs; profesyonel web satışı, premium LeaderOS temaları geliştirme ve kurumsal/özel web projeleri üretme alanında faaliyet gösteren yenilikçi bir teknoloji stüdyosudur."
    },
    "tr/kurumsal/ekibimiz.mdx": {
        "title": "Ekibimiz | GurLabs",
        "description": "GurLabs'ın arkasındaki profesyonel tasarımcı ve geliştirici ekibiyle tanışın.",
        "content": "# Ekibimiz\n\nGurLabs'ın profesyonel ürünlerini hayata geçiren ekibimizle tanışın."
    },
    "tr/kurumsal/referanslarimiz.mdx": {
        "title": "Referanslarımız | GurLabs",
        "description": "GurLabs LeaderOS temaları ve özel web projeleri ile hayata geçirdiğimiz başarılı referans müşterilerimiz.",
        "content": "# Referanslarımız\n\nGurLabs ürünlerini güvenle kullanan iş ortaklarımız ve müşterilerimiz."
    },
    "tr/kurumsal/linklerimiz.mdx": {
        "title": "Resmi Bağlantılarımız | GurLabs",
        "description": "GurLabs'a ait tüm resmi web siteleri, satış kanalları, sosyal medya hesapları ve iletişim linkleri.",
        "content": "# Linklerimiz\n\nGurLabs resmi hesap ve bağlantıları."
    },

    # TR OynaTR
    "tr/leaderos/oynatr/tanitim.mdx": {
        "title": "OynaTR Teması Özellikleri ve Tanıtım",
        "description": "GurLabs OynaTR LeaderOS teması: Gelişmiş, minimalist tasarım, modern UI/UX ve premium özellikler. Minecraft web siteniz için en iyi tema.",
        "content": "# OynaTR Teması Tanıtımı\n\nGelişmiş, minimalist ve premium özelliklerle donatılmış web teması."
    },
    "tr/leaderos/oynatr/satin-alma.mdx": {
        "title": "OynaTR Teması Satın Al | GurLabs",
        "description": "OynaTR LeaderOS temasını satın alın. Lisanslama adımları, fiyatlandırma ve satış öncesi detaylar.",
        "content": "# OynaTR Satın Alma\n\nTemanın nasıl satın alınacağı ve lisanslanacağı hakkında bilgiler."
    },
    "tr/leaderos/oynatr/yukleme.mdx": {
        "title": "OynaTR Kurulum Rehberi | LeaderOS",
        "description": "Satın aldığınız OynaTR temasını LeaderOS panelinize adım adım nasıl kuracağınızı anlatan resimli ve detaylı rehber.",
        "content": "# OynaTR Yükleme\n\nOynaTR temasının LeaderOS'a kurulum aşamaları."
    },
    "tr/leaderos/oynatr/ozellestirme.mdx": {
        "title": "OynaTR Tema Özelleştirme | Renk, Logo ve Tasarım",
        "description": "OynaTR temasını kendi markanıza göre özelleştirin. Renk değiştirme, logo ekleme ve ana sayfa düzenleme rehberi.",
        "content": "# OynaTR Özelleştirme\n\nTema renkleri, logoları, menü yapıları ve ana sayfa düzeninin nasıl değiştirileceği."
    },
    "tr/leaderos/oynatr/kullanma.mdx": {
        "title": "OynaTR Yönetimi ve Kullanım Kılavuzu",
        "description": "OynaTR LeaderOS temasının günlük kullanımı, widget yönetimi, duyurular ve operasyonel ayarları.",
        "content": "# OynaTR Kullanma\n\nTemanın günlük yönetimi, widget kullanımı, duyuru ekleme gibi operasyonel detaylar."
    },
    "tr/leaderos/oynatr/iletisim.mdx": {
        "title": "OynaTR Teknik Destek ve İletişim",
        "description": "OynaTR teması için teknik destek talebi oluşturun. GurLabs destek ekibine 7/24 ulaşın.",
        "content": "# OynaTR İletişim\n\nDestek talepleri ve satış sonrası doğrudan GurLabs ekibine ulaşma kanalları."
    },

    # TR Arena
    "tr/leaderos/arena/tanitim.mdx": {
        "title": "Arena Teması Özellikleri ve Tanıtım",
        "description": "GurLabs Arena LeaderOS teması: Oyuncu ve topluluk odaklı, dinamik, agresif ve modern premium web teması.",
        "content": "# Arena Teması Tanıtımı\n\nModern, dinamik ve oyuncu/topluluk odaklı web teması."
    },
    "tr/leaderos/arena/satin-alma.mdx": {
        "title": "Arena Teması Satın Al | GurLabs",
        "description": "Arena LeaderOS temasını güvenle satın alın. Kurumsal satış, fiyatlar ve lisans detayları.",
        "content": "# Arena Satın Alma\n\nTemanın satın alınması ve lisanslama süreçleri."
    },
    "tr/leaderos/arena/yukleme.mdx": {
        "title": "Arena Kurulum Rehberi | LeaderOS",
        "description": "Arena temasının LeaderOS altyapısına sorunsuz kurulumu. Adım adım FTP yükleme ve panel ayarları.",
        "content": "# Arena Yükleme\n\nArena temasının kurulum adımları."
    },
    "tr/leaderos/arena/ozellestirme.mdx": {
        "title": "Arena Tema Özelleştirme | Renk, Logo ve Tasarım",
        "description": "Arena temasını projenize göre özelleştirin. Dinamik renk paletleri, görsel değişiklikler ve sayfa yapılandırması.",
        "content": "# Arena Özelleştirme\n\nTema görünümünü kendi markanıza göre şekillendirme rehberi."
    },
    "tr/leaderos/arena/kullanma.mdx": {
        "title": "Arena Yönetimi ve Kullanım Kılavuzu",
        "description": "Arena LeaderOS temasının panel üzerinden kullanımı. İçerik girme, ayarları düzenleme.",
        "content": "# Arena Kullanma\n\nTemanın yönetim paneli üzerinden operasyonel kullanımı."
    },
    "tr/leaderos/arena/iletisim.mdx": {
        "title": "Arena Teknik Destek ve İletişim",
        "description": "Arena teması için profesyonel destek hizmeti. GurLabs ile iletişime geçin.",
        "content": "# Arena İletişim\n\nDestek talepleri ve iletişim kanalları."
    },

    # TR Ozel Projeler
    "tr/ozel-projeler/talep.mdx": {
        "title": "Özel Kurumsal Web Projesi Talebi | GurLabs",
        "description": "GurLabs profesyonel ekibiyle sıfırdan kurumsal ve e-ticaret odaklı web projeleri geliştirin. Fiyat teklifi ve talep formu.",
        "content": "# Özel Proje Talebi\n\nİhtiyaçlarınıza göre sıfırdan geliştirilen özel web tasarımları ve çözümleri."
    },
    "tr/ozel-projeler/sureclerimiz.mdx": {
        "title": "Proje Geliştirme Süreçlerimiz | GurLabs",
        "description": "GurLabs'ta özel web projesi nasıl geliştirilir? Tasarım, yazılım, test ve yayına alma aşamalarımız.",
        "content": "# Süreçlerimiz\n\nSıfırdan projeleri nasıl tasarlıyor ve hayata geçiriyoruz?"
    },

    # EN Root & Corporate
    "en/index.mdx": {
        "title": "GurLabs Documentation",
        "description": "Official documentation and help center for GurLabs premium LeaderOS themes (OynaTR, Arena) and custom web project solutions.",
        "content": "# Welcome to GurLabs Documentation\n\nFind all the guides you need for professional web sales and premium LeaderOS themes."
    },
    "en/corporate/about-us.mdx": {
        "title": "About Us | GurLabs",
        "description": "Learn more about GurLabs, an innovative tech studio. Our vision, mission, and journey in professional web sales.",
        "content": "# About Us\n\nGurLabs is an innovative tech studio operating in professional web sales, premium LeaderOS theme development, and custom web projects."
    },
    "en/corporate/our-team.mdx": {
        "title": "Our Team | GurLabs",
        "description": "Meet the professional designers and developers behind GurLabs.",
        "content": "# Our Team\n\nMeet the team that brings GurLabs' professional products to life."
    },
    "en/corporate/references.mdx": {
        "title": "Our References | GurLabs",
        "description": "Successful reference clients and partners using GurLabs LeaderOS themes and custom web projects.",
        "content": "# Our References\n\nPartners and clients who trust GurLabs products."
    },
    "en/corporate/links.mdx": {
        "title": "Official Links | GurLabs",
        "description": "All official GurLabs websites, sales channels, social media accounts, and contact links.",
        "content": "# Our Links\n\nGurLabs official accounts and connections."
    },

    # EN OynaTR
    "en/leaderos/oynatr/introduction.mdx": {
        "title": "OynaTR Theme Features & Introduction",
        "description": "GurLabs OynaTR LeaderOS theme: Advanced, minimalist design, modern UI/UX, and premium features. The best theme for your Minecraft website.",
        "content": "# OynaTR Theme Introduction\n\nAn advanced, minimalist web theme equipped with premium features."
    },
    "en/leaderos/oynatr/purchasing.mdx": {
        "title": "Buy OynaTR Theme | GurLabs",
        "description": "Purchase the OynaTR LeaderOS theme. Licensing steps, pricing, and pre-sales details.",
        "content": "# Purchasing OynaTR\n\nInformation on how to purchase and license the theme."
    },
    "en/leaderos/oynatr/installation.mdx": {
        "title": "OynaTR Installation Guide | LeaderOS",
        "description": "Step-by-step illustrated and detailed guide on how to install your purchased OynaTR theme on your LeaderOS panel.",
        "content": "# Installing OynaTR\n\nInstallation steps for the OynaTR theme on LeaderOS."
    },
    "en/leaderos/oynatr/customization.mdx": {
        "title": "OynaTR Theme Customization | Colors & Design",
        "description": "Customize the OynaTR theme for your brand. Color changing, logo adding, and home page layout guide.",
        "content": "# Customizing OynaTR\n\nHow to change theme colors, logos, menus, and home page layouts."
    },
    "en/leaderos/oynatr/usage.mdx": {
        "title": "OynaTR Management and Usage Guide",
        "description": "Daily usage of the OynaTR LeaderOS theme, widget management, announcements, and operational settings.",
        "content": "# Using OynaTR\n\nOperational details like daily management, widget usage, and announcements."
    },
    "en/leaderos/oynatr/contact.mdx": {
        "title": "OynaTR Technical Support & Contact",
        "description": "Create a technical support request for the OynaTR theme. Contact GurLabs support 24/7.",
        "content": "# OynaTR Contact\n\nSupport requests and direct communication channels with the GurLabs team."
    },

    # EN Arena
    "en/leaderos/arena/introduction.mdx": {
        "title": "Arena Theme Features & Introduction",
        "description": "GurLabs Arena LeaderOS theme: Player and community focused, dynamic, aggressive, and modern premium web theme.",
        "content": "# Arena Theme Introduction\n\nA modern, dynamic, and community-focused web theme."
    },
    "en/leaderos/arena/purchasing.mdx": {
        "title": "Buy Arena Theme | GurLabs",
        "description": "Securely purchase the Arena LeaderOS theme. Corporate sales, pricing, and license details.",
        "content": "# Purchasing Arena\n\nPurchasing and licensing processes for the theme."
    },
    "en/leaderos/arena/installation.mdx": {
        "title": "Arena Installation Guide | LeaderOS",
        "description": "Seamless installation of the Arena theme on LeaderOS. Step-by-step FTP upload and panel settings.",
        "content": "# Installing Arena\n\nInstallation steps for the Arena theme."
    },
    "en/leaderos/arena/customization.mdx": {
        "title": "Arena Theme Customization | Colors & Design",
        "description": "Customize the Arena theme for your project. Dynamic color palettes, visual changes, and page configuration.",
        "content": "# Customizing Arena\n\nGuide to shaping the theme appearance according to your brand."
    },
    "en/leaderos/arena/usage.mdx": {
        "title": "Arena Management and Usage Guide",
        "description": "Usage of the Arena LeaderOS theme via the panel. Entering content, editing settings.",
        "content": "# Using Arena\n\nOperational usage of the theme via the management panel."
    },
    "en/leaderos/arena/contact.mdx": {
        "title": "Arena Technical Support & Contact",
        "description": "Professional support service for the Arena theme. Contact GurLabs.",
        "content": "# Arena Contact\n\nSupport requests and contact channels."
    },

    # EN Custom Projects
    "en/custom-projects/request.mdx": {
        "title": "Custom Corporate Web Project Request | GurLabs",
        "description": "Develop custom corporate and e-commerce web projects from scratch with GurLabs' professional team. Quote and request form.",
        "content": "# Custom Project Request\n\nCustom web designs and solutions developed from scratch according to your needs."
    },
    "en/custom-projects/process.mdx": {
        "title": "Our Project Development Process | GurLabs",
        "description": "How is a custom web project developed at GurLabs? Our design, software, testing, and deployment stages.",
        "content": "# Our Process\n\nHow do we design and bring projects to life from scratch?"
    }
}

for path, data in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"---\ntitle: \"{data['title']}\"\ndescription: \"{data['description']}\"\n---\n\n{data['content']}")

print("All files created successfully with SEO tags.")
