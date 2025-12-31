class CitationGraph:
    def __init__(self):
        self.graph = {}

    def add(self, paper_id, citations):
        self.graph[paper_id] = citations
