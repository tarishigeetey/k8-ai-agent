from bs4 import BeautifulSoup
import logfire


def parse_html(file_path: str):
    """
    Parses HTML content using BeautifulSoup.
    Cleans scripts, styles, and extracts readable text for RAG.
    """
    with logfire.span("📄 HTML Parsing", filename=file_path):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            soup = BeautifulSoup(
                content, "html.parser"
            )  # Enables us to parse the HTML content and extract text while ignoring scripts, styles, and metadata.

            # 1. Remove Junk (Scripts, Styles, Metadata)
            for script in soup(["script", "style", "meta", "noscript"]):
                script.decompose()

            # 2. Extract Text
            text = soup.get_text(separator="\n")

            # 3. Clean Whitespace (Collapse multiple newlines)
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text_clean = "\n".join(chunk for chunk in chunks if chunk)

            return text_clean
        except Exception as e:
            logfire.error(f"❌ HTML Parse Failed: {e}")
            raise e


# Notes : to extract website specific data, you can use BeautifulSoup to parse the HTML and extract the relevant information. You can also use libraries like Scrapy or Selenium for more complex scraping tasks.
# can also use crawl for ai or  firecrawl for ai to extract text from html and other formats.
