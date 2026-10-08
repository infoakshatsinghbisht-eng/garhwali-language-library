# -*- coding: utf-8 -*-
"""
Folklore, Traditional Songs, Classical Holi/Chaiti Ballads, and Musical Heritage of Garhwal.

Includes:
1. Traditional Folk, Jagar & Recorded Songs Corpus (GSN-0001 to GSN-0020).
2. Classical & Semi-Classical Baithki, Khadi & Chaiti Holi Songs.
3. Digital Archive Sources (SRC-001 to SRC-007) for heritage preservation.
"""

import json
import os
import random
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, field


@dataclass
class GarhwaliSong:
    id: str
    title: str
    roman: str
    artist: str
    genre: str
    corpus: str
    theme: str
    lyrics_sample: str
    verses: List[str]
    english_translation: str
    cultural_context: str
    source_url: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "roman": self.roman,
            "artist": self.artist,
            "genre": self.genre,
            "corpus": self.corpus,
            "theme": self.theme,
            "lyrics_sample": self.lyrics_sample,
            "verses": self.verses,
            "english_translation": self.english_translation,
            "cultural_context": self.cultural_context,
            "source_url": self.source_url
        }


@dataclass
class GarhwaliHoliSong:
    id: int
    title: str
    form: str
    raag: str
    theme: str
    verses: List[str]
    english_translation: str
    archive_source: str
    source_url: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "form": self.form,
            "raag": self.raag,
            "theme": self.theme,
            "verses": self.verses,
            "english_translation": self.english_translation,
            "archive_source": self.archive_source,
            "source_url": self.source_url
        }


@dataclass
class DigitalArchiveSource:
    id: str
    source: str
    what_it_provides: str
    url: str
    preservation_status: str

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "source": self.source,
            "what_it_provides": self.what_it_provides,
            "url": self.url,
            "preservation_status": self.preservation_status
        }


_SONGS_CACHE: Optional[List[GarhwaliSong]] = None
_HOLI_SONGS_CACHE: Optional[List[GarhwaliHoliSong]] = None
_SOURCES_CACHE: Optional[List[DigitalArchiveSource]] = None


def _load_songs() -> List[GarhwaliSong]:
    global _SONGS_CACHE
    if _SONGS_CACHE is not None:
        return _SONGS_CACHE

    path = os.path.join(os.path.dirname(__file__), 'data', 'songs.json')
    if not os.path.exists(path):
        _SONGS_CACHE = []
        return _SONGS_CACHE

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        _SONGS_CACHE = [
            GarhwaliSong(
                id=item['id'],
                title=item['title'],
                roman=item['roman'],
                artist=item['artist'],
                genre=item['genre'],
                corpus=item.get('corpus', ''),
                theme=item['theme'],
                lyrics_sample=item['lyrics_sample'],
                verses=item['verses'],
                english_translation=item['english_translation'],
                cultural_context=item['cultural_context'],
                source_url=item.get('source_url', '')
            )
            for item in data
        ]
    return _SONGS_CACHE


def _load_holi_songs() -> List[GarhwaliHoliSong]:
    global _HOLI_SONGS_CACHE
    if _HOLI_SONGS_CACHE is not None:
        return _HOLI_SONGS_CACHE

    path = os.path.join(os.path.dirname(__file__), 'data', 'holi_songs.json')
    if not os.path.exists(path):
        _HOLI_SONGS_CACHE = []
        return _HOLI_SONGS_CACHE

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        _HOLI_SONGS_CACHE = [
            GarhwaliHoliSong(
                id=item['id'],
                title=item['title'],
                form=item['form'],
                raag=item['raag'],
                theme=item['theme'],
                verses=item['verses'],
                english_translation=item['english_translation'],
                archive_source=item.get('archive_source', ''),
                source_url=item.get('source_url', '')
            )
            for item in data
        ]
    return _HOLI_SONGS_CACHE


def _load_sources() -> List[DigitalArchiveSource]:
    global _SOURCES_CACHE
    if _SOURCES_CACHE is not None:
        return _SOURCES_CACHE

    path = os.path.join(os.path.dirname(__file__), 'data', 'digital_sources.json')
    if not os.path.exists(path):
        _SOURCES_CACHE = []
        return _SOURCES_CACHE

    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        _SOURCES_CACHE = [
            DigitalArchiveSource(
                id=item['id'],
                source=item['source'],
                what_it_provides=item['what_it_provides'],
                url=item['url'],
                preservation_status=item['preservation_status']
            )
            for item in data
        ]
    return _SOURCES_CACHE


class FolkloreTreasury:
    """Master access interface for Garhwali folk songs, jagars, Holi/Chaiti ragas, and digital archives."""

    @staticmethod
    def list_songs(genre: Optional[str] = None) -> List[GarhwaliSong]:
        """List all catalogued Garhwali folk songs, optionally filtered by genre."""
        songs = _load_songs()
        if genre:
            g_low = genre.lower()
            return [s for s in songs if g_low in s.genre.lower()]
        return songs

    @staticmethod
    def get_jagar_songs() -> List[GarhwaliSong]:
        """Retrieve all sacred Jagar songs and divine spirit invocations."""
        return [s for s in _load_songs() if "jagar" in s.genre.lower() or "जागर" in s.title]

    @staticmethod
    def get_mangal_geet() -> List[GarhwaliSong]:
        """Retrieve all sacred nuptial Mangal Geet and wedding hymns."""
        return [s for s in _load_songs() if "mangal" in s.genre.lower() or "मांगल" in s.title]

    @staticmethod
    def get_pawada_songs() -> List[GarhwaliSong]:
        """Retrieve historical heroic martial Pawada ballads."""
        return [s for s in _load_songs() if "pawada" in s.genre.lower() or "पवाड़ा" in s.title or "भड़ौला" in s.title]

    @staticmethod
    def get_khudei_songs() -> List[GarhwaliSong]:
        """Retrieve traditional nostalgic Khudei songs of mountain longing."""
        return [s for s in _load_songs() if "khudei" in s.genre.lower() or "खुदेड़" in s.title or "viraha" in s.genre.lower()]

    @staticmethod
    def get_dance_songs() -> List[GarhwaliSong]:
        """Retrieve community dance songs (Thadya, Chounphula, Jhumelo, Chhori)."""
        return [
            s for s in _load_songs()
            if any(k in s.genre.lower() for k in ("dance", "thadya", "chounphula", "jhumelo", "chhori"))
        ]

    @staticmethod
    def get_ritu_geet() -> List[GarhwaliSong]:
        """Retrieve seasonal songs (Chaiti, Basanti, Ritu-Geet)."""
        return [
            s for s in _load_songs()
            if any(k in s.genre.lower() for k in ("chaiti", "spring", "ritu-geet", "seasonal"))
        ]

    @staticmethod
    def get_song(song_id: str) -> Optional[GarhwaliSong]:
        """Retrieve a folk song by ID (e.g. 'GSN-0001') or title."""
        id_clean = song_id.upper().strip()
        for s in _load_songs():
            if s.id.upper() == id_clean or id_clean in s.title or id_clean in s.roman.upper():
                return s
        return None

    @staticmethod
    def search_songs(query: str) -> List[GarhwaliSong]:
        """Search songs across title, artist, genre, theme, and verses."""
        if not query:
            return _load_songs()
        q_low = query.strip().lower()
        res = []
        for s in _load_songs():
            if (
                q_low in s.id.lower()
                or q_low in s.title.lower()
                or q_low in s.roman.lower()
                or q_low in s.artist.lower()
                or q_low in s.genre.lower()
                or q_low in s.theme.lower()
                or q_low in s.english_translation.lower()
                or any(q_low in v.lower() for v in s.verses)
            ):
                res.append(s)
        return res

    @staticmethod
    def random_song() -> Optional[GarhwaliSong]:
        """Return a random catalogued folk song."""
        songs = _load_songs()
        return random.choice(songs) if songs else None

    @staticmethod
    def list_holi_songs(form: Optional[str] = None, raag: Optional[str] = None) -> List[GarhwaliHoliSong]:
        """List classical Garhwali Holi songs, optionally filtered by form or raag."""
        songs = _load_holi_songs()
        if form:
            f_low = form.lower()
            songs = [s for s in songs if f_low in s.form.lower()]
        if raag:
            r_low = raag.lower()
            songs = [s for s in songs if r_low in s.raag.lower()]
        return songs

    @staticmethod
    def get_holi_song(song_id: Union[int, str]) -> Optional[GarhwaliHoliSong]:
        """Retrieve a Holi song by integer ID or title substring."""
        songs = _load_holi_songs()
        if isinstance(song_id, int) or (isinstance(song_id, str) and song_id.isdigit()):
            target_id = int(song_id)
            for s in songs:
                if s.id == target_id:
                    return s
        s_str = str(song_id).strip()
        for s in songs:
            if s_str in s.title:
                return s
        return None

    @staticmethod
    def search_holi_songs(query: str) -> List[GarhwaliHoliSong]:
        """Search Holi songs across title, form, raag, theme, verses, and translation."""
        if not query:
            return _load_holi_songs()
        q_low = query.strip().lower()
        res = []
        for s in _load_holi_songs():
            if (
                q_low in s.title.lower()
                or q_low in s.form.lower()
                or q_low in s.raag.lower()
                or q_low in s.theme.lower()
                or q_low in s.english_translation.lower()
                or any(q_low in v.lower() for v in s.verses)
            ):
                res.append(s)
        return res

    @staticmethod
    def list_sources() -> List[DigitalArchiveSource]:
        """List active digital heritage and archival repositories."""
        return _load_sources()

    @staticmethod
    def get_source(source_id: str) -> Optional[DigitalArchiveSource]:
        """Retrieve digital source by ID (e.g. 'SRC-001') or name."""
        id_clean = source_id.upper().strip()
        for src in _load_sources():
            if src.id.upper() == id_clean or id_clean in src.source.lower():
                return src
        return None

    @staticmethod
    def stats() -> Dict[str, Any]:
        """Summary metrics of Garhwali digital folklore, folk songs, and Holi corpus."""
        songs = _load_songs()
        holi_songs = _load_holi_songs()
        sources = _load_sources()
        from collections import Counter
        genre_counts = Counter(s.genre for s in songs)
        return {
            "total_folk_songs": len(songs),
            "total_holi_songs": len(holi_songs),
            "total_digital_sources": len(sources),
            "song_genres": dict(genre_counts)
        }
