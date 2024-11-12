import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        # Frequency of symbol
        self.freq = freq

        # Symbol name (character)
        self.symbol = symbol

        # Node left of current node
        self.left = left

        # Node right of current node
        self.right = right

        # Tree direction (0/1)
        self.huff = ''
        
    # Comparison function for priority queue
    def __lt__(self, nxt):
        return self.freq < nxt.freq

# Utility function to print Huffman codes for all symbols in the tree
def printNodes(node, val=''):
    # Huffman code for current node
    newVal = val + str(node.huff)

    # Traverse the tree
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)

    # If node is a leaf node, display its Huffman code
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

# Main function to create Huffman Tree and display codes
def createHuffmanTree(chars, freq):
    # List containing unused nodes
    nodes = []

    # Convert characters and frequencies into Huffman tree nodes
    for x in range(len(chars)):
        heapq.heappush(nodes, Node(freq[x], chars[x]))

    while len(nodes) > 1:
        # Get the two nodes with the smallest frequency
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # Assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # Combine the two nodes to create a new parent node
        newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, newNode)

    # Print Huffman codes for the symbols
    print("Huffman Codes for the characters are:")
    printNodes(nodes[0])

# Taking user input for characters and their frequencies
def main():
    chars = input("Enter characters (comma-separated): ").split(',')
    freq = list(map(int, input("Enter frequencies (comma-separated, in same order as characters): ").split(',')))

    if len(chars) != len(freq):
        print("Error: The number of characters and frequencies must match.")
        return

    createHuffmanTree(chars, freq)

# Run the main function
main()
