## paranoia

- The binary is seeded using srand(NULL), i.e. the current time

- Using the python `ctypes` library, sync with the time (and the seed) of the binary, allowing us to get the same outputs from `rand()`

- Connect with the remote server and use the output from `rand()` to decrypt the message