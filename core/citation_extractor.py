import re

class CitationExtractor:
    def extract(self, text):
        return [l for l in text.split("\n") if re.match(r"\[\d+\]", l)]
