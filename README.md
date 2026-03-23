# 📖 Word Frequency Analysis — The Great Gatsby

A text analytics project using Python and NLP techniques to analyze word
frequency patterns in F. Scott Fitzgerald's *The Great Gatsby*, scraped
directly from Project Gutenberg.

---

## 📌 Problem Statement

Which words define *The Great Gatsby*? Which characters dominate the narrative?
What themes emerge from raw word frequency data? This project answers these
through web scraping, NLP preprocessing, and data visualization.

---

## 📦 Data Source

- **Source:** [Project Gutenberg](https://www.gutenberg.org/files/64317/64317-0.txt)
- **Book:** The Great Gatsby — F. Scott Fitzgerald
- **Size:** ~47,000 words (after cleaning)
- **No download needed** — text is scraped directly at runtime

---

## 🛠️ Tech Stack

| Layer           | Tool                            |
|-----------------|---------------------------------|
| Web Scraping    | Python Requests, BeautifulSoup  |
| Text Cleaning   | Python re, string               |
| NLP / Analysis  | Collections (Counter), custom stopwords |
| Visualization   | Matplotlib                      |
| Version Control | GitHub                          |

---

## 🧹 NLP Preprocessing Steps

1. Scraped raw `.txt` from Project Gutenberg
2. Stripped Gutenberg header/footer boilerplate
3. Lowercased all text
4. Removed punctuation and special characters using regex
5. Tokenized text by whitespace splitting
6. Removed 100+ custom stopwords (articles, prepositions, pronouns etc.)
7. Filtered tokens shorter than 3 characters

---

## 📊 Analysis Performed

- **Top 20 most frequent words** — bar chart with character vs thematic coloring
- **Thematic word group comparison** — Wealth, Characters, Emotions, Time & Past
- **Word frequency distribution** — log-scale curve (Zipf's Law pattern)
- **Character mention frequency** — Gatsby, Daisy, Tom, Nick, Jordan

---

## 💡 Key Insights

1. **Gatsby** is the most mentioned character, reinforcing his central narrative role
2. **Time & Past** is the dominant thematic group — aligns with the novel's nostalgia motif
3. **Wealth-related words** appear frequently, reflecting the novel's class commentary
4. Word frequency follows **Zipf's Law** — a small set of words account for most occurrences
5. **Daisy** is mentioned significantly less than Gatsby despite being the emotional center

---

## 📁 Project Structure

```
gatsby_analysis/
│
├── analysis.py          # Main scraping + NLP + visualization script
├── README.md            # This file
│
└── outputs/
    ├── 01_top_words.png
    ├── 02_themes.png
    ├── 03_frequency_distribution.png
    └── 04_character_mentions.png
```

---

## ▶️ How to Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/gatsby-word-frequency

# 2. Install dependencies
pip install requests beautifulsoup4 matplotlib

# 3. Run the analysis (scrapes + cleans + visualizes in one go)
python analysis.py
```

---

## 🔗 Connect
Made by Ayush Singh
