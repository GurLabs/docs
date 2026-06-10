import os
import glob
import re

# Emojis to remove
emojis = ["🚀", "🌐", "🛒", "💬", "📧", "🎨", "⚡", "📱", "🔧", "💥", "🏆"]

def remove_emojis_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    for emoji in emojis:
        content = content.replace(emoji + " ", "") # with trailing space
        content = content.replace(emoji, "") # without trailing space
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

for file in glob.glob("**/*.mdx", recursive=True):
    remove_emojis_from_file(file)

print("Emojis removed.")
