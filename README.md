# Timeline News - Live BBC News Pulse Dashboard

A Full-Stack application that automatically scrapes latest news from RSS feeds, performs thematic topic grouping using analytical algorithms, exposes structured endpoints via a Node.js API, and renders an interactive chronological news timeline on a web dashboard.

## Project Deployments
* **Frontend Web Application:** https://vercel.app
* **Backend Production API:** https://onrender.com
* **GitHub Repository:** https://github.com

---

## Architecture Overview

The system is built inside a monorepo structure, separated into three operational pipelines:
1. **Frontend:** Built using React and Vite. It styles a scannable dashboard using custom layout structures, requesting chronological data from the live backend server using Axios.
2. **Backend:** A Node.js and Express REST API that queries grouped news nodes stored inside an embedded SQLite base and outputs streamlined JSON structures to the clients.
3. **Scraper Pipeline:** A Python script utilizing feedparser to extract live feeds, perform text processing, and cluster related news items.

---

## Topic-Grouping Approach

For grouping similar incoming news into unique thematic timeline nodes, the Keyword/Word Overlap strategy was implemented.

### Selection Rationale
* **High Predictability:** Breaking news coverage shares distinctive proper nouns such as specific politician names, locations, and event tags. The overlap intersection yields deterministic groupings quickly without requiring heavy external matrix models.
* **Minimal Computational Overhead:** Runs instantaneously directly over built-in Python collection types, eliminating complex array multiplication or tensor runtime setup inside a resource-constrained server.

### Limitations
* **Synonym Blindness:** The overlap approach operates purely on exact word matches. If one article uses the keyword "Automobile" and another uses "Car", the system fails to discover their underlying semantic relationship.
* **Over-clustering on Common Terms:** Articles describing entirely different incidents might occasionally match and merge erroneously into a single cluster if generic high-frequency terms slip past the filtering threshold.

---

## News Sources
The automated data ingestion script connects to public news channels to aggregate pulse updates:
1. **BBC News - Home Feed:** http://bbci.co.uk
2. **BBC News - World Feed:** http://bbci.co.uk
3. **BBC News - Technology Feed:** http://bbci.co.uk

---

## Local Installation and Setup

### Prerequisites
* Node.js Installed (v16+)
* Python Installed (v3.9+)

### 1. Setup Backend Server
```bash
cd Backend
npm install
node server.js
```

### 2. Run Scraper Manually
```bash
cd Scraper
pip install feedparser
python scraper.py
```

### 3. Launch Frontend Client
```bash
cd Frontend
npm install
npm run dev
```

---

## API Endpoints Summary
* `GET /api/news` - Fetches chronological categorized historical items mapped to individual timeline rows.
* `POST /ingest/trigger` - Triggers the automated internal python scraper subprocess on-demand to fetch latest inputs.
