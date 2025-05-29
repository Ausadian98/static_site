from image_extraction import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for old_node in old_nodes:
        # If not a text node, just add it as is
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        chunks = process_delimiters(old_node.text, delimiter, text_type)
        result.extend(chunks)

    return result


def process_delimiters(text, delimiter, text_type):
    if delimiter not in text:
        return [TextNode(text, TextType.TEXT)] if text else []

    parts = []
    remaining_text = text

    while delimiter in remaining_text:
        opening_index = remaining_text.find(delimiter)

        parts.append(TextNode(remaining_text[:opening_index], TextType.TEXT))

        start_of_search = opening_index + len(delimiter)
        closing_index = remaining_text.find(delimiter, start_of_search)

        if closing_index == -1:
            raise Exception(f"Invalid markdown: missing closing delimiter {delimiter}")

        delimited_content = remaining_text[
            opening_index + len(delimiter) : closing_index
        ]
        parts.append(TextNode(delimited_content, text_type))

        remaining_text = remaining_text[closing_index + len(delimiter) :]

    if remaining_text:
        parts.append(TextNode(remaining_text, TextType.TEXT))

    return parts
