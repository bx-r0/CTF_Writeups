# C4: leaky power
C4 is a very advanced AES based defensive system. You are able to monitor the power lines. Is that enough?

You're given three files:

   - powertraces.npy: Measurements (over time) of power consumption of a chip while performing AES encryption
   - plaintexts.npy: Corresponding plaintext inputs that were encrypted
   - instructions.jwe: File encrypted using the same key as plaintexts.npy.

note: The first two files are NumPy arrays.

note: there's a mistake in the way instructions.jwe was created (the algorithm is A128GCM, not A256GCM).

