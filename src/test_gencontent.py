import unittest
from gencontent import extract_title


class TestGenContent(unittest.TestCase):
    def test_extract_title(self):
        text = """Nov 24th
# This is the title 

here is the body text"""
        title = extract_title(text)
        self.assertEqual("This is the title", title)

    def test_multiple_titles(self):
        text = """# This is the title
# this is not the title
### this is DEFINITELY not the title"""
        title = extract_title(text)
        self.assertEqual("This is the title", title)

    def test_no_title(self):
        text = """## This is a subtitle"""
        self.assertRaises(Exception, extract_title, text)

    def test_title_typo(self):
        text = """#This is a title"""
        self.assertRaises(Exception, extract_title, text)