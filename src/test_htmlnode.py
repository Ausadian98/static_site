import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"href": "https://nhl.com"})
        self.assertEqual(node.props_to_html(), ' href="https://nhl.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://nhl.com", "target": "_blank"})
        result = node.props_to_html()
        self.assertIn(' href="https://nhl.com"', result)
        self.assertIn(' target="_blank"', result)
        expected_length = len(' href="https://nhl.com"') + len(' target="_blank"')
        self.assertEqual(len(result), expected_length)


if __name__ == "__main__":
    unittest.main()
