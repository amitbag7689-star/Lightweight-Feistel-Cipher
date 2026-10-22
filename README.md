# A 128-bit ARX-Feistel Block Cipher (v2)

This repository contains the C implementation, Python analysis scripts, and benchmark harnesses for the 128-bit ARX-Feistel Block Cipher proposed in the paper: 
"A 128-bit ARX-Feistel Block Cipher for 8-bit Microcontrollers: Design Lessons, Differential Trail Analysis, and Measured AVR Performance"

## Contents
- `v2_cipher.c`: The plain C reference implementation of the v2 cipher (32 rounds) optimized for the ATmega328P.
- `v2.py`: Python reference implementation used for functional verification.
- `trail.py`: Python script for heuristic beam search of differential trails (Markov model).
- `sweep.py`: Python script for the all-pairs rotation-constant sweep.
- `sacbic.py`: Python script for SAC and BIC analysis.
- `gen.py`: Python script for generating CTR-mode sequences for NIST STS validation.

## Cipher Specifications (v2)
- Block Size: 128 bits
- Key Size: 128 bits
- Rounds: 32
- Structure: Balanced Feistel network
- Round Function: `F(R,K) = ((R ^ ROTL(R,3)) + K) ^ ROTL(R,8)`
- Key Schedule: Speck-style non-linear key schedule.

## Test Vectors
- Plaintext: `0123456789ABCDEFFEDCBA9876543210`
- Master Key: `00112233445566778899AABBCCDDEEFF`
- Expected Ciphertext: `1D900683674A2121E0B373406EC8D335`

(Note: The ATmega328P implementation, the Python reference, and the C host implementation all produce this expected ciphertext and correctly decrypt it back to the plaintext.)
