import os
import glob

# Mapping filenames to short sidebar titles
short_titles = {
    # TR
    "index.mdx": {"tr": "Ana Sayfa", "en": "Home"},
    "biz-kimiz.mdx": {"tr": "Biz Kimiz?", "en": "About Us"},
    "ekibimiz.mdx": {"tr": "Ekibimiz", "en": "Our Team"},
    "referanslarimiz.mdx": {"tr": "Referanslarımız", "en": "References"},
    "linklerimiz.mdx": {"tr": "Linklerimiz", "en": "Links"},
    
    "tanitim.mdx": {"tr": "Tanıtım", "en": "Introduction"},
    "satin-alma.mdx": {"tr": "Satın Alma", "en": "Purchasing"},
    "yukleme.mdx": {"tr": "Yükleme", "en": "Installation"},
    "ozellestirme.mdx": {"tr": "Özelleştirme", "en": "Customization"},
    "kullanma.mdx": {"tr": "Kullanma", "en": "Usage"},
    "iletisim.mdx": {"tr": "İletişim", "en": "Contact"},
    
    "talep.mdx": {"tr": "Proje Talebi", "en": "Project Request"},
    "sureclerimiz.mdx": {"tr": "Süreçlerimiz", "en": "Our Process"},
    
    # EN (Some filenames are different in EN)
    "about-us.mdx": {"tr": "Biz Kimiz?", "en": "About Us"},
    "our-team.mdx": {"tr": "Ekibimiz", "en": "Our Team"},
    "references.mdx": {"tr": "Referanslarımız", "en": "References"},
    "links.mdx": {"tr": "Linklerimiz", "en": "Links"},
    
    "introduction.mdx": {"tr": "Tanıtım", "en": "Introduction"},
    "purchasing.mdx": {"tr": "Satın Alma", "en": "Purchasing"},
    "installation.mdx": {"tr": "Yükleme", "en": "Installation"},
    "customization.mdx": {"tr": "Özelleştirme", "en": "Customization"},
    "usage.mdx": {"tr": "Kullanma", "en": "Usage"},
    "contact.mdx": {"tr": "İletişim", "en": "Contact"},
    
    "request.mdx": {"tr": "Proje Talebi", "en": "Project Request"},
    "process.mdx": {"tr": "Süreçlerimiz", "en": "Our Process"},
}

def add_sidebar_title(filepath, lang):
    filename = os.path.basename(filepath)
    if filename not in short_titles:
        return
        
    short_title = short_titles[filename][lang]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "sidebarTitle:" in content:
        return
        
    parts = content.split("---")
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # Insert sidebarTitle right after title
        lines = frontmatter.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if line.startswith('title:'):
                new_lines.append(f'sidebarTitle: "{short_title}"')
                
        parts[1] = '\n'.join(new_lines)
        new_content = "---".join(parts)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

for file in glob.glob("tr/**/*.mdx", recursive=True):
    add_sidebar_title(file, "tr")

for file in glob.glob("en/**/*.mdx", recursive=True):
    add_sidebar_title(file, "en")

for file in glob.glob("*.mdx"):
    add_sidebar_title(file, "en") # root files if any

print("Sidebar titles added.")
