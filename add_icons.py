import os
import glob

# Map filenames to Mintlify/FontAwesome/Lucide icons
icon_mapping = {
    "index.mdx": "house",
    "biz-kimiz.mdx": "building",
    "about-us.mdx": "building",
    "ekibimiz.mdx": "users",
    "our-team.mdx": "users",
    "referanslarimiz.mdx": "star",
    "references.mdx": "star",
    "linklerimiz.mdx": "link",
    "links.mdx": "link",
    "tanitim.mdx": "book-open",
    "introduction.mdx": "book-open",
    "satin-alma.mdx": "cart-shopping",
    "purchasing.mdx": "cart-shopping",
    "yukleme.mdx": "download",
    "installation.mdx": "download",
    "ozellestirme.mdx": "palette",
    "customization.mdx": "palette",
    "kullanma.mdx": "gamepad",
    "usage.mdx": "gamepad",
    "iletisim.mdx": "envelope",
    "contact.mdx": "envelope",
    "talep.mdx": "file-contract",
    "request.mdx": "file-contract",
    "sureclerimiz.mdx": "list-check",
    "process.mdx": "list-check",
}

def add_icon(filepath):
    filename = os.path.basename(filepath)
    if filename not in icon_mapping:
        return
        
    icon_name = icon_mapping[filename]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "icon:" in content:
        return
        
    parts = content.split("---")
    if len(parts) >= 3:
        frontmatter = parts[1]
        
        # Insert icon right after title
        lines = frontmatter.split('\n')
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if line.startswith('title:'):
                new_lines.append(f'icon: "{icon_name}"')
                
        parts[1] = '\n'.join(new_lines)
        new_content = "---".join(parts)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

for file in glob.glob("**/*.mdx", recursive=True):
    add_icon(file)

print("Icons added to frontmatter.")
