import os

files = {
    # TR Root & Corporate
    "tr/index.mdx": {
        "title": "GurLabs Dokümantasyon",
        "description": "GurLabs premium LeaderOS temaları (OynaTR, Arena) ve özel web proje çözümleri için resmi dokümantasyon ve yardım merkezi.",
        "content": """# GurLabs Dokümantasyon Merkezine Hoş Geldiniz! 🚀

GurLabs olarak, profesyonel web satışı, premium LeaderOS temaları geliştirme ve kurumsal/özel web projeleri üretme konusunda yenilikçi bir teknoloji stüdyosuyuz.

Aradığınız tüm rehberleri, kurulum aşamalarını ve destek belgelerini burada bulabilirsiniz.

## Hizmetlerimiz

<CardGroup cols={2}>
  <Card title="OynaTR Teması" icon="gamepad" href="/tr/leaderos/oynatr/tanitim">
    Gelişmiş, minimalist ve premium özelliklerle donatılmış en popüler LeaderOS temamız.
  </Card>
  <Card title="Arena Teması" icon="swords" href="/tr/leaderos/arena/tanitim">
    Modern, dinamik ve tamamen topluluk odaklı, iddialı web temamız.
  </Card>
  <Card title="Özel Web Projeleri" icon="code" href="/tr/ozel-projeler/talep">
    İhtiyaçlarınıza özel, sıfırdan geliştirilen kurumsal ve modern e-ticaret projeleri.
  </Card>
  <Card title="Mağaza" icon="shop" href="https://shop.gurlabs.xyz">
    Tüm GurLabs ürünlerine resmi mağazamız üzerinden anında ulaşın.
  </Card>
</CardGroup>

<Info>
Teknik destek veya sorularınız için 7/24 [GurLabs Discord](https://discord.gurlabs.xyz) sunucumuz üzerinden ekibimize ulaşabilirsiniz.
</Info>
"""
    },
    "tr/kurumsal/biz-kimiz.mdx": {
        "title": "Biz Kimiz? | GurLabs",
        "description": "GurLabs yenilikçi teknoloji stüdyosu hakkında detaylı bilgi edinin. Vizyonumuz, misyonumuz ve profesyonel web satış serüvenimiz.",
        "content": """# Biz Kimiz?

GurLabs, dijital dünyada fark yaratmak isteyen girişimcilere, oyun sunucularına ve kurumsal markalara özel çözümler sunan yeni nesil bir teknoloji stüdyosudur.

## Vizyonumuz

Premium kaliteyi herkes için erişilebilir kılmak. LeaderOS gibi güçlü altyapılara entegre ettiğimiz eşsiz temalarla, müşterilerimizin rakiplerinin her zaman bir adım önünde olmasını sağlıyoruz.

## Misyonumuz

- Müşteri odaklı ve %100 memnuniyet garantili hizmet sunmak.
- Yüksek performanslı, SEO uyumlu ve mobil öncelikli (responsive) web tasarımları üretmek.
- Satış sonrası kesintisiz destek ile uzun vadeli güven ilişkileri inşa etmek.

Biz sadece bir tema sağlayıcısı değil, aynı zamanda projenizin dijital çözüm ortağıyız.
"""
    },
    "tr/kurumsal/ekibimiz.mdx": {
        "title": "Ekibimiz | GurLabs",
        "description": "GurLabs'ın arkasındaki profesyonel tasarımcı ve geliştirici ekibiyle tanışın.",
        "content": """# Ekibimiz

GurLabs projelerinin arkasında, alanında uzman, vizyoner ve detaylara önem veren profesyonel bir ekip yer almaktadır.

Ekibimiz, modern web standartlarını (UI/UX, Tailwind CSS, Next.js vb.) en iyi şekilde harmanlayarak ortaya premium ürünler çıkarmaktadır.

> **Gücümüzü vizyonumuzdan, kalitemizi ekibimizden alıyoruz.**

Her projeye özel atanan proje yöneticilerimiz ve geliştiricilerimiz sayesinde tüm teslimatlar zamanında ve eksiksiz olarak yapılır.
"""
    },
    "tr/kurumsal/referanslarimiz.mdx": {
        "title": "Referanslarımız | GurLabs",
        "description": "GurLabs LeaderOS temaları ve özel web projeleri ile hayata geçirdiğimiz başarılı referans müşterilerimiz.",
        "content": """# Referanslarımız

GurLabs olarak, geliştirdiğimiz temalar ve özel web projeleri ile yüzlerce başarılı projenin arkasındaki gizli kahramanız.

Müşterilerimizin başarı hikayeleri, bizim kalitemizin en büyük göstergesidir. GurLabs ürünlerini tercih ederek satışlarını ve kullanıcı deneyimini zirveye taşıyan projeler arasına siz de katılın.

<Tip>
Detaylı referanslarımız ve portföyümüz için resmi sitemizi ziyaret edebilirsiniz: [gurlabs.xyz](https://gurlabs.xyz)
</Tip>
"""
    },
    "tr/kurumsal/linklerimiz.mdx": {
        "title": "Resmi Bağlantılarımız | GurLabs",
        "description": "GurLabs'a ait tüm resmi web siteleri, satış kanalları, sosyal medya hesapları ve iletişim linkleri.",
        "content": """# Resmi Bağlantılarımız

GurLabs ile ilgili tüm gelişmeleri takip edebileceğiniz ve bizimle iletişime geçebileceğiniz resmi platformlar:

- 🌐 **Ana Website:** [gurlabs.xyz](https://gurlabs.xyz)
- 🛒 **Mağaza:** [shop.gurlabs.xyz](https://shop.gurlabs.xyz)
- 💬 **Discord:** [discord.gurlabs.xyz](https://discord.gurlabs.xyz)
- 📧 **E-Posta:** [info@gurlabs.xyz](mailto:info@gurlabs.xyz)

Bizi sosyal medyadan takip etmeyi unutmayın!
"""
    },

    # TR OynaTR
    "tr/leaderos/oynatr/tanitim.mdx": {
        "title": "OynaTR Teması Özellikleri ve Tanıtım",
        "description": "GurLabs OynaTR LeaderOS teması: Gelişmiş, minimalist tasarım, modern UI/UX ve premium özellikler. Minecraft web siteniz için en iyi tema.",
        "content": """# OynaTR Teması Tanıtımı

OynaTR, LeaderOS altyapısı üzerinde çalışan, tamamen minimalist ve modern çizgilere sahip **premium** bir web temasıdır. Göz yormayan tasarımı ve üst düzey performansıyla projenizi bir adım öteye taşır.

## Öne Çıkan Özellikler

- 🎨 **Minimalist UI/UX:** Oyuncularınız aradıklarını saniyeler içinde bulsun.
- ⚡ **Yüksek Performans:** Özel optimize edilmiş kod yapısı ile ışık hızında açılış.
- 📱 **%100 Mobil Uyumlu:** Telefon ve tabletlerde kusursuz görünüm.
- 🔧 **Gelişmiş Özelleştirme:** Tema renklerini, menüleri ve logoları yönetim panelinden anında değiştirin.

<Frame>
  <img src="/logo/gurlabs-logo.png" alt="OynaTR Demo" />
</Frame>
"""
    },
    "tr/leaderos/oynatr/satin-alma.mdx": {
        "title": "OynaTR Teması Satın Al | GurLabs",
        "description": "OynaTR LeaderOS temasını satın alın. Lisanslama adımları, fiyatlandırma ve satış öncesi detaylar.",
        "content": """# OynaTR Satın Alma

OynaTR temasını resmi mağazamız üzerinden anında satın alabilir ve anında kullanmaya başlayabilirsiniz.

## Fiyatlandırma

**OynaTR Teması Fiyatı:** 749,99 ₺

<Card title="Hemen Satın Al" icon="cart-shopping" href="https://shop.gurlabs.xyz">
  GurLabs resmi mağazasına giderek OynaTR temanızı hemen sipariş edin.
</Card>

## Lisans Koşulları
- Satın alınan lisans **tek bir domain (alan adı)** için geçerlidir.
- Lisans devri veya satışı kesinlikle yasaktır.
- Satın alım sonrası dosyalar otomatik olarak hesabınıza tanımlanır.

Herhangi bir sorun yaşarsanız [Discord](https://discord.gurlabs.xyz) sunucumuzdan destek bileti oluşturabilirsiniz.
"""
    },
    "tr/leaderos/oynatr/yukleme.mdx": {
        "title": "OynaTR Kurulum Rehberi | LeaderOS",
        "description": "Satın aldığınız OynaTR temasını LeaderOS panelinize adım adım nasıl kuracağınızı anlatan resimli ve detaylı rehber.",
        "content": """# OynaTR Yükleme Rehberi

OynaTR temanızı satın aldıktan sonra sitenize kurmak oldukça basittir. Lütfen aşağıdaki adımları sırasıyla uygulayın.

## Kurulum Adımları

<Steps>
  <Step title="Dosyaları İndirin">
    [shop.gurlabs.xyz](https://shop.gurlabs.xyz) adresinden müşteri panelinize giriş yapıp OynaTR tema dosyalarınızı (ZIP formatında) bilgisayarınıza indirin.
  </Step>
  <Step title="FTP'ye Yükleyin">
    Web sitenizin FTP'sine veya dosya yöneticisine (cPanel/Plesk) bağlanın.
    İndirdiğiniz `.zip` dosyasının içindeki klasörleri LeaderOS ana dizinine yükleyin.
  </Step>
  <Step title="Paneli Aktifleştirin">
    LeaderOS Yönetim Paneli > Temalar sekmesine gidin.
    OynaTR temasını bularak **Aktifleştir** butonuna tıklayın.
  </Step>
  <Step title="Önbelleği Temizleyin">
    Eski temanın kalıntılarının gitmesi için Yönetim Panelinden önbelleği temizleyin (Cache Temizle).
  </Step>
</Steps>

<Success>
Tebrikler! OynaTR temanız başarıyla kuruldu. Artık "Özelleştirme" sekmesindeki adımlara geçerek temanızı kişiselleştirebilirsiniz.
</Success>
"""
    },
    "tr/leaderos/oynatr/ozellestirme.mdx": {
        "title": "OynaTR Tema Özelleştirme | Renk, Logo ve Tasarım",
        "description": "OynaTR temasını kendi markanıza göre özelleştirin. Renk değiştirme, logo ekleme ve ana sayfa düzenleme rehberi.",
        "content": """# OynaTR Özelleştirme

Temanızın renklerini, logolarını ve genel görünümünü değiştirmek için kod bilgisine ihtiyacınız yoktur.

## Logo Değişimi
Yönetim Paneli > Ayarlar > Genel Ayarlar yolunu izleyerek sitenizin logosunu yükleyebilirsiniz. Yüklediğiniz logo otomatik olarak OynaTR menüsüne entegre olacaktır.

## Renk Paletini Değiştirme
LeaderOS Yönetim Paneli > Temalar > OynaTR Ayarları kısmından temanın **Ana Renk** (Primary) ve **Vurgu Rengi** (Accent) ayarlarını değiştirebilirsiniz.

Tavsiye Edilen Renk Seçimi:
- Ana Renk: Projenizin marka rengi (Örn: #2563EB)
- Yazı Tipi: Temanın kendi modern fontu otomatik yüklenecektir.

## Ana Sayfa Düzeni
Menülerin ve blokların sırasını LeaderOS panelinizdeki "Sayfalar" veya "Bloklar" kısmından sürükle bırak mantığıyla rahatça düzenleyebilirsiniz.
"""
    },
    "tr/leaderos/oynatr/kullanma.mdx": {
        "title": "OynaTR Yönetimi ve Kullanım Kılavuzu",
        "description": "OynaTR LeaderOS temasının günlük kullanımı, widget yönetimi, duyurular ve operasyonel ayarları.",
        "content": """# OynaTR Kullanım Rehberi

Temanızı kurdunuz ve özelleştirdiniz. Peki günlük kullanımda nelere dikkat etmelisiniz?

## Widget Yönetimi (Yan Menü)
Sitenizin sağ veya sol sütununda yer alan widget'ları (Discord botu, Son Bağışçılar, En İyi Oyuncular) yönetmek için:
- LeaderOS Yönetim Paneli > Widgetlar sekmesine gidin.
- Yeni widget ekleyebilir veya mevcutların konumunu (Sürükle & Bırak) değiştirebilirsiniz.

## Duyurular ve Haberler
Ana sayfanızdaki büyük slider veya duyuru panosu, "Haberler" modülünden beslenir. Eklediğiniz her haber, OynaTR'nin şık kart tasarımıyla otomatik olarak ana sayfada listelenir.
Haberlere görsel (thumbnail) eklemeyi unutmayın!
"""
    },
    "tr/leaderos/oynatr/iletisim.mdx": {
        "title": "OynaTR Teknik Destek ve İletişim",
        "description": "OynaTR teması için teknik destek talebi oluşturun. GurLabs destek ekibine 7/24 ulaşın.",
        "content": """# OynaTR Destek ve İletişim

OynaTR temasını kullanırken bir hatayla karşılaşırsanız veya yardıma ihtiyacınız olursa, GurLabs destek ekibi her zaman yanınızdadır.

## Destek Talebi Nasıl Oluşturulur?
1. [discord.gurlabs.xyz](https://discord.gurlabs.xyz) adresinden resmi Discord sunucumuza katılın.
2. Satın alım faturanızla birlikte hesabınızı doğrulayın.
3. **#destek-talebi** kanalından bir "Destek Bileti" (Ticket) oluşturun.

<Warning>
Sorununuzu iletirken aldığınız hatanın ekran görüntüsünü ve sistem loglarını iletmeyi unutmayın. Bu, çözüm sürecini oldukça hızlandıracaktır.
</Warning>

**E-Posta Desteği:** [info@gurlabs.xyz](mailto:info@gurlabs.xyz)
"""
    },

    # TR Arena
    "tr/leaderos/arena/tanitim.mdx": {
        "title": "Arena Teması Özellikleri ve Tanıtım",
        "description": "GurLabs Arena LeaderOS teması: Oyuncu ve topluluk odaklı, dinamik, agresif ve modern premium web teması.",
        "content": """# Arena Teması Tanıtımı

Arena Teması, tamamen e-spor dinamizmi ve oyuncu toplulukları baz alınarak tasarlanmış agresif, modern ve **premium** bir web temasıdır. 

Dikkat çekici banner alanları ve vurgulanmış butonlarla projenizin vizyonunu yansıtır.

## Öne Çıkan Özellikler

- 💥 **Dinamik Tasarım:** Keskin hatlar, koyu tema (Dark Mode) ağırlıklı oyuncu dostu arayüz.
- 🏆 **Topluluk Odaklılık:** Sunucu istatistiklerini ve lider tablolarını öne çıkaran özel modül görünümleri.
- ⚡ **Yüksek Performans:** LeaderOS altyapısıyla tam senkronizasyon ve sıfır donma.
- 📱 **Mobil Uyumluluk:** Her cihazda agresif ve şık görünümünden ödün vermez.
"""
    },
    "tr/leaderos/arena/satin-alma.mdx": {
        "title": "Arena Teması Satın Al | GurLabs",
        "description": "Arena LeaderOS temasını güvenle satın alın. Kurumsal satış, fiyatlar ve lisans detayları.",
        "content": """# Arena Satın Alma

Arena temasını saniyeler içinde satın alıp hemen indirebilirsiniz.

## Fiyatlandırma

**Arena Teması Fiyatı:** 749,99 ₺

<Card title="Hemen Satın Al" icon="cart-shopping" href="https://shop.gurlabs.xyz">
  GurLabs mağazasına gidin ve Arena temanıza sahip olun.
</Card>

## Lisans Koşulları
- Satın alınan temanın lisansı tek bir domaine tanımlanır.
- Başkalarına satılması, paylaşılması veya kopyalanması kesinlikle yasaktır.
- GurLabs tarafından ömür boyu teknik destek hakkına sahip olursunuz.
"""
    },
    "tr/leaderos/arena/yukleme.mdx": {
        "title": "Arena Kurulum Rehberi | LeaderOS",
        "description": "Arena temasının LeaderOS altyapısına sorunsuz kurulumu. Adım adım FTP yükleme ve panel ayarları.",
        "content": """# Arena Yükleme Rehberi

Arena temasının kurulumu standart LeaderOS yönergelerine uygundur.

<Steps>
  <Step title="Dosya İndirme">
    [shop.gurlabs.xyz](https://shop.gurlabs.xyz) panelinizden satın aldığınız Arena temasını bilgisayarınıza indirin.
  </Step>
  <Step title="Sunucuya Aktarım">
    İndirdiğiniz arşiv dosyasının içindeki tema dosyalarını, sitenizin barındığı sunucuya (FTP üzerinden) direkt ana dizine atın.
  </Step>
  <Step title="Temayı Aktifleştirme">
    Yönetici girişi yapın. LeaderOS Yönetim Paneli > Temalar yolunu takip ederek "Arena" temasını seçin ve aktifleştirin.
  </Step>
</Steps>

<Note>
Yükleme sonrası temanın hatasız görünmesi için muhakkak **Önbellek (Cache) Temizleme** işlemini yapın.
</Note>
"""
    },
    "tr/leaderos/arena/ozellestirme.mdx": {
        "title": "Arena Tema Özelleştirme | Renk, Logo ve Tasarım",
        "description": "Arena temasını projenize göre özelleştirin. Dinamik renk paletleri, görsel değişiklikler ve sayfa yapılandırması.",
        "content": """# Arena Özelleştirme

Arena temasının agresif yapısını kendi kurumsal renklerinizle harmanlayın.

## Renk ve Görünüm Değişikliği
LeaderOS panelinizde yer alan **Tema Ayarları** sekmesinden Arena'nın birincil ve ikincil renklerini hex (örneğin `#E11D48`) kodlarıyla değiştirebilirsiniz. Değişiklikler tüm sayfalara otomatik olarak yansır.

## Arka Plan ve Afişler (Banners)
Arena teması büyük arka plan görselleri (Banner) kullanımına oldukça uygundur. CSS müdahalesine gerek kalmadan panel üzerinden ana sayfa görselinizi yüklediğinizde, karanlık arayüz ile mükemmel bir uyum sağlayacaktır.
"""
    },
    "tr/leaderos/arena/kullanma.mdx": {
        "title": "Arena Yönetimi ve Kullanım Kılavuzu",
        "description": "Arena LeaderOS temasının panel üzerinden kullanımı. İçerik girme, ayarları düzenleme.",
        "content": """# Arena Kullanım Kılavuzu

Arena temasını günlük projelerinizde verimli şekilde kullanmak için bazı ipuçları:

## Mağaza Modülü Kullanımı
Arena'nın mağaza (VİP/Ürün Satış) kartları oldukça belirgin ve büyüktür. Ürün eklerken mutlaka şeffaf arka planlı (PNG) veya kaliteli kare görseller kullanmanız temanın profesyonelliğini artıracaktır.

## İstatistik Kartları
Oyun sunucunuzun online oyuncu sayısı ve diğer API istatistikleri doğrudan ana sayfada vurgulanır. Sunucu ayarlarınızın LeaderOS panelinde doğru yapılandırıldığından emin olun.
"""
    },
    "tr/leaderos/arena/iletisim.mdx": {
        "title": "Arena Teknik Destek ve İletişim",
        "description": "Arena teması için profesyonel destek hizmeti. GurLabs ile iletişime geçin.",
        "content": """# Arena Destek ve İletişim

Sorunsuz bir deneyim için daima buradayız. Arena teması hakkında soru, görüş, öneri veya teknik destek bildirimleri için aşağıdaki kanalları kullanın.

## Discord Destek Kanalımız
[discord.gurlabs.xyz](https://discord.gurlabs.xyz) adresinden bize ulaşın, destek bileti açın, teknik ekibimiz dakikalar içinde sorununuzu çözsün!

**İletişim:** [info@gurlabs.xyz](mailto:info@gurlabs.xyz)
"""
    },

    # TR Ozel Projeler
    "tr/ozel-projeler/talep.mdx": {
        "title": "Özel Kurumsal Web Projesi Talebi | GurLabs",
        "description": "GurLabs profesyonel ekibiyle sıfırdan kurumsal ve e-ticaret odaklı web projeleri geliştirin. Fiyat teklifi ve talep formu.",
        "content": """# Özel Web Projesi Talebi

İşinizi dijitalde büyütmek, kurumsal bir kimlik kazanmak veya özel bir e-ticaret/yönetim paneli yazılımına mı ihtiyacınız var? GurLabs olarak sıfırdan, tamamen size özel projeler geliştiriyoruz.

## Neler Yapıyoruz?
- Kurumsal Web Siteleri
- Gelişmiş E-Ticaret Sistemleri
- Özel CMS (İçerik Yönetim Sistemleri) ve Admin Panelleri
- Full-Stack Web Uygulamaları (Next.js, Laravel, Node.js)

## Nasıl Teklif Alınır?
Özel projeniz için fiyat teklifi ve detaylı analiz toplantısı talep etmek için iletişim kanallarımızı kullanın:
- **Discord Üzerinden:** [discord.gurlabs.xyz](https://discord.gurlabs.xyz) sunucumuzda "Özel Proje" bileti açarak.
- **Mail Yoluyla:** Proje detaylarınızı (brief) [info@gurlabs.xyz](mailto:info@gurlabs.xyz) adresine göndererek.
"""
    },
    "tr/ozel-projeler/sureclerimiz.mdx": {
        "title": "Proje Geliştirme Süreçlerimiz | GurLabs",
        "description": "GurLabs'ta özel web projesi nasıl geliştirilir? Tasarım, yazılım, test ve yayına alma aşamalarımız.",
        "content": """# Proje Geliştirme Süreçlerimiz

GurLabs olarak, her özel web projesini büyük bir titizlikle, tamamen şeffaf aşamalarla hayata geçiriyoruz.

<Steps>
  <Step title="1. Analiz ve Planlama">
    Müşterimizin istekleri (brief) alınır. İhtiyaç duyulan teknolojiler, site mimarisi ve tahmini teslim süresi belirlenip fiyat teklifi sunulur.
  </Step>
  <Step title="2. UI/UX Tasarım">
    Yazılıma başlamadan önce sitenizin arayüz tasarımı (Figma vb.) hazırlanıp müşterinin onayına sunulur. Onaylanmayan hiçbir tasarım koda dökülmez.
  </Step>
  <Step title="3. Geliştirme (Yazılım)">
    Tasarım kodlamaya başlanır. Front-end ve Back-end geliştirme süreçleri en modern standartlarla (SEO uyumlu ve güvenli) yazılır.
  </Step>
  <Step title="4. Test ve Yayına Alma">
    Projeler tüm cihazlarda (Mobil/Masaüstü) test edilir. Güvenlik açıkları taranır. Hatasız olduğu onaylandıktan sonra müşterinin sunucusunda yayına alınır.
  </Step>
</Steps>
"""
    },

    # EN Root & Corporate
    "en/index.mdx": {
        "title": "GurLabs Documentation",
        "description": "Official documentation and help center for GurLabs premium LeaderOS themes (OynaTR, Arena) and custom web project solutions.",
        "content": """# Welcome to GurLabs Documentation Center! 🚀

As GurLabs, we are an innovative technology studio specializing in professional web sales, premium LeaderOS theme development, and custom/corporate web projects.

You can find all the guides, installation steps, and support documents you need right here.

## Our Services

<CardGroup cols={2}>
  <Card title="OynaTR Theme" icon="gamepad" href="/en/leaderos/oynatr/introduction">
    Our most popular LeaderOS theme, equipped with advanced, minimalist, and premium features.
  </Card>
  <Card title="Arena Theme" icon="swords" href="/en/leaderos/arena/introduction">
    Our modern, dynamic, and community-focused web theme.
  </Card>
  <Card title="Custom Web Projects" icon="code" href="/en/custom-projects/request">
    Corporate and modern e-commerce projects tailored to your needs, built from scratch.
  </Card>
  <Card title="Store" icon="shop" href="https://shop.gurlabs.xyz">
    Access all GurLabs products instantly via our official store.
  </Card>
</CardGroup>

<Info>
For technical support or inquiries, you can reach our team 24/7 via the [GurLabs Discord](https://discord.gurlabs.xyz) server.
</Info>
"""
    },
    "en/corporate/about-us.mdx": {
        "title": "About Us | GurLabs",
        "description": "Learn more about GurLabs, an innovative tech studio. Our vision, mission, and journey in professional web sales.",
        "content": """# About Us

GurLabs is a next-generation technology studio offering tailored solutions to entrepreneurs, gaming servers, and corporate brands aiming to make a difference in the digital world.

## Our Vision

To make premium quality accessible to everyone. By integrating unique themes into powerful infrastructures like LeaderOS, we ensure our clients are always one step ahead of their competitors.

## Our Mission

- Provide customer-focused services with a 100% satisfaction guarantee.
- Create high-performance, SEO-friendly, and mobile-first (responsive) web designs.
- Build long-term relationships based on trust through continuous after-sales support.

We are not just a theme provider; we are the digital solution partner for your project.
"""
    },
    "en/corporate/our-team.mdx": {
        "title": "Our Team | GurLabs",
        "description": "Meet the professional designers and developers behind GurLabs.",
        "content": """# Our Team

Behind GurLabs' projects stands a professional team of experts who are visionary and pay great attention to detail.

Our team brings premium products to life by masterfully blending modern web standards (UI/UX, Tailwind CSS, Next.js, etc.).

> **We draw our strength from our vision, and our quality from our team.**

Thanks to the dedicated project managers and developers assigned to each project, all deliveries are made on time and perfectly executed.
"""
    },
    "en/corporate/references.mdx": {
        "title": "Our References | GurLabs",
        "description": "Successful reference clients and partners using GurLabs LeaderOS themes and custom web projects.",
        "content": """# Our References

As GurLabs, we are the hidden heroes behind hundreds of successful projects with the themes and custom web projects we've developed.

The success stories of our clients are the greatest indicator of our quality. Join the projects that have taken their sales and user experience to the peak by choosing GurLabs products.

<Tip>
For our detailed references and portfolio, visit our official website: [gurlabs.xyz](https://gurlabs.xyz)
</Tip>
"""
    },
    "en/corporate/links.mdx": {
        "title": "Official Links | GurLabs",
        "description": "All official GurLabs websites, sales channels, social media accounts, and contact links.",
        "content": """# Official Links

The official platforms where you can follow all developments regarding GurLabs and get in touch with us:

- 🌐 **Main Website:** [gurlabs.xyz](https://gurlabs.xyz)
- 🛒 **Store:** [shop.gurlabs.xyz](https://shop.gurlabs.xyz)
- 💬 **Discord:** [discord.gurlabs.xyz](https://discord.gurlabs.xyz)
- 📧 **E-Mail:** [info@gurlabs.xyz](mailto:info@gurlabs.xyz)

Don't forget to follow us on social media!
"""
    },

    # EN OynaTR
    "en/leaderos/oynatr/introduction.mdx": {
        "title": "OynaTR Theme Features & Introduction",
        "description": "GurLabs OynaTR LeaderOS theme: Advanced, minimalist design, modern UI/UX, and premium features. The best theme for your Minecraft website.",
        "content": """# OynaTR Theme Introduction

OynaTR is a **premium** web theme running on the LeaderOS infrastructure, featuring completely minimalist and modern lines. It takes your project one step further with its eye-friendly design and top-tier performance.

## Highlighted Features

- 🎨 **Minimalist UI/UX:** Let your players find what they're looking for in seconds.
- ⚡ **High Performance:** Lightning-fast loading times with a specially optimized code structure.
- 📱 **100% Mobile Responsive:** Flawless appearance on phones and tablets.
- 🔧 **Advanced Customization:** Change theme colors, menus, and logos instantly from the admin panel.

<Frame>
  <img src="/logo/gurlabs-logo.png" alt="OynaTR Demo" />
</Frame>
"""
    },
    "en/leaderos/oynatr/purchasing.mdx": {
        "title": "Buy OynaTR Theme | GurLabs",
        "description": "Purchase the OynaTR LeaderOS theme. Licensing steps, pricing, and pre-sales details.",
        "content": """# Purchasing OynaTR

You can instantly purchase the OynaTR theme via our official store and start using it right away.

## Pricing

**OynaTR Theme Price:** 749.99 ₺

<Card title="Buy Now" icon="cart-shopping" href="https://shop.gurlabs.xyz">
  Go to the official GurLabs store and order your OynaTR theme now.
</Card>

## Licensing Conditions
- The purchased license is valid for a **single domain**.
- Transfer or resale of the license is strictly prohibited.
- Files are automatically assigned to your account after purchase.

If you encounter any issues, you can create a support ticket on our [Discord](https://discord.gurlabs.xyz) server.
"""
    },
    "en/leaderos/oynatr/installation.mdx": {
        "title": "OynaTR Installation Guide | LeaderOS",
        "description": "Step-by-step illustrated and detailed guide on how to install your purchased OynaTR theme on your LeaderOS panel.",
        "content": """# OynaTR Installation Guide

Installing the OynaTR theme on your site after purchase is very simple. Please follow the steps below.

## Installation Steps

<Steps>
  <Step title="Download Files">
    Log in to your client panel at [shop.gurlabs.xyz](https://shop.gurlabs.xyz) and download your OynaTR theme files (in ZIP format) to your computer.
  </Step>
  <Step title="Upload via FTP">
    Connect to your website's FTP or file manager (cPanel/Plesk).
    Upload the folders inside the downloaded `.zip` file to the LeaderOS root directory.
  </Step>
  <Step title="Activate from Panel">
    Go to LeaderOS Admin Panel > Themes tab.
    Find the OynaTR theme and click the **Activate** button.
  </Step>
  <Step title="Clear Cache">
    Clear the cache from the Admin Panel to ensure no remnants of the old theme remain.
  </Step>
</Steps>

<Success>
Congratulations! Your OynaTR theme is successfully installed. You can now proceed to the "Customization" steps to personalize your theme.
</Success>
"""
    },
    "en/leaderos/oynatr/customization.mdx": {
        "title": "OynaTR Theme Customization | Colors & Design",
        "description": "Customize the OynaTR theme for your brand. Color changing, logo adding, and home page layout guide.",
        "content": """# Customizing OynaTR

You do not need coding knowledge to change the colors, logos, and overall appearance of your theme.

## Changing the Logo
You can upload your site's logo by navigating to Admin Panel > Settings > General Settings. The uploaded logo will automatically integrate into the OynaTR menu.

## Changing the Color Palette
You can change the **Primary Color** and **Accent Color** settings of the theme from the LeaderOS Admin Panel > Themes > OynaTR Settings section.

Recommended Color Choice:
- Primary Color: Your brand's main color (e.g., #2563EB)
- Font: The theme's modern font will load automatically.

## Home Page Layout
You can easily arrange the order of menus and blocks using the drag-and-drop logic in the "Pages" or "Blocks" section of your LeaderOS panel.
"""
    },
    "en/leaderos/oynatr/usage.mdx": {
        "title": "OynaTR Management and Usage Guide",
        "description": "Daily usage of the OynaTR LeaderOS theme, widget management, announcements, and operational settings.",
        "content": """# OynaTR Usage Guide

You have installed and customized your theme. What should you pay attention to in daily usage?

## Widget Management (Sidebar)
To manage the widgets (Discord bot, Recent Donors, Top Players) located in the right or left column of your site:
- Go to LeaderOS Admin Panel > Widgets tab.
- You can add new widgets or change the position of existing ones (Drag & Drop).

## Announcements and News
The large slider or announcement board on your home page is fed from the "News" module. Every news item you add is automatically listed on the home page with OynaTR's elegant card design.
Don't forget to add an image (thumbnail) to the news!
"""
    },
    "en/leaderos/oynatr/contact.mdx": {
        "title": "OynaTR Technical Support & Contact",
        "description": "Create a technical support request for the OynaTR theme. Contact GurLabs support 24/7.",
        "content": """# OynaTR Support and Contact

If you encounter an error or need help while using the OynaTR theme, the GurLabs support team is always by your side.

## How to Create a Support Request?
1. Join our official Discord server at [discord.gurlabs.xyz](https://discord.gurlabs.xyz).
2. Verify your account with your purchase invoice.
3. Create a "Support Ticket" in the **#support-tickets** channel.

<Warning>
When reporting your issue, do not forget to provide a screenshot of the error and system logs. This will significantly speed up the resolution process.
</Warning>

**E-Mail Support:** [info@gurlabs.xyz](mailto:info@gurlabs.xyz)
"""
    },

    # EN Arena
    "en/leaderos/arena/introduction.mdx": {
        "title": "Arena Theme Features & Introduction",
        "description": "GurLabs Arena LeaderOS theme: Player and community focused, dynamic, aggressive, and modern premium web theme.",
        "content": """# Arena Theme Introduction

The Arena Theme is an aggressive, modern, and **premium** web theme designed entirely around e-sports dynamism and player communities.

It reflects the vision of your project with eye-catching banner areas and highlighted buttons.

## Highlighted Features

- 💥 **Dynamic Design:** Sharp lines, dark mode-oriented player-friendly interface.
- 🏆 **Community Focused:** Special module designs that highlight server statistics and leaderboards.
- ⚡ **High Performance:** Full synchronization with the LeaderOS infrastructure with zero lag.
- 📱 **Mobile Responsive:** Maintains its aggressive and stylish look on every device.
"""
    },
    "en/leaderos/arena/purchasing.mdx": {
        "title": "Buy Arena Theme | GurLabs",
        "description": "Securely purchase the Arena LeaderOS theme. Corporate sales, pricing, and license details.",
        "content": """# Purchasing Arena

You can purchase and instantly download the Arena theme within seconds.

## Pricing

**Arena Theme Price:** 749.99 ₺

<Card title="Buy Now" icon="cart-shopping" href="https://shop.gurlabs.xyz">
  Go to the GurLabs store and get your Arena theme.
</Card>

## Licensing Conditions
- The license for the purchased theme is assigned to a single domain.
- Reselling, sharing, or copying is strictly prohibited.
- You are entitled to lifetime technical support from GurLabs.
"""
    },
    "en/leaderos/arena/installation.mdx": {
        "title": "Arena Installation Guide | LeaderOS",
        "description": "Seamless installation of the Arena theme on LeaderOS. Step-by-step FTP upload and panel settings.",
        "content": """# Arena Installation Guide

The installation of the Arena theme complies with standard LeaderOS guidelines.

<Steps>
  <Step title="Download File">
    Download the Arena theme you purchased from your [shop.gurlabs.xyz](https://shop.gurlabs.xyz) panel to your computer.
  </Step>
  <Step title="Transfer to Server">
    Upload the theme files inside the downloaded archive file directly to the root directory of your website's server (via FTP).
  </Step>
  <Step title="Activate Theme">
    Log in as admin. Follow the path LeaderOS Admin Panel > Themes, select the "Arena" theme, and activate it.
  </Step>
</Steps>

<Note>
Be sure to perform the **Clear Cache** operation to ensure the theme appears flawlessly after installation.
</Note>
"""
    },
    "en/leaderos/arena/customization.mdx": {
        "title": "Arena Theme Customization | Colors & Design",
        "description": "Customize the Arena theme for your project. Dynamic color palettes, visual changes, and page configuration.",
        "content": """# Customizing Arena

Blend the aggressive structure of the Arena theme with your own corporate colors.

## Changing Color and Appearance
You can change the primary and secondary colors of Arena with hex codes (e.g., `#E11D48`) from the **Theme Settings** tab in your LeaderOS panel. Changes automatically apply to all pages.

## Backgrounds and Banners
The Arena theme is highly suitable for large background images (Banners). Without needing CSS intervention, when you upload your home page image via the panel, it will blend perfectly with the dark interface.
"""
    },
    "en/leaderos/arena/usage.mdx": {
        "title": "Arena Management and Usage Guide",
        "description": "Usage of the Arena LeaderOS theme via the panel. Entering content, editing settings.",
        "content": """# Arena Usage Guide

Some tips to use the Arena theme efficiently in your daily projects:

## Store Module Usage
Arena's store (VIP/Product Sales) cards are quite distinct and large. Make sure to use transparent background (PNG) or high-quality square images when adding products to enhance the professionalism of the theme.

## Statistics Cards
Your game server's online player count and other API statistics are highlighted directly on the home page. Ensure your server settings are configured correctly in the LeaderOS panel.
"""
    },
    "en/leaderos/arena/contact.mdx": {
        "title": "Arena Technical Support & Contact",
        "description": "Professional support service for the Arena theme. Contact GurLabs.",
        "content": """# Arena Support and Contact

We are always here for a seamless experience. Use the channels below for questions, comments, suggestions, or technical support notifications regarding the Arena theme.

## Our Discord Support Channel
Contact us at [discord.gurlabs.xyz](https://discord.gurlabs.xyz), open a support ticket, and our technical team will resolve your issue in minutes!

**Contact:** [info@gurlabs.xyz](mailto:info@gurlabs.xyz)
"""
    },

    # EN Custom Projects
    "en/custom-projects/request.mdx": {
        "title": "Custom Corporate Web Project Request | GurLabs",
        "description": "Develop custom corporate and e-commerce web projects from scratch with GurLabs' professional team. Quote and request form.",
        "content": """# Custom Web Project Request

Looking to grow your business digitally, gain a corporate identity, or need a custom e-commerce/admin panel software? At GurLabs, we develop entirely custom projects from scratch.

## What Do We Do?
- Corporate Websites
- Advanced E-Commerce Systems
- Custom CMS (Content Management Systems) and Admin Panels
- Full-Stack Web Applications (Next.js, Laravel, Node.js)

## How to Get a Quote?
To request a price quote and detailed analysis meeting for your custom project, use our communication channels:
- **Via Discord:** By opening a "Custom Project" ticket on our server at [discord.gurlabs.xyz](https://discord.gurlabs.xyz).
- **Via E-Mail:** By sending your project details (brief) to [info@gurlabs.xyz](mailto:info@gurlabs.xyz).
"""
    },
    "en/custom-projects/process.mdx": {
        "title": "Our Project Development Process | GurLabs",
        "description": "How is a custom web project developed at GurLabs? Our design, software, testing, and deployment stages.",
        "content": """# Our Project Development Process

As GurLabs, we bring every custom web project to life with great care and fully transparent stages.

<Steps>
  <Step title="1. Analysis and Planning">
    The client's requests (brief) are received. The required technologies, site architecture, and estimated delivery time are determined, and a price quote is presented.
  </Step>
  <Step title="2. UI/UX Design">
    Before coding begins, the interface design of your site (e.g., Figma) is prepared and submitted for client approval. No unapproved design is turned into code.
  </Step>
  <Step title="3. Development (Software)">
    Coding of the design begins. Front-end and Back-end development processes are written with the most modern standards (SEO friendly and secure).
  </Step>
  <Step title="4. Testing and Deployment">
    Projects are tested across all devices (Mobile/Desktop). Vulnerabilities are scanned. Once confirmed to be error-free, it is deployed on the client's server.
  </Step>
</Steps>
"""
    }
}

for path, data in files.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"---\ntitle: \"{data['title']}\"\ndescription: \"{data['description']}\"\n---\n\n{data['content']}")

print("All files populated with premium content.")
