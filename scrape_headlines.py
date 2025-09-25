import requests
from bs4 import BeautifulSoup

# Step 1: URL choose karo
url = "https://www.bbc.com/news"   # Example news site

# Step 2: Request bhejna
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
html_content = response.text

# Step 3: Parse karna
soup = BeautifulSoup(html_content, "lxml")

# Step 4: Headlines nikalna (h2 tags se)
headlines = []
for tag in soup.find_all("h2"):
    text = tag.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)

# Step 5: File me save karna
with open("headlines.txt", "w", encoding="utf-8") as f:
    for i, h in enumerate(headlines, 1):
        f.write(f"{i}. {h}\n")

print("✅ Headlines saved in headlines.txt")
