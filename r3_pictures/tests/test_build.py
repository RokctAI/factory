"""Content-free tests for the R-3 picture generator. Run: python -m pytest r3_pictures/tests

The real pack slugs and picture words are private; these tests use a few
made-up slugs and words, so they check the engine, not the lessons.
"""
import json
import os
import re
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
import build  # noqa: E402

# Slugs that exercise the slug-driven rules (numbers, clocks, sums, cards).
SLUGS = ['numeral_37', 'name_forty_two', "3 o'clock", 'half_past_four', 'sum_7_plus_5', 'digital_7_15',
         'sticks_two_tens_five', 'groups_two_of_three', 'flard_43', 'word_zzz', 'card_six_plus_two']
TEXT = {'text': {'g_text:sentences': {'sentence_test_only': 'Qq zz.'}, 'g_text:lines': {}, 'g_text:titles': {},
                 'g_text:headings': {}, 'g_text:cards': {}, 'g_text:months': [], 'g_text:words': {}}}
FAST = ['g_letters', 'g_numbers', 'g_shapes', 'g_maths', 'g_text']


def norm(s):
    return re.sub('[^a-z0-9]+', '_', s.lower()).strip('_')


class Base(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.slugs = os.path.join(cls.tmp.name, 'slugs.json')
        with open(cls.slugs, 'w') as f:
            json.dump({'1': SLUGS}, f)
        cls.text = os.path.join(cls.tmp.name, 'text.json')
        with open(cls.text, 'w') as f:
            json.dump(TEXT, f)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()


class NoWordsInTheEngine(Base):
    """Without a text file, nothing a picture prints may come from the code:
    every printed word (two or more letters) must come from a slug name."""

    def test_printed_words_come_from_slugs(self):
        seen = set()
        rep = build.build(self.slugs, None, None, trace=seen.add, log=lambda *a: None)
        names = ' '.join(norm(s) for s in SLUGS + list(rep['drawn']) + list(rep['needs_text']) + list(rep['alias']))
        leaks = sorted(s for s in seen if len(re.findall('[A-Za-z]', s)) >= 2 and norm(s) not in names)
        self.assertEqual(leaks, [], 'words printed from the code; move them to the text file (content.words)')
        self.assertTrue(rep['needs_text'], 'pictures with words should wait for the text file')


class Pictures(Base):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.out = os.path.join(cls.tmp.name, 'out')
        cls.rep = build.build(cls.slugs, cls.text, cls.out, modules=FAST, check=True, log=lambda *a: None)

    def test_slug_rules_draw_the_pack_slugs(self):
        for s in ['numeral_37', 'name_forty_two', '3_o_clock', 'half_past_four', 'sum_7_plus_5', 'digital_7_15',
                  'sticks_two_tens_five', 'groups_two_of_three', 'flard_43', 'word_zzz', 'card_six_plus_two',
                  'sentence_test_only']:
            self.assertTrue(os.path.exists(os.path.join(self.out, s + '.svg')), s)

    def test_shared_style(self):
        for f in sorted(os.listdir(self.out))[:400]:
            svg = open(os.path.join(self.out, f), encoding='utf-8').read()
            root = ET.fromstring(svg)
            self.assertEqual(root.get('viewBox'), '0 0 200 200', f)
            g = root[0]
            self.assertEqual((g.get('stroke'), g.get('stroke-width'), g.get('fill')), ('#1F2A44', '6', 'none'), f)

    def test_fit_and_overlap_checks_pass(self):
        bad = [p for p in self.rep['problems'] if p[0] in ('xml', 'fit', 'overlap')]
        self.assertEqual(bad, [])

    def test_missing_words_skip_the_picture(self):
        rep = build.build(self.slugs, None, None, modules=FAST, log=lambda *a: None)
        self.assertIn('g_text:sentences', rep['absent_tables'])
        self.assertNotIn('sentence_test_only', rep['drawn'])
        self.assertIn('g_text:word', rep['needs_text'].get('word', []))
        self.assertNotIn('word', rep['drawn'])
        self.assertIn('sentence_test_only', self.rep['drawn'])

    def test_existing_slugs_are_not_written_again(self):
        with tempfile.TemporaryDirectory() as d:
            open(os.path.join(d, 'numeral_37.svg'), 'w').close()
            rep = build.build(self.slugs, self.text, None, existing=d, modules=FAST, log=lambda *a: None)
        self.assertNotIn('numeral_37', rep['drawn'])


if __name__ == '__main__':
    unittest.main()
