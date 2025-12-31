from collections import Counter

class TrendAnalyzer:
    def analyze(self, papers):
        trends = {}
        for p in papers:
            year = p.get("year")
            if year:
                trends.setdefault(year, [])
                trends[year] += p.get("keywords", [])
        return {y: Counter(k).most_common(5) for y, k in trends.items()}

