import os

tr_payment_content = """## Ödeme ve Teslimat

Sitemizden satın almanız durumunda tema lisansınız **direkt olarak domaininize tanımlanır** ve anında teslim edilir.

<CardGroup cols={2}>
  <Card title="(Tavsiye Edilen) Havale / EFT ile Ödeme" icon="building-columns" href="https://discord.gurlabs.xyz">
    Discord sunucumuz üzerinden destek bileti açarak Ticari IBAN hesabımıza ödeme yapabilirsiniz.
  </Card>
  <Card title="Kredi Kartı ile Satın Al" icon="cart-shopping" href="https://shop.gurlabs.xyz">
    GurLabs resmi mağazasına giderek temanızı kredi kartıyla anında sipariş edebilirsiniz.
  </Card>
</CardGroup>

## Fiyatlandırma"""

en_payment_content = """## Payment and Delivery

If you purchase from our site, the theme license is **directly assigned to your domain** and delivered instantly.

<CardGroup cols={2}>
  <Card title="(Recommended) Bank Transfer / IBAN" icon="building-columns" href="https://discord.gurlabs.xyz">
    You can make a payment to our Corporate IBAN account by opening a support ticket via our Discord server.
  </Card>
  <Card title="Buy with Credit Card" icon="cart-shopping" href="https://shop.gurlabs.xyz">
    Order your theme instantly with a credit card by visiting the official GurLabs store.
  </Card>
</CardGroup>

## Pricing"""

def update_file(filepath, is_tr):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the old basic purchase card and pricing intro
    if is_tr:
        # We find "## Fiyatlandırma" and everything after it until "## Lisans Koşulları"
        # We will replace the paragraph before Fiyatlandırma, and Fiyatlandırma itself.
        if "## Ödeme ve Teslimat" in content:
            return # Already updated
            
        import re
        # Find where to inject
        new_content = re.sub(
            r'## Fiyatlandırma', 
            tr_payment_content, 
            content
        )
        
        # Remove the old card
        new_content = re.sub(r'<Card title="Hemen Satın Al".*?</Card>', '', new_content, flags=re.DOTALL)
        
    else:
        if "## Payment and Delivery" in content:
            return
            
        import re
        new_content = re.sub(
            r'## Pricing', 
            en_payment_content, 
            content
        )
        new_content = re.sub(r'<Card title="Buy Now".*?</Card>', '', new_content, flags=re.DOTALL)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

files_tr = [
    "tr/leaderos/oynatr/satin-alma.mdx",
    "tr/leaderos/arena/satin-alma.mdx"
]

files_en = [
    "en/leaderos/oynatr/purchasing.mdx",
    "en/leaderos/arena/purchasing.mdx"
]

for f in files_tr:
    update_file(f, True)
    
for f in files_en:
    update_file(f, False)

print("Purchasing pages updated.")
