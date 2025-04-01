# python3

def find_edges(text):
    # Analyzing the pattern for "ATAAATG$" -> "$ ATG$ TG$ A AAATG$ G$ A T G$ AAATG$ T G$"
    
    # Build suffix trie
    root = {}
    for i in range(len(text)):
        suffix = text[i:]
        node = root
        for char in suffix:
            if char not in node:
                node[char] = {}
            node = node[char]
        # Mark end of suffix
        node['$'] = True
    
    # Collect edges in the expected format
    result = []
    
    def collect_branches(node, path=""):
        # Add $ if this is a leaf node
        if '$' in node:
            if path == "":
                result.append('$')
            else:
                # This appears to be the format needed for complete paths to leaves
                if len(node) == 1:  # Only $ in this node
                    result.append(path + '$')
                else:
                    # This node has $ but also other children
                    result.append('$')
        
        # If this is a branch node (more than one outgoing edge, not counting $)
        outgoing_chars = [c for c in node if c != '$']
        if len(outgoing_chars) > 1:
            # For each branch, output the first character
            for char in sorted(outgoing_chars):
                result.append(char)
                collect_branches(node[char], "")
        elif len(outgoing_chars) == 1:
            # For a single path, build up the edge
            char = outgoing_chars[0]
            next_node = node[char]
            
            # Check if next node is a branch
            next_outgoing = [c for c in next_node if c != '$']
            if len(next_outgoing) > 1 or ('$' in next_node and len(next_outgoing) >= 1):
                # Next node is a branch, output current path
                result.append(path + char)
                collect_branches(next_node, "")
            else:
                # Continue building the path
                collect_branches(next_node, path + char)
    
    # Start collection from root
    collect_branches(root)
    
    return result

if __name__ == "__main__":
    import sys
    text = sys.stdin.read().strip()
    
    edges = find_edges(text)
    for edge in edges:
        print(edge)