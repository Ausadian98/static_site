from textnode import TextNode, TextType


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

    opening_index = text.find(delimiter)
    start_of_search = opening_index + len(delimiter)
    closing_index = text.find(delimiter, start_of_search)

    if closing_index == -1:
        raise Exception(f"Invalid markdown: missing closing delimiter {delimiter}")

    chunks = []

    if opening_index > 0:
        chunks.append(TextNode(text[:opening_index], TextType.TEXT))

    chunks.append(
        TextNode(text[opening_index + len(delimiter) : closing_index], text_type)
    )

    remaining_text = text[closing_index + len(delimiter) :]
    chunks.extend(process_delimiters(remaining_text, delimiter, text_type))

    return chunks
