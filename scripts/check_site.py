from html.parser import HTMLParser
from pathlib import Path
class Page(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=set(); self.links=[]; self.images=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag=='a': self.links.append(a.get('href',''))
        if tag=='img': self.images.append(a)
text=Path('site/index.html').read_text()
p=Page();p.feed(text)
assert '<title>Taryn / Portfolio</title>' in text
assert {'personal','internship','skill','skill-modal'} <= p.ids
assert 'mailto:15201859355@163.com' in p.links
for link in p.links:
    if link.startswith('#') and len(link)>1: assert link[1:] in p.ids, link
for image in p.images:
    assert image.get('alt'), 'Image needs alternative text'
    src=image.get('src','')
    assert src.startswith('data:image/') or (Path('site')/src).is_file(), src
assert not any(x in text for x in ['localhost:', '127.0.0.1:', '/Users/', 'art_v2_'])
assert 'showModal()' in text and "closest('dialog').close()" in text
print('Portfolio content, links, assets and modal checks passed.')
