# 🕵️‍♂️ DarkNet Leak Scanner

A Tor-based OSINT tool for discovering leaked emails on the darknet. It scrapes `.onion` sites, indexes email leaks into a SQLite database, sends real-time alerts, and provides a web dashboard via Streamlit.

---

## 🔧 Features

- ✅ Scrapes `.onion` pages over Tor
- ✅ Detects both standard and obfuscated email formats
- ✅ Stores leak metadata (email, URL, timestamp) in SQLite
- ✅ Sends alert emails for sensitive matches (e.g., your domains)
- ✅ Auto-discovers new darknet links
- ✅ Visual frontend to filter/search data leaks

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/darknet-leak-scanner.git
cd darknet-leak-scanner
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up Tor

Ensure Tor is installed and running locally:

```bash
tor
```

Enable the control port (e.g. in `torrc`):

```conf
ControlPort 9051
CookieAuthentication 1
```

---

## 🕸️ Usage

### 🌐 Launch dashboard

```bash
python crawler/autoExpand.py
```

This:
- Expands `.onion` targets in `crawler/targets.txt`

### ▶ Run crawler & alert system

```bash
python main.py
```

This:
- Loads `.onion` targets from `crawler/targets.txt`
- Scrapes email leaks
- Stores results in `data/leaks.db`
- Sends email alerts based on matching terms

---

### 🌐 Launch dashboard

```bash
streamlit run app.py
```

> View leak records, search/filter by domain, and apply date ranges.

---

## 📂 Project Structure

```
.
├── main.py                    # Main crawler + alert execution
├── app.py                     # Streamlit dashboard
├── core/
│   ├── alert.py               # Alert logic (email triggers)
│   └── indexer.py             # DB initialization and storing leaks
├── crawler/
│   ├── scraper.py             # Web scraping via BeautifulSoup + Tor
│   ├── tor_connector.py       # Tor identity rotation and session mgmt
│   ├── autoExpand.py          # Expand your Targets automatically
│   └── targets.txt            # List of .onion URLs to crawl
├── data/
│   └── leaks.db               # SQLite DB (auto-created)
├── requirements.txt
└── README.md
```

---

## 🔐 Email Alerts

Update SMTP and recipient configs in `core/alert.py`:

```python
msg['From'] = "alert@yourdomain.com"
msg['To'] = "admin@yourdomain.com"
server.login("user", "pass")
```

---

## 📈 Future Ideas

- Hash-based breach correlation
- Integration with HaveIBeenPwned or similar APIs
- Alert webhook/Slack integration
- GPG-encrypted report exports

---

## ⚠️ Disclaimer

This tool is for **educational and ethical research** purposes only. Use responsibly and within legal boundaries. Accessing certain darknet content may be illegal in your jurisdiction.

---

## 🛠 Built With

- Python 3.11+
- [Tor Project](https://www.torproject.org/)
- Streamlit
- BeautifulSoup
- Stem (Tor Controller)
