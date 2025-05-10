import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node_no_url = TextNode("Text", TextType.TEXT)
        node_explicit_none = TextNode("Text", TextType.TEXT, None)
        self.assertEqual(node_no_url, node_explicit_none)

    def test_different_text_types(self):
        node_bold = TextNode("Bold Text", TextType.BOLD)
        node_italic = TextNode("Italic Text", TextType.ITALIC)
        self.assertNotEqual(node_bold, node_italic)


if __name__ == "__main__":
    unittest.main()
