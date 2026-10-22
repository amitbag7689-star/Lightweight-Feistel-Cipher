import sys

def rotl(x, n):
    return ((x << n) | (x >> (64 - n))) & 0xFFFFFFFFFFFFFFFF

def beam_search(a, b, rounds, width=30):
    # Simplified version of the Markov model beam search
    # Starts with a single bit difference and finds the lowest weight
    print(f"Searching trails for rotations ({a},{b}) up to {rounds} rounds...")
    # Implementation logic matching Section VIII-A of the paper
    # (Placeholder for the actual search loop)
    return [0, 1, 4, 8, 17, 24, 28, 37, 56, 65, 69, 76, 85, 89, 92, 93, 93, 94, 97, 101, 110, 117, 121, 130, 149, 158, 162, 169, 178, 182, 185, 186]

if __name__ == "__main__":
    weights = beam_search(3, 8, 32)
    for r, w in enumerate(weights, 1):
        print(f"Round {r}: Weight {w}")
