from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class PaperSection:
    """
    Represents a logical section of a research paper
    (e.g., Abstract, Introduction, Methods, Results)
    """
    section_name: str
    content: str


@dataclass
class Citation:
    """
    Represents a citation relationship between papers
    """
    cited_paper_title: str
    cited_authors: Optional[List[str]] = None
    cited_year: Optional[int] = None


@dataclass
class ResearchPaper:
    """
    Unified internal representation of a research paper
    """
    paper_id: str
    title: Optional[str]
    authors: Optional[List[str]]
    abstract: Optional[str]
    year: Optional[int]

    sections: List[PaperSection] = field(default_factory=list)
    references: List[Citation] = field(default_factory=list)

    full_text: Optional[str] = None
    venue: Optional[str] = None
    keywords: Optional[List[str]] = None
