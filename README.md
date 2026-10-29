# Vita Sanfilippo Parrucchieri

Sito di presentazione per Vita Sanfilippo, professionista e consulente per la cura cosmetica di cute e capelli a Ravanusa.

**Progetto completo e pronto da consegnare:** HTML, CSS, JavaScript, immagini e contenuti editoriali. Nessuna dipendenza npm, database o chiave API.

## Sito pubblico

https://matteopiazzabusiness-ui.github.io/vita-sanfilippo/

Accessibile senza account, ospitato su GitHub Pages.

## Avvio in un minuto

```sh
git clone https://github.com/matteopiazzabusiness-ui/vita-sanfilippo.git
cd vita-sanfilippo
python -m http.server 4173 --directory dist --bind 127.0.0.1
```

Apri **http://127.0.0.1:4173**. Con alcuni sistemi il comando Python è `python3` oppure `py`.

La cartella **`dist/` è già pronta da pubblicare**: non occorre compilare nulla.

## Contenuti e funzioni

- Presentazione di Vita e percorso Ascolto → Analisi → Cura.
- Consulenza con selezione dell’esigenza e messaggio WhatsApp contestuale.
- Sei approfondimenti: cute e lunghezze, caduta e rottura, cura dopo l’estate, detersione, cambio di stagione, trattamenti personalizzati.
- Fotografie di Vita, copertine originali e collegamenti ai Reel Instagram.
- Ingressi progressivi, parallasse fotografico leggero, foto laterali sticky e avanzamento di lettura.
- Menu mobile, FAQ accessibili, contatti e indicazioni stradali.
- Supporto a `prefers-reduced-motion`, immagini lazy loading e scorrimento nativo.

## Struttura

```text
dist/
  index.html       Pagina completa pronta alla pubblicazione
  style.css        Identità visiva e layout responsive
  topics.css       Approfondimenti editoriali
  motion.css       Fotografie e animazioni di scroll
  app.js           Menu, consulenza e interazioni
  assets/          Logo, foto e copertine
topics.html        Sorgente dei sei approfondimenti
build-content.py   Assemblaggio editoriale opzionale
PHOTO-NOTES.md     Provenienza e rielaborazione delle fotografie
CONSEGNA.md        Scheda di consegna e testo da inviare
```

## Modificare il sito

Per cambiare testi generali, contatti o collegamenti, modifica `dist/index.html`. Il messaggio WhatsApp e il numero sono presenti anche in `dist/app.js`.

Per cambiare gli approfondimenti, modifica `topics.html` e le integrazioni in `build-content.py`, poi esegui:

```sh
python build-content.py
```

Il comando è idempotente: aggiorna il blocco degli approfondimenti senza duplicarlo. Le immagini dei capitoli sono configurate nella mappa `photos` del file Python. Non è necessario eseguirlo per pubblicare la versione inclusa.

## Pubblicazione

### Hosting statico / FTP

Carica **il contenuto** di `dist/` nella cartella pubblica del dominio. `index.html` deve trovarsi nella radice pubblica insieme a CSS, JavaScript e `assets/`.

### Netlify

Importa questo repository: `netlify.toml` imposta già `dist` come cartella pubblica. Nessun comando di build richiesto.

### Vercel

Importa il repository come progetto statico, seleziona il preset **Other**, lascia vuoto il comando di build e imposta **Output Directory: `dist`**.

### GitHub Pages

Il workflow è predisposto **solo per avvio manuale**. Per pubblicare:

1. Apri **Settings → Pages → Source → GitHub Actions**.
2. Apri **Actions → Publish GitHub Pages → Run workflow**.
3. Attendi il completamento e usa l’URL restituito dal deployment.

Il caricamento del repository non attiva automaticamente un nuovo sito pubblico. Configurazione basata sulla [documentazione ufficiale GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Fonti e fotografie

I temi e i contatti sono stati verificati sul [profilo Instagram ufficiale](https://www.instagram.com/vitaparrucchiera/) e sul [sito esistente](https://vitasanfilippo.socialbeautysalon.com/). Le spiegazioni generali di cura includono riferimenti AAD nei rispettivi approfondimenti. I Reel sono collegati, non copiati né trascritti.

Due fotografie sono rielaborazioni AI basate sulle immagini originali di Vita; dettagli in [PHOTO-NOTES.md](PHOTO-NOTES.md). Non vengono presentate come foto di risultati prima/dopo. Il logo originale è conservato.

## Prima della pubblicazione sul dominio definitivo

Aggiorna `og:image` e il campo `url` dei dati strutturati in `dist/index.html` con il dominio scelto. Attualmente indicano il sito pubblico GitHub Pages. Verifica inoltre la pagina privacy collegata e completa gli eventuali dati legali dell’attività.

Prezzi, orari e titoli professionali non verificati non sono stati aggiunti. Gli appuntamenti vengono concordati direttamente con il salone.
