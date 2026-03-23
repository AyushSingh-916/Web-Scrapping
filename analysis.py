# ============================================================
# Word Frequency Analysis — The Great Gatsby
# By F. Scott Fitzgerald | Source: Project Gutenberg
# Tools: Python, Requests, BeautifulSoup, NLP, Matplotlib
# ============================================================

import re
import string
import requests
from collections import Counter
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

# ── Config ───────────────────────────────────────────────────
URL        = "https://www.gutenberg.org/files/64317/64317-0.txt"
BOOK_TITLE = "The Great Gatsby"
AUTHOR     = "F. Scott Fitzgerald"
TOP_N      = 20       # top N words to display
OUTPUT_DIR = "outputs"

import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Color palette ────────────────────────────────────────────
GOLD  = "#C9A84C"
GREEN = "#2E7D4F"
DARK  = "#1a1a2e"

# ============================================================
# STEP 1 — SCRAPE TEXT FROM PROJECT GUTENBERG
# ============================================================
print("=" * 55)
print(f"  {BOOK_TITLE} — Word Frequency Analysis")
print("=" * 55)
print(f"\n[1] Scraping text from Project Gutenberg...")

response = requests.get(URL, timeout=15)
response.encoding = "utf-8"
raw_text = response.text

print(f"    ✅ Downloaded {len(raw_text):,} characters")

# ============================================================
# STEP 2 — EXTRACT CLEAN BOOK TEXT
# (Strip Gutenberg header/footer boilerplate)
# ============================================================
print("\n[2] Extracting book content...")

start_marker = "THE GREAT GATSBY"
end_marker   = "End of the Project Gutenberg"

start_idx = raw_text.find(start_marker)
end_idx   = raw_text.find(end_marker)

if start_idx != -1 and end_idx != -1:
    book_text = raw_text[start_idx:end_idx]
else:
    book_text = raw_text   # fallback: use full text

print(f"    ✅ Extracted {len(book_text):,} characters of book content")

# ============================================================
# STEP 3 — DATA CLEANING & NLP PREPROCESSING
# ============================================================
print("\n[3] Cleaning and preprocessing text...")

# 3.1 Lowercase
text = book_text.lower()

# 3.2 Remove punctuation and special characters
text = re.sub(r"[^a-z\s]", " ", text)

# 3.3 Tokenize (split into words)
tokens = text.split()

total_raw_words = len(tokens)
print(f"    Raw word count     : {total_raw_words:,}")

# 3.4 Stopword removal (comprehensive custom list)
STOPWORDS = {
    "the","a","an","and","or","but","in","on","at","to","for",
    "of","with","as","is","was","are","were","be","been","being",
    "have","has","had","do","does","did","will","would","shall",
    "should","may","might","must","can","could","it","its","it's",
    "this","that","these","those","i","me","my","myself","we","our",
    "ours","ourselves","you","your","yours","yourself","he","him",
    "his","himself","she","her","hers","herself","they","them",
    "their","theirs","themselves","what","which","who","whom",
    "when","where","why","how","all","each","every","both","few",
    "more","most","other","some","such","no","not","only","same",
    "so","than","too","very","just","about","up","out","if","then",
    "there","here","from","by","into","through","during","before",
    "after","above","below","between","own","again","further","once",
    "said","mr","mrs","one","two","like","over","back","well","down",
    "now","still","even","also","us","him","got","go","came","come",
    "went","get","know","think","see","look","say","tell","make",
    "take","want","seem","felt","knew","could","long","never","little",
    "old","new","much","away","around","across","without","within",
    "i'm","i've","i'd","i'll","don't","didn't","wasn't","weren't",
    "couldn't","wouldn't","shouldn't","hadn't","hasn't","haven't",
    "doesn't","isn't","aren't","won't","let","put","ve","ll","re","d","s","t"
}

filtered_tokens = [w for w in tokens if w not in STOPWORDS and len(w) > 2]

print(f"    After stopword removal: {len(filtered_tokens):,} words")
print(f"    Unique words           : {len(set(filtered_tokens)):,}")

# ============================================================
# STEP 4 — WORD FREQUENCY ANALYSIS
# ============================================================
print("\n[4] Computing word frequencies...")

word_freq   = Counter(filtered_tokens)
top_words   = word_freq.most_common(TOP_N)
top_df_words = [w for w, _ in top_words]
top_df_counts= [c for _, c in top_words]

print(f"\n    Top {TOP_N} Most Frequent Words:")
print(f"    {'Rank':<6} {'Word':<18} {'Count':<8}")
print("    " + "-" * 32)
for rank, (word, count) in enumerate(top_words, 1):
    print(f"    {rank:<6} {word:<18} {count:<8}")

# ── Thematic word groups ──────────────────────────────────────
THEME_WORDS = {
    "Wealth & Status" : ["money","rich","gold","silver","luxury","party","parties","mansion","estate","car","white","dress"],
    "Characters"      : ["gatsby","daisy","tom","nick","jordan","wilson","myrtle","wolfsheim","carraway"],
    "Emotions"        : ["love","dream","hope","afraid","happy","sad","lonely","excited","nervous","beautiful"],
    "Time & Past"     : ["time","past","future","old","young","ago","before","again","remember","night","day","year"],
}

print("\n    Thematic Word Counts:")
for theme, words in THEME_WORDS.items():
    count = sum(word_freq.get(w, 0) for w in words)
    print(f"    {theme:<22}: {count:,} occurrences")

# ============================================================
# STEP 5 — VISUALIZATIONS
# ============================================================
print("\n[5] Generating visualizations...")

# ── Chart 1: Top 20 Words Bar Chart ─────────────────────────
fig, ax = plt.subplots(figsize=(12, 7))
colors = [GOLD if w in THEME_WORDS["Characters"] else GREEN for w in top_df_words]

bars = ax.barh(top_df_words[::-1], top_df_counts[::-1], color=colors[::-1], edgecolor="white", linewidth=0.5)

for bar, count in zip(bars, top_df_counts[::-1]):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
            str(count), va="center", ha="left", fontsize=9, color="#444")

gold_patch  = mpatches.Patch(color=GOLD,  label="Character Name")
green_patch = mpatches.Patch(color=GREEN, label="Thematic Word")
ax.legend(handles=[gold_patch, green_patch], loc="lower right", fontsize=9)

ax.set_title(f"Top {TOP_N} Most Frequent Words\n{BOOK_TITLE} — {AUTHOR}",
             fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Frequency", fontsize=11)
ax.set_xlim(0, max(top_df_counts) * 1.15)
ax.spines[["top","right"]].set_visible(False)
ax.tick_params(axis="y", labelsize=10)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_top_words.png", dpi=150, bbox_inches="tight")
plt.show()
print(f"    ✅ Saved 01_top_words.png")


# ── Chart 2: Thematic Word Group Comparison ─────────────────
theme_counts = {
    theme: sum(word_freq.get(w, 0) for w in words)
    for theme, words in THEME_WORDS.items()
}
theme_labels = list(theme_counts.keys())
theme_values = list(theme_counts.values())
theme_colors = [GOLD, "#4A90D9", "#E67E22", GREEN]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(theme_labels, theme_values, color=theme_colors, edgecolor="white", linewidth=0.8, width=0.5)

for bar, val in zip(bars, theme_values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
            str(val), ha="center", va="bottom", fontsize=10, fontweight="bold")

ax.set_title(f"Thematic Word Group Frequency\n{BOOK_TITLE} — {AUTHOR}",
             fontsize=14, fontweight="bold", pad=15)
ax.set_ylabel("Total Word Count", fontsize=11)
ax.set_ylim(0, max(theme_values) * 1.15)
ax.spines[["top","right"]].set_visible(False)
ax.tick_params(axis="x", labelsize=9)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_themes.png", dpi=150, bbox_inches="tight")
plt.show()
print(f"    ✅ Saved 02_themes.png")


# ── Chart 3: Word Frequency Distribution (Log scale) ────────
all_counts = sorted(word_freq.values(), reverse=True)[:200]
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(range(1, len(all_counts)+1), all_counts, color=GOLD, linewidth=2)
ax.fill_between(range(1, len(all_counts)+1), all_counts, alpha=0.2, color=GOLD)
ax.set_yscale("log")
ax.set_title(f"Word Frequency Distribution (Top 200 Words)\n{BOOK_TITLE}",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Word Rank", fontsize=11)
ax.set_ylabel("Frequency (log scale)", fontsize=11)
ax.spines[["top","right"]].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_frequency_distribution.png", dpi=150, bbox_inches="tight")
plt.show()
print(f"    ✅ Saved 03_frequency_distribution.png")


# ── Chart 4: Character Mention Comparison ───────────────────
characters = {
    "Gatsby" : word_freq.get("gatsby", 0),
    "Daisy"  : word_freq.get("daisy", 0),
    "Tom"    : word_freq.get("tom", 0),
    "Nick"   : word_freq.get("nick", 0),
    "Jordan" : word_freq.get("jordan", 0),
}
char_colors = [GOLD, "#E8A0BF", "#4A90D9", GREEN, "#9B59B6"]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(characters.keys(), characters.values(),
              color=char_colors, edgecolor="white", linewidth=0.8, width=0.5)

for bar, val in zip(bars, characters.values()):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            str(val), ha="center", va="bottom", fontsize=11, fontweight="bold")

ax.set_title(f"Character Mention Frequency\n{BOOK_TITLE} — {AUTHOR}",
             fontsize=14, fontweight="bold", pad=15)
ax.set_ylabel("Mentions", fontsize=11)
ax.set_ylim(0, max(characters.values()) * 1.18)
ax.spines[["top","right"]].set_visible(False)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_character_mentions.png", dpi=150, bbox_inches="tight")
plt.show()
print(f"    ✅ Saved 04_character_mentions.png")


# ============================================================
# STEP 6 — SUMMARY INSIGHTS
# ============================================================
most_common_word, most_common_count = top_words[0]
top_character = max(characters, key=characters.get)
top_theme     = max(theme_counts, key=theme_counts.get)

print("\n" + "=" * 55)
print("  KEY INSIGHTS")
print("=" * 55)
print(f"  Total words scraped       : {total_raw_words:,}")
print(f"  Words after cleaning      : {len(filtered_tokens):,}")
print(f"  Unique words              : {len(set(filtered_tokens)):,}")
print(f"  Most frequent word        : '{most_common_word}' ({most_common_count}x)")
print(f"  Most mentioned character  : {top_character.title()} ({characters[top_character]}x)")
print(f"  Dominant theme group      : {top_theme}")
print(f"\n  All charts saved to /{OUTPUT_DIR}/")
print("=" * 55)
