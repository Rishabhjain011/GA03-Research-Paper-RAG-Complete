import re

class MetadataExtractor:
    def extract(self, text):
        year = re.search(r"(19|20)\d{2}", text)
        return {"year": int(year.group()) if year else None}
