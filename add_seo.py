import os
import glob

# SEO keywords for TR and EN pages
keywords_tr = "GurLabs, LeaderOS Tema, Minecraft Web Tema, Premium Tema, OynaTR, Arena, Özel Web Projesi"
keywords_en = "GurLabs, LeaderOS Theme, Minecraft Web Theme, Premium Theme, OynaTR, Arena, Custom Web Project"

def update_seo(filepath, lang="tr"):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "keywords:" in content:
        return # Already processed
    
    # Split by frontmatter
    parts = content.split("---")
    if len(parts) >= 3:
        frontmatter = parts[1]
        kw = keywords_tr if lang == "tr" else keywords_en
        
        # Add keywords and og:image to frontmatter
        # Mintlify uses the logo for og:image by default, but explicitly setting keywords is very helpful.
        new_frontmatter = frontmatter.rstrip() + f'\nkeywords: "{kw}"\n'
        
        parts[1] = new_frontmatter
        new_content = "---".join(parts)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

# Process all MDX files
for file in glob.glob("tr/**/*.mdx", recursive=True):
    update_seo(file, "tr")

for file in glob.glob("en/**/*.mdx", recursive=True):
    update_seo(file, "en")

for file in glob.glob("*.mdx"):
    update_seo(file, "en") # root files

print("SEO keywords added to all MDX files.")
