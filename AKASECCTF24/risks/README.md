## risks

- Binary using `riscv64` architecture

- The binary uses `getline` and stores the address of the buffer into `long buf`

- It then encrypts the contents of the buffer using addition and xor operations

- The buffer is treated as `long arr[4]`.

- Thereafter a check is done on each `long` in the buffer.

- Use z3 to apply the addition and xor operations and do the final check. 