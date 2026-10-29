"""Assembla gli approfondimenti editoriali nella pagina statica, senza dipendenze."""
from pathlib import Path

root = Path(__file__).parent
page = root / 'dist/index.html'
html = page.read_text(encoding='utf-8')
start, end = '<!-- TOPICS START -->', '<!-- TOPICS END -->'
topics = (root / 'topics.html').read_text(encoding='utf-8')
photos = {
 'cute-lunghezze': ('vita-al-lavoro-v2.png', 'Vita osserva le lunghezze di una cliente, rielaborazione dalla fotografia originale', 'L’attenzione comincia dai dettagli.', 'landscape'),
 'caduta-rottura': ('vita-ritratto-v2.png', 'Ritratto di Vita in salone, rielaborato dalle fotografie originali', 'Uno sguardo attento. Prima di scegliere.', 'portrait'),
 'detersione': ('be6db46e4615122c.jpg', 'Vita nella copertina originale del Reel Shampoo a secco o borotalco', 'I consigli di Vita, dalla sua voce.', 'original'),
 'cambio-stagione': ('d13a02a9e1ea2b39.jpg', 'Vita nella copertina originale del Reel sulla cura dopo l’estate', 'La tua professionista, stagione dopo stagione.', 'original')
}
for topic_id, (image, alt, caption, shape) in photos.items():
    section_start = topics.index(f'id="{topic_id}"')
    side_end = topics.index('</div>', section_start)
    figure = f'<figure class="chapter-photo photo-reveal reveal {shape}"><div class="photo-window"><img src="assets/{image}" alt="{alt}" loading="lazy" width="640" height="800" data-parallax></div><figcaption>{caption}</figcaption></figure>'
    topics = topics[:side_end] + figure + topics[side_end:]
topics = topics.replace('<img src="assets/hair.jpg" alt="Capelli castani luminosi, immagine del salone" width="2048" height="2560" loading="lazy">', '<img src="assets/vita-ritratto-v2.png" alt="Vita nel salone, ritratto rielaborato dalle foto originali" width="1122" height="1402" loading="lazy" data-parallax>')
topics = topics.replace('<div class="season-image reveal">', '<div class="season-image photo-reveal reveal">')
gallery = '<figure class="treatment-photo photo-reveal reveal"><div class="photo-window"><img src="assets/vita-al-lavoro-v2.png" alt="Vita al lavoro con una cliente, rielaborazione da una fotografia originale" loading="lazy" width="1536" height="1024" data-parallax></div><figcaption>Vita Sanfilippo · La cura, gesto dopo gesto.</figcaption></figure>'
topics = topics.replace('<div class="treatment-columns">', gallery + '<div class="treatment-columns">', 1)
facts = {
 'cute-lunghezze': '''<div class="topic-explainer"><h3>Detergere e condizionare sono gesti diversi.</h3><p>Lo shampoo si massaggia delicatamente sulla cute; durante il risciacquo scorre sulle lunghezze, che non hanno bisogno di essere strofinate con forza. Il balsamo aiuta a ridurre attrito e rottura del capello. Da questi gesti di base possiamo partire per rivedere la tua routine.</p><a class="reading-reference" href="https://www.aad.org/public/everyday-care/hair-scalp-care/hair/habits-that-damage-hair" target="_blank" rel="noopener noreferrer">Per approfondire: indicazioni generali AAD sulla cura dei capelli ↗</a></div>''',
 'caduta-rottura': '''<div class="topic-explainer"><h3>Due fenomeni da non confondere.</h3><p>La caduta riguarda il distacco del capello; la rottura riguarda il fusto, che si spezza. Un capello danneggiato è più fragile e può rompersi più facilmente. Sono aspetti diversi: osservare dei capelli sulla spazzola, da solo, non basta a stabilire la causa.</p><p>Se noti una perdita insolita o un diradamento, il riferimento per chiarirne le cause è il dermatologo. In salone ci concentriamo sulla cura cosmetica e sulle abitudini che accompagnano i tuoi capelli.</p><a class="reading-reference" href="https://www.aad.org/public/diseases/hair-loss/insider/shedding/" target="_blank" rel="noopener noreferrer">Per approfondire: AAD, caduta e perdita dei capelli ↗</a></div>''',
 'dopo-estate': '''<div class="topic-explainer"><h3>Preparare la cura, anche prima delle vacanze.</h3><p>Esposizione solare e piscina possono contribuire a rendere i capelli secchi e fragili. Proteggerli dal sole e risciacquarli dopo il nuoto sono attenzioni da considerare nella routine estiva. Al rientro, raccontami come li senti: la scelta dei trattamenti parte dalle esigenze che osserviamo insieme.</p><a class="reading-reference" href="https://www.aad.org/public/everyday-care/hair-scalp-care/hair/summer-hair-care" target="_blank" rel="noopener noreferrer">Per approfondire: AAD, cura dei capelli in estate ↗</a></div>''',
 'detersione': '''<div class="topic-explainer"><h3>Shampoo a secco: cosa fa davvero?</h3><p>Assorbe l’olio in eccesso e può rendere i capelli più freschi nell’aspetto tra un lavaggio e l’altro. Non deterge, però, come shampoo e acqua: non sostituisce il lavaggio regolare. La quantità, la zona di applicazione e le istruzioni del prodotto contano.</p><p>Una polvere per il corpo non va considerata automaticamente equivalente a un prodotto formulato per i capelli. Nel Reel trovi la spiegazione di Vita; in consulenza possiamo parlare dei prodotti che già utilizzi e del ruolo che hanno nella tua routine.</p><a class="reading-reference" href="https://www.aad.org/public/everyday-care/hair-scalp-care/hair/dry-shampoo-best-results" target="_blank" rel="noopener noreferrer">Per approfondire: AAD, uso dello shampoo a secco ↗</a></div>'''
}
for topic_id, addition in facts.items():
    marker = f'id="{topic_id}"'
    section_start = topics.index(marker)
    link_at = topics.index('<a class="text-link"', section_start)
    topics = topics[:link_at] + addition + topics[link_at:]
fragment = start + '\n' + topics + '\n' + end + '\n'
if start in html:
    before, rest = html.split(start, 1)
    _, after = rest.split(end, 1)
    html = before + fragment.rstrip('\n') + after
else:
    target = '<section class="journal section" id="consigli">'
    assert target in html
    html = html.replace(target, fragment + target, 1)
if 'href="topics.css"' not in html:
    html = html.replace('<link rel="stylesheet" href="style.css">', '<link rel="stylesheet" href="style.css"><link rel="stylesheet" href="topics.css">', 1)
if 'href="motion.css"' not in html:
    html = html.replace('<link rel="stylesheet" href="topics.css">', '<link rel="stylesheet" href="topics.css"><link rel="stylesheet" href="motion.css">', 1)
html = html.replace('<a href="#consigli">I consigli di Vita</a>', '<a href="#approfondimenti">Gli argomenti di Vita</a>')
page.write_text(html, encoding='utf-8')
print('Approfondimenti assemblati: 6 argomenti, navigazione interna e fonti Instagram.')
