import unittest

from split_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_functionality(self):
        node = TextNode("Text with `code block` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "Text with ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "code block")
        self.assertEqual(result[1].text_type, TextType.CODE)
        self.assertEqual(result[2].text, " here")
        self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_multiple_pairs(self):
        node = TextNode("Text with **Multiple pairs** of **types**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "Text with ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "Multiple pairs")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " of ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "types")
        self.assertEqual(result[3].text_type, TextType.BOLD)

    def test_multiple_delimiter_types(self):
        # Start with text
        node = TextNode("Text with **bold** and _italic_", TextType.TEXT)

        # First split by bold
        intermediate_result = split_nodes_delimiter([node], "**", TextType.BOLD)
        # Then split by italic (using the results from the previous split)
        final_result = split_nodes_delimiter(intermediate_result, "_", TextType.ITALIC)

        self.assertEqual(len(final_result), 4)
        self.assertEqual(final_result[0].text, "Text with ")
        self.assertEqual(final_result[0].text_type, TextType.TEXT)
        self.assertEqual(final_result[1].text, "bold")
        self.assertEqual(final_result[1].text_type, TextType.BOLD)
        self.assertEqual(final_result[2].text, " and ")
        self.assertEqual(final_result[2].text_type, TextType.TEXT)
        self.assertEqual(final_result[3].text, "italic")
        self.assertEqual(final_result[3].text_type, TextType.ITALIC)

    def test_empty_node_creation(self):
        node = TextNode("Text with _italic_", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)

        # Check if there's an empty node at the end
        self.assertEqual(len(result), 2)  # If empty nodes are created
        if len(result) == 3:
            self.assertEqual(result[2].text, "")
            self.assertEqual(result[2].text_type, TextType.TEXT)

    def test_missing_closing_delimiter(self):
        # Create a node with a missing closing delimiter
        node = TextNode("Text with **bold but no closing delimiter", TextType.TEXT)

        # The function should raise an exception
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_non_text_nodes_untouched(self):
        # Create a bold node that shouldn't be split even if it contains delimiters
        node = TextNode("This is already **bold** text", TextType.BOLD)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        # The node should remain unchanged
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is already **bold** text")
        self.assertEqual(result[0].text_type, TextType.BOLD)

    def test_delimiter_at_start_and_end(self):
        node = TextNode("**Bold at start** and **bold at end**", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 4)
        self.assertEqual(result[0].text, "")  # Empty node before first delimiter
        self.assertEqual(result[1].text, "Bold at start")
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[3].text, "bold at end")
