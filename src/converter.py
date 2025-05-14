from htmlnode import HTMLNode
from textnode import TextType


def text_node_to_html_node(text_node):
    match textnode.text_type:
        case TextType.BOLD:
            return HTMLNode("<b>")
