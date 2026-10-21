#include <stdint.h>

// Fast inline rotations for uint64_t
static inline uint64_t rotl64(uint64_t x, uint8_t n) {
    return (x << n) | (x >> (64 - n));
}
static inline uint64_t rotr64(uint64_t x, uint8_t n) {
    return (x >> n) | (x << (64 - n));
}
static inline uint64_t round_func(uint64_t R, uint64_t K) {
    return (rotl64(R, 5) + K) ^ rotr64(R, 11);
}

void key_schedule(const uint8_t MK[16], uint64_t RK[12]) {
    uint64_t SA = 0, SB = 0;
    for(int i=7; i>=0; i--) SA = (SA << 8) | MK[i];
    for(int i=15; i>=8; i--) SB = (SB << 8) | MK[i];

    for (uint8_t i = 1; i <= 12; i++) {
        if (i & 1) {
            SA = rotl64(SA ^ SB, 13);
            RK[i-1] = SA ^ i;
        } else {
            SB = rotl64(SB ^ SA, 13);
            RK[i-1] = SB ^ (2 * i);
        }
    }
}

void encrypt_block(const uint8_t P[16], const uint64_t RK[12], uint8_t C[16]) {
    uint64_t L = 0, R = 0;
    for(int i=7; i>=0; i--) L = (L << 8) | P[i];
    for(int i=15; i>=8; i--) R = (R << 8) | P[i];

    for (uint8_t i = 0; i < 12; i++) {
        uint64_t Fi = round_func(R, RK[i]);
        uint64_t nL = R;
        uint64_t nR = L ^ Fi;
        L = nL; R = nR;
    }
    
    for(int i=0; i<8; i++) C[i] = (L >> (i*8)) & 0xFF;
    for(int i=0; i<8; i++) C[i+8] = (R >> (i*8)) & 0xFF;
}

void decrypt_block(const uint8_t C[16], const uint64_t RK[12], uint8_t P[16]) {
    uint64_t L = 0, R = 0;
    for(int i=7; i>=0; i--) L = (L << 8) | C[i];
    for(int i=15; i>=8; i--) R = (R << 8) | C[i];

    for (int8_t i = 11; i >= 0; i--) {
        uint64_t Fi = round_func(L, RK[i]); 
        uint64_t nL = R ^ Fi;
        uint64_t nR = L;
        L = nL; R = nR;
    }
    for(int i=0; i<8; i++) P[i] = (L >> (i*8)) & 0xFF;
    for(int i=0; i<8; i++) P[i+8] = (R >> (i*8)) & 0xFF;
}