from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []

    for old_node in old_nodes:
        # If not a text node, just add it as is
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue

        # Here's where we need to check for delimiters in text nodes
        text = old_node.text
        if delimiter not in text:
            # No delimiter found, add the node as is
            result.append(old_node)
            continue

        opening_index = text.find(delimiter)
        if opening_index == -1:
            result.append(old_node)
            continue

        start_of_search = opening_index + len(delimiter)
        closing_index = text.find(delimiter, start_of_search)

        if closing_index == -1:
            raise Exception(f"Invalid markdown: missing closing delimiter {delimiter}")

        result.extend(
            [
                TextNode(text[:opening_index], TextType.TEXT),
                TextNode(
                    text[opening_index + len(delimiter) : closing_index], text_type
                ),
                TextNode(text[closing_index + len(delimiter) :], TextType.TEXT),
            ]
        )
    return result
