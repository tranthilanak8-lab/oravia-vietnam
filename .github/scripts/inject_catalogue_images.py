from pathlib import Path
import re

mapping = {
    'Amanda Luxury Cruise': 'amanda-luxury-cruise.webp',
    'Hera Classic Cruise': 'hera-classic-cruise.webp',
    'Le Journey Luxury Cruise': 'le-journey-luxury-cruise.webp',
    'Le Journey Elegance Cruise': 'le-journey-elegance-cruise-4-star.webp',
    'Scarlet Pearl': 'scarlet-pearl.webp',
    'Milalux Cruises': 'milalux-cruises.webp',
    'Cycad Indochine Cruise': 'cycad-indochine-cruise.webp',
    'Cycad Grand Cruise': 'cycad-grand-cruise.webp',
    'Verdure Lotus Classic': 'verdure-lotus-classic.webp',
    'Verdure Lotus Luxury': 'verdure-lotus-luxury.webp',
    'Phoenix Cruise': 'phoenix-cruise.webp',
    'Orchid Trendy Cruise': 'orchid-trendy-cruise.webp',
    'Orchid Classic Cruise': 'orchid-classic-cruise.webp',
    'Fantasea Cruise': 'fantasea-cruise-3-star.webp',
    'Orchid Premium': 'orchid-premium.webp',
    'Velar of the Sea': 'velar-of-the-sea.webp',
    'Celina of the Sea': 'celina-of-the-sea.webp',
    'Sea Coral': 'sea-coral.webp',
    'Aqua Legend Cruise': 'aqua-legend-cruise.webp',
    'Tulip Cruise': 'tulip-cruise.webp',
    'Catherine Cruise': 'catherine-cruise.webp',
    'Star Light Cruise': 'star-light-cruise.webp',
    'La Casta Star': 'la-casta-star.webp',
    'Grand Pioneers': 'grand-pioneers.webp',
    'Ruby Cruise': 'ruby-cruise.webp',
    'La Pandora': 'la-pandora.webp',
    'Athena Cruise': 'athena-cruise.webp',
    'Signature Cruise': 'signature-cruise-bai-tu-long.webp',
}

path = Path('cruises.html')
html = path.read_text(encoding='utf-8')

for name, image in mapping.items():
    if f'assets/cruises/{image}' in html:
        continue
    pattern = rf'(<div class="card">\s*<div class="body">\s*<span class="tag">.*?</span>\s*<h3>{re.escape(name)}</h3>)'
    replacement = (
        f'<div class="card">\n'
        f'  <div class="cruise-visual" style="padding:0;height:245px;overflow:hidden;background:#eef3f0;">\n'
        f'    <img src="assets/cruises/{image}" alt="{name}" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;display:block;">\n'
        f'  </div>\n'
        f'  <div class="body">\n'
        f'    <span class="tag">'
    )
    # Preserve the existing tag text by using a targeted insertion instead of replacing it.
    match = re.search(pattern, html, flags=re.S)
    if not match:
        raise RuntimeError(f'Cruise card not found: {name}')
    original = match.group(1)
    tag_match = re.search(r'(<span class="tag">.*?</span>\s*<h3>)' + re.escape(name) + r'(</h3>)', original, flags=re.S)
    if not tag_match:
        raise RuntimeError(f'Cruise heading not found: {name}')
    tag_block = tag_match.group(1)
    tag_text = tag_block.split('</span>')[0] + '</span>'
    new = (
        f'<div class="card">\n'
        f'  <div class="cruise-visual" style="padding:0;height:245px;overflow:hidden;background:#eef3f0;">\n'
        f'    <img src="assets/cruises/{image}" alt="{name}" loading="lazy" decoding="async" style="width:100%;height:100%;object-fit:cover;display:block;">\n'
        f'  </div>\n'
        f'  <div class="body">\n'
        f'    {tag_text}\n'
        f'    <h3>{name}</h3>'
    )
    html = html[:match.start()] + new + html[match.end():]

path.write_text(html, encoding='utf-8')
print('Injected catalogue images for all 28 cruise cards.')
