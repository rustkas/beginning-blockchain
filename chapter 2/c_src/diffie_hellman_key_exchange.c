#include <stdio.h>

// Function to return value of a ^ b mod P
long long int power(long long int a, long long int b, long long int P) {
    if (b == 1)
        return a;
    else
        return ((a % P) * (power(a, b - 1, P) % P)) % P;
}

// Main program for DH Key computation
int main() {
    long long int P, G, x, a, y, b, ka, kb;

    // Both the parties agree upon the public keys G and P
    P = 23; // A prime number P is taken
    printf("The value of P : %lld\n", P);

    G = 5; // A prime number G is taken
    printf("The value of G : %lld\n", G);

    // Alice chooses the private key a
    a = 6;
    printf("The private key a for Alice : %lld\n", a);

    // Bob chooses the private key b
    b = 3;
    printf("The private key b for Bob : %lld\n\n", b);

    // Alice and Bob generate their public keys
    y = power(G, a, P); // gets the generated key for Alice
    x = power(G, b, P); // gets the generated key for Bob

    // Generating the secret key after the exchange of keys
    ka = power(x, a, P); // Secret key for Alice
    kb = power(y, b, P); // Secret key for Bob

    printf("Secret key for Alice is : %lld\n", ka);
    printf("Secret key for Bob is : %lld\n", kb);

    return 0;
}
