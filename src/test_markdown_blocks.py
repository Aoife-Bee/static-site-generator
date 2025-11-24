import unittest
from markdown_blocks import (
BlockType, 
markdown_to_blocks,
block_to_block_type)

class TestMarkdownBlocks(unittest.TestCase):

    def test_markdown_to_blocks(self):
        text = """# This is a heading

        This is a paragraph

        - This is a list"""
        result = markdown_to_blocks(text)
        self.assertEqual(["# This is a heading", "This is a paragraph", "- This is a list"], result)

    def test_block_to_heading(self):
        block = "### This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)
    
    def test_block_to_code(self):
        block = """```
This is code
```"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_block_to_quote(self):
        block = """>this is
>a quote"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_block_to_unordered_list(self):
        block = """- this is
- an unordered"
- list of items"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ULIST)
    
    def test_unordered_list_fail(self):
        block = """- This is
- an unordered
list of items"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_block_to_ordered_list(self):
        block = """1. This is"
2. An ordered"
3. List of"
4. Items"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.OLIST)

    def test_ordered_list_fail(self):
        block = """1. This is
2. An ordered
3. List of
5. Items"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_block_to_paragraph(self):
        block = """#This is not a header
```not code```
>or a quote
- or an unordered
5. or ordered list"""
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)
    