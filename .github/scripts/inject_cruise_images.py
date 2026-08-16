from pathlib import Path
import re

mapping = {
    'amanda-luxury-cruise': 'amanda-luxury-cruise.webp',
    'hera-classic-cruise': 'hera-classic-cruise.webp',
    'le-journey-luxury-cruise': 'le-journey-luxury-cruise.webp',
    'le-journey-elegance-cruise-4-star': 'le-journey-elegance-cruise-4-star.webp',
    'scarlet-pearl': 'scarlet-pearl.webp',
    'milalux-cruises': 'milalux-cruises.webp',
    'cycad-indochine-cruise': 'cycad-indochine-cruise.webp',
    'cycad-grand-cruise': 'cycad-grand-cruise.webp',
    'verdure-lotus-classic': 'verdure-lotus-classic.webp',
    'verdure-lotus-luxury': 'verdure-lotus-luxury.webp',
    'phoenix-cruise': 'phoenix-cruise.webp',
    'orchid-trendy-cruise': 'orchid-trendy-cruise.webp',
    'orchid-classic-cruise': 'orchid-classic-cruise.webp',
    'fantasea-cruise-3-star': 'fantasea-cruise-3-star.webp',
    'orchid-premium': 'orchid-premium.webp',
    'velar-of-the-sea': 'velar-of-the-sea.webp',
    'celina-of-the-sea': 'celina-of-the-sea.webp',
    'sea-coral': 'sea-coral.webp',
    'aqua-legend-cruise': 'aqua-legend-cruise.webp',
    'tulip-cruise': 'tulip-cruise.webp',
    'catherine-cruise': 'catherine-cruise.webp',
    'star-light-cruise': 'star-light-cruise.webp',
    'la-casta-star': 'la-casta-star.webp',
    'grand-pioneers': 'grand-pioneers.webp',
    'ruby-cruise': 'ruby-cruise.webp',
    'la-pandora': 'la-pandora.webp',
    'athena-cruise': 'athena-cruise.webp',
    'signature-cruise-bai-tu-long': 'signature-cruise-bai-tu-long.webp',
}

for slug, image in mapping.items():
    path = Path('cruises') / f'{slug}.html'
    html = path.read_text(encoding='utf-8')
    if 'class="cruise-hero-image"' in html:
        continue
    alt = slug.replace('-', ' ').title()
    image_tag = (
        f'<img class="cruise-hero-image" '
        f'src="../assets/cruises/{image}" '
        f'alt="{alt}" loading="eager" decoding="async" '
        f'style="width:100%;height:330px;object-fit:cover;border-radius:22px;display:block;">'
    )
    updated, count = re.subn(r'<div class="visual"[^>]*>.*?</div>', image_tag, html, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'Could not find visual placeholder in {path}')
    path.write_text(updated, encoding='utf-8')

print('Injected hero images into 28 cruise pages.')
