# -*- coding: utf-8 -*-
"""Unit tests for Garhwali Folklore, Folk Songs, Jagars, and Digital Archives."""

import unittest
from garhwali.culture.folklore import FolkloreTreasury, GarhwaliSong, DigitalArchiveSource


class TestGarhwaliFolklore(unittest.TestCase):
    """Test suite for Garhwali folk songs, jagars, and digital heritage archives."""

    def test_songs_list(self):
        songs = FolkloreTreasury.list_songs()
        self.assertEqual(len(songs), 45, "Should contain all 45 canonical Garhwali songs")
        self.assertIsInstance(songs[0], GarhwaliSong)

    def test_get_song(self):
        bedu = FolkloreTreasury.get_song("GSN-0001")
        self.assertIsNotNone(bedu)
        self.assertIn("बेडू पाको", bedu.title)
        self.assertIn("काफल", bedu.lyrics_sample)
        self.assertGreaterEqual(len(bedu.verses), 5)

        chaitwali = FolkloreTreasury.get_song("GSN-0002")
        self.assertIsNotNone(chaitwali)
        self.assertIn("चैतवाली", chaitwali.title)

        dhari = FolkloreTreasury.get_song("GSN-0005")
        self.assertIsNotNone(dhari)
        self.assertIn("धारी देवी", dhari.title)

        maletha = FolkloreTreasury.get_song("GSN-0010")
        self.assertIsNotNone(maletha)
        self.assertIn("माधो सिंह", maletha.title)

    def test_search_songs(self):
        negi_songs = FolkloreTreasury.search_songs("Negi")
        self.assertGreaterEqual(len(negi_songs), 2)

        jagar_songs = FolkloreTreasury.search_songs("जागर")
        self.assertGreaterEqual(len(jagar_songs), 2)

    def test_random_song(self):
        song = FolkloreTreasury.random_song()
        self.assertIsNotNone(song)
        self.assertIsInstance(song, GarhwaliSong)

    def test_digital_sources(self):
        sources = FolkloreTreasury.list_sources()
        self.assertGreaterEqual(len(sources), 5)
        self.assertIsInstance(sources[0], DigitalArchiveSource)

        src1 = FolkloreTreasury.get_source("SRC-001")
        self.assertIsNotNone(src1)
        self.assertIn("Uttarakhand Open University", src1.source)

    def test_stats(self):
        stats = FolkloreTreasury.stats()
        self.assertEqual(stats["total_folk_songs"], 45)
        self.assertGreaterEqual(stats["total_digital_sources"], 5)
        self.assertIn("song_genres", stats)


if __name__ == "__main__":
    unittest.main()
