# Lightweight Feistel Block Cipher (128-bit)

This repository contains the C implementation and Python analysis scripts for the 128-bit Lightweight Feistel Block Cipher proposed in the paper: 
*"A 128-bit Lightweight Feistel Block Cipher with Cross-Mixed Key Scheduling for Resource-Constrained IoT Devices"*

## Contents
- `cipher.c`: The C implementation of the cipher (Encryption and Decryption) optimized for ATmega328P.
- `differential_analysis.py`: The Python script used for the 1,000,000-trial empirical differential cryptanalysis.

## Test Vectors
- Plaintext: `0123456789ABCDEFEDCBA9876543210`
- Key: `00112233445566778899AABBCCDDEEFF`
- Ciphertext: `96246E32E0FA1EEA96AC9D21564EB838`
