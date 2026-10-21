import random
import time
from collections import Counter

MASK64 = 0xFFFFFFFFFFFFFFFF
TRIALS = 1_000_000

def rotl64(x, n):
    return ((x << n) | (x >> (64 - n))) & MASK64

def rotr64(x, n):
    return ((x >> n) | (x << (64 - n))) & MASK64

def F(R, K):
    return (((rotl64(R, 5) + K) & MASK64) ^ rotr64(R, 11)) & MASK64

def key_schedule(MK):
    SA = (MK >> 64) & MASK64
    SB = MK & MASK64
    RK = []
    for i in range(1, 13):
        if i % 2 == 1:
            SA = rotl64(SA ^ SB, 13)
            RK.append((SA ^ i) & MASK64)
        else:
            SB = rotl64(SB ^ SA, 13)
            RK.append((SB ^ (2 * i)) & MASK64)
    return RK

def encrypt(P, RK, rounds):
    L = (P >> 64) & MASK64
    R = P & MASK64
    for i in range(rounds):
        f_out = F(R, RK[i])
        L, R = R, (L ^ f_out) & MASK64
    return (L << 64) | R

print("Running Differential Analysis...")
input_diffs = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
rounds_to_test = [1, 2, 3, 4, 6, 8, 10, 12]

for r in rounds_to_test:
    max_prob = 0.0
    for diff in input_diffs:
        output_diffs = Counter()
        for _ in range(TRIALS // len(input_diffs)):
            P1 = random.getrandbits(128)
            MK = random.getrandbits(128)
            P2 = P1 ^ diff
            RK = key_schedule(MK)
            C1 = encrypt(P1, RK, r)
            C2 = encrypt(P2, RK, r)
            output_diffs[C1 ^ C2] += 1
        if output_diffs:
            most_common_diff, count = output_diffs.most_common(1)[0]
            prob = count / (TRIALS // len(input_diffs))
            if prob > max_prob:
                max_prob = prob
    print(f"Rounds: {r:2d} | Max Observed Probability: {max_prob:.2e}")