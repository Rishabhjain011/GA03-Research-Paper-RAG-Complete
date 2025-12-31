from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ResearchPaper:
    paper_id: str
    title: str
    authors: List[str]
    abstract: str
    year: Optional[int]
    keywords: List[str]
    references: List[str]
    full_text: str
