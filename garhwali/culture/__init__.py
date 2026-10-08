# -*- coding: utf-8 -*-
"""Garhwali Culture, Lore, Literature, Bibliography, Geography, Deities, Surnames, Flora, Rituals & Folklore Package."""

from .calendar import GARHWALI_MONTHS, GARHWALI_RITUS, GARHWALI_DAYS, get_current_season
from .festivals import GARHWALI_FESTIVALS, list_festivals
from .literature import (
    FolkEpic,
    FolkPoem,
    GarhwaliAuthor,
    LiteratureTreasury,
    EPICS_DATA,
    POEMS_DATA,
    AUTHORS_DATA,
    poems,
    epics,
    authors,
)
from .bibliography import (
    GarhwaliBook,
    BibliographyTreasury,
    get_bibliography,
    search_books,
    get_book_by_id,
    get_works_in_garhwali,
    get_grammar_books,
)
from .places import GarhwaliPlace, PlacesTreasury
from .deities import GarhwaliDeity, DeitiesTreasury
from .surnames import GarhwaliSurname, SurnamesTreasury
from .flora import GarhwaliPlant, FloraTreasury
from .rituals import GarhwaliRitualItem, RitualsTreasury
from .folklore import GarhwaliSong, GarhwaliHoliSong, DigitalArchiveSource, FolkloreTreasury
from .books import (
    BookPage,
    GarhwaliDigitalBook,
    BooksCorpus,
    read_book_page,
    list_digital_books,
    get_digital_book,
    search_digital_books,
)

__all__ = [
    # Calendar & Festivals
    "GARHWALI_MONTHS",
    "GARHWALI_RITUS",
    "GARHWALI_DAYS",
    "get_current_season",
    "GARHWALI_FESTIVALS",
    "list_festivals",
    # Literature & Epics
    "FolkEpic",
    "FolkPoem",
    "GarhwaliAuthor",
    "LiteratureTreasury",
    "EPICS_DATA",
    "POEMS_DATA",
    "AUTHORS_DATA",
    "poems",
    "epics",
    "authors",
    # Bibliography
    "GarhwaliBook",
    "BibliographyTreasury",
    "get_bibliography",
    "search_books",
    "get_book_by_id",
    "get_works_in_garhwali",
    "get_grammar_books",
    # Sacred Geography & Places
    "GarhwaliPlace",
    "PlacesTreasury",
    # Local Deities & Shrines
    "GarhwaliDeity",
    "DeitiesTreasury",
    # Surnames, Clans & Social Concepts
    "GarhwaliSurname",
    "SurnamesTreasury",
    # Himalayan Ethnobotanical Flora
    "GarhwaliPlant",
    "FloraTreasury",
    # Temple Implements & Ritual Objects
    "GarhwaliRitualItem",
    "RitualsTreasury",
    # Folklore, Folk Songs & Archives
    "GarhwaliSong",
    "GarhwaliHoliSong",
    "DigitalArchiveSource",
    "FolkloreTreasury",
    # Full-Text Digital Books & Page Reader
    "BookPage",
    "GarhwaliDigitalBook",
    "BooksCorpus",
    "read_book_page",
    "list_digital_books",
    "get_digital_book",
    "search_digital_books",
]
