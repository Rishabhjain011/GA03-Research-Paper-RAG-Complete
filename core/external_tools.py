import requests

class ArxivTool:
    def search(self, query):
        return requests.get(
            "http://export.arxiv.org/api/query",
            params={"search_query": query}
        ).text
