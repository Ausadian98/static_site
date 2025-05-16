def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_nodes = []
    expanded_nodes = old_nodes.expand()
    # not how  you use expand at all! not the purpose of expand.
    if expanded_nodes[text_type] != TextType.TEXT:
        # not how we go into the node apparently!
        new_nodes.append(expanded_nodes)
        # we don't want to use append here.
