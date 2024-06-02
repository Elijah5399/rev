# creds @HalfInchPunisher
import z3

flag = [z3.BitVec(f"b{i}", 8) for i in range(20)]
solver = z3.Solver()

# general key format
for f in flag:
    solver.add(
        z3.Or(
            z3.And(ord('0') <= f, f <= ord('9')),
            z3.And(ord('A') <= f, f <= ord('Z'))
        )
    )

# x86_64 part
nums = [0, 7, 0xE, 0x11]
uppers = [0x3D, 0x24, 0x2C, 0x32]

for i in range(4):
    n = z3.BitVecVal(0, 8)
    u = z3.BitVecVal(0, 8)
    for j in range(5):
        idx = i * 5 + j
        n += z3.If(z3.And(ord('0') <= flag[idx], flag[idx] <= ord('9')), flag[idx] - z3.BitVecVal(ord('0'), 8), 0)
        u += z3.If(z3.And(ord('A') <= flag[idx], flag[idx] <= ord('Z')), flag[idx] - z3.BitVecVal(ord('A'), 8), 0)

    solver.add(n == nums[i])
    solver.add(u == uppers[i])

# ppc64 part
for i in range(19):
    solver.add(z3.Implies(flag[i] == 65, z3.Or(*[flag[i+1] == x for x in [0x48, 0x4F, 0x57, 0x46, 0x4D, 0x32, 0x41, 0x31, 0x54, 0x45, 0x53, 0x58, 0x30, 0x4B, 0x43, 0x51, 0x35, 0x42, 0x59, 0x44, 0x4A, 0x37, 0x50, 0x38]])))
    solver.add(z3.Implies(flag[i] == 66, z3.Or(*[flag[i+1] == x for x in [0x33, 0x44, 0x5A, 0x4A, 0x48, 0x42, 0x32, 0x55, 0x4F, 0x53, 0x39, 0x4D, 0x54, 0x38, 0x4C, 0x4E, 0x57, 0x4B, 0x45, 0x46, 0x56, 0x36, 0x49, 0x37]])))
    solver.add(z3.Implies(flag[i] == 67, z3.Or(*[flag[i+1] == x for x in [0x4E, 0x41, 0x4B, 0x31, 0x4C, 0x51, 0x48, 0x58, 0x55, 0x4F, 0x57, 0x5A, 0x36, 0x45, 0x44, 0x39, 0x52, 0x53, 0x30, 0x42, 0x4A, 0x37, 0x54, 0x35]])))
    solver.add(z3.Implies(flag[i] == 68, z3.Or(*[flag[i+1] == x for x in [0x48, 0x39, 0x4F, 0x4A, 0x56, 0x36, 0x4D, 0x31, 0x53, 0x41, 0x50, 0x43, 0x35, 0x47, 0x57, 0x30, 0x55, 0x45, 0x38, 0x49, 0x5A, 0x59, 0x51, 0x4E]])))
    solver.add(z3.Implies(flag[i] == 69, z3.Or(*[flag[i+1] == x for x in [0x57, 0x39, 0x56, 0x55, 0x34, 0x36, 0x49, 0x46, 0x59, 0x50, 0x4E, 0x4A, 0x58, 0x4F, 0x32, 0x43, 0x41, 0x31, 0x37, 0x4B, 0x47, 0x30, 0x44, 0x4D]])))
    solver.add(z3.Implies(flag[i] == 70, z3.Or(*[flag[i+1] == x for x in [0x48, 0x39, 0x4D, 0x51, 0x46, 0x31, 0x57, 0x47, 0x56, 0x30, 0x43, 0x4E, 0x49, 0x38, 0x42, 0x41, 0x4C, 0x55, 0x58, 0x53, 0x44, 0x52, 0x5A, 0x33]])))
    solver.add(z3.Implies(flag[i] == 71, z3.Or(*[flag[i+1] == x for x in [0x37, 0x31, 0x33, 0x38, 0x55, 0x53, 0x35, 0x44, 0x4A, 0x4D, 0x4E, 0x4C, 0x58, 0x49, 0x47, 0x54, 0x59, 0x36, 0x30, 0x57, 0x5A, 0x50, 0x34, 0x39]])))
    solver.add(z3.Implies(flag[i] == 72, z3.Or(*[flag[i+1] == x for x in [0x31, 0x34, 0x33, 0x36, 0x38, 0x4D, 0x44, 0x56, 0x4A, 0x4E, 0x52, 0x49, 0x35, 0x4F, 0x32, 0x53, 0x4C, 0x48, 0x55, 0x58, 0x42, 0x5A, 0x30, 0x43]])))
    solver.add(z3.Implies(flag[i] == 73, z3.Or(*[flag[i+1] == x for x in [0x48, 0x31, 0x49, 0x34, 0x59, 0x4C, 0x5A, 0x41, 0x32, 0x55, 0x35, 0x44, 0x39, 0x43, 0x47, 0x37, 0x4A, 0x46, 0x4D, 0x58, 0x42, 0x51, 0x53, 0x30]])))
    solver.add(z3.Implies(flag[i] == 74, z3.Or(*[flag[i+1] == x for x in [0x39, 0x48, 0x47, 0x59, 0x4F, 0x36, 0x31, 0x37, 0x5A, 0x30, 0x46, 0x55, 0x4C, 0x56, 0x45, 0x50, 0x53, 0x4A, 0x41, 0x58, 0x52, 0x42, 0x57, 0x51]])))
    solver.add(z3.Implies(flag[i] == 75, z3.Or(*[flag[i+1] == x for x in [0x35, 0x54, 0x57, 0x31, 0x41, 0x50, 0x38, 0x4D, 0x46, 0x44, 0x36, 0x4F, 0x4B, 0x4A, 0x43, 0x30, 0x51, 0x42, 0x48, 0x49, 0x32, 0x45, 0x39, 0x34]])))
    solver.add(z3.Implies(flag[i] == 76, z3.Or(*[flag[i+1] == x for x in [0x4A, 0x44, 0x5A, 0x52, 0x36, 0x4F, 0x41, 0x57, 0x33, 0x31, 0x42, 0x39, 0x48, 0x47, 0x32, 0x37, 0x58, 0x59, 0x56, 0x4E, 0x45, 0x55, 0x38, 0x46]])))
    solver.add(z3.Implies(flag[i] == 77, z3.Or(*[flag[i+1] == x for x in [0x30, 0x45, 0x56, 0x39, 0x59, 0x44, 0x38, 0x51, 0x35, 0x50, 0x5A, 0x4E, 0x42, 0x47, 0x55, 0x31, 0x4D, 0x58, 0x54, 0x33, 0x49, 0x41, 0x43, 0x57]])))
    solver.add(z3.Implies(flag[i] == 78, z3.Or(*[flag[i+1] == x for x in [0x47, 0x48, 0x56, 0x38, 0x54, 0x59, 0x35, 0x49, 0x41, 0x4A, 0x43, 0x58, 0x4E, 0x55, 0x4F, 0x33, 0x34, 0x31, 0x52, 0x50, 0x4B, 0x32, 0x4C, 0x4D]])))
    solver.add(z3.Implies(flag[i] == 79, z3.Or(*[flag[i+1] == x for x in [0x42, 0x4F, 0x57, 0x4D, 0x37, 0x38, 0x34, 0x4B, 0x30, 0x55, 0x52, 0x32, 0x4C, 0x4A, 0x31, 0x59, 0x50, 0x45, 0x49, 0x56, 0x41, 0x53, 0x36, 0x39]])))
    solver.add(z3.Implies(flag[i] == 80, z3.Or(*[flag[i+1] == x for x in [0x46, 0x34, 0x30, 0x37, 0x38, 0x47, 0x4E, 0x42, 0x5A, 0x45, 0x4D, 0x35, 0x43, 0x39, 0x44, 0x48, 0x31, 0x50, 0x55, 0x4C, 0x49, 0x54, 0x41, 0x56]])))
    solver.add(z3.Implies(flag[i] == 81, z3.Or(*[flag[i+1] == x for x in [0x54, 0x49, 0x58, 0x50, 0x56, 0x38, 0x52, 0x31, 0x35, 0x37, 0x4E, 0x4A, 0x4C, 0x36, 0x45, 0x59, 0x42, 0x44, 0x55, 0x46, 0x4F, 0x57, 0x4D, 0x47]])))
    solver.add(z3.Implies(flag[i] == 82, z3.Or(*[flag[i+1] == x for x in [0x42, 0x48, 0x53, 0x4F, 0x30, 0x46, 0x56, 0x5A, 0x45, 0x35, 0x34, 0x59, 0x36, 0x39, 0x51, 0x52, 0x31, 0x44, 0x49, 0x33, 0x4D, 0x50, 0x47, 0x55]])))
    solver.add(z3.Implies(flag[i] == 83, z3.Or(*[flag[i+1] == x for x in [0x51, 0x38, 0x32, 0x4A, 0x58, 0x54, 0x56, 0x30, 0x57, 0x37, 0x34, 0x41, 0x53, 0x59, 0x33, 0x55, 0x52, 0x4F, 0x47, 0x5A, 0x46, 0x42, 0x35, 0x45]])))
    solver.add(z3.Implies(flag[i] == 84, z3.Or(*[flag[i+1] == x for x in [0x4F, 0x45, 0x37, 0x5A, 0x4B, 0x33, 0x47, 0x55, 0x50, 0x59, 0x54, 0x57, 0x41, 0x46, 0x4A, 0x58, 0x34, 0x49, 0x32, 0x52, 0x51, 0x4C, 0x4E, 0x39]])))
    solver.add(z3.Implies(flag[i] == 85, z3.Or(*[flag[i+1] == x for x in [0x4E, 0x45, 0x4A, 0x48, 0x43, 0x31, 0x4F, 0x46, 0x53, 0x42, 0x4D, 0x49, 0x44, 0x55, 0x33, 0x50, 0x56, 0x32, 0x37, 0x51, 0x39, 0x36, 0x59, 0x57]])))
    solver.add(z3.Implies(flag[i] == 86, z3.Or(*[flag[i+1] == x for x in [0x54, 0x4D, 0x42, 0x4A, 0x39, 0x35, 0x5A, 0x49, 0x53, 0x51, 0x30, 0x4C, 0x34, 0x59, 0x57, 0x4B, 0x56, 0x4E, 0x37, 0x55, 0x43, 0x32, 0x46, 0x36]])))
    solver.add(z3.Implies(flag[i] == 87, z3.Or(*[flag[i+1] == x for x in [0x53, 0x36, 0x5A, 0x48, 0x51, 0x34, 0x43, 0x59, 0x4D, 0x44, 0x33, 0x39, 0x30, 0x45, 0x38, 0x42, 0x41, 0x4F, 0x4B, 0x4E, 0x56, 0x46, 0x37, 0x4A]])))
    solver.add(z3.Implies(flag[i] == 88, z3.Or(*[flag[i+1] == x for x in [0x58, 0x36, 0x35, 0x39, 0x5A, 0x37, 0x33, 0x4D, 0x43, 0x44, 0x49, 0x4E, 0x4F, 0x4B, 0x34, 0x54, 0x4A, 0x46, 0x31, 0x47, 0x53, 0x57, 0x48, 0x45]])))
    solver.add(z3.Implies(flag[i] == 89, z3.Or(*[flag[i+1] == x for x in [0x4C, 0x47, 0x34, 0x45, 0x32, 0x36, 0x35, 0x46, 0x58, 0x38, 0x4E, 0x56, 0x5A, 0x49, 0x39, 0x54, 0x53, 0x43, 0x33, 0x4B, 0x50, 0x37, 0x48, 0x44]])))
    solver.add(z3.Implies(flag[i] == 90, z3.Or(*[flag[i+1] == x for x in [0x34, 0x52, 0x44, 0x32, 0x53, 0x4E, 0x4A, 0x41, 0x38, 0x35, 0x4F, 0x49, 0x36, 0x39, 0x4C, 0x58, 0x43, 0x54, 0x45, 0x50, 0x37, 0x57, 0x4D, 0x31]])))
    solver.add(z3.Implies(flag[i] == 48, z3.Or(*[flag[i+1] == x for x in [0x4D, 0x54, 0x47, 0x4B, 0x30, 0x51, 0x33, 0x35, 0x5A, 0x57, 0x52, 0x41, 0x45, 0x50, 0x56, 0x46, 0x4A, 0x48, 0x59, 0x32, 0x53, 0x58, 0x4C, 0x44]])))
    solver.add(z3.Implies(flag[i] == 49, z3.Or(*[flag[i+1] == x for x in [0x44, 0x5A, 0x43, 0x49, 0x54, 0x37, 0x57, 0x4D, 0x4B, 0x4E, 0x32, 0x46, 0x30, 0x52, 0x33, 0x50, 0x59, 0x51, 0x4F, 0x53, 0x45, 0x31, 0x36, 0x39]])))
    solver.add(z3.Implies(flag[i] == 50, z3.Or(*[flag[i+1] == x for x in [0x55, 0x54, 0x43, 0x4F, 0x36, 0x56, 0x57, 0x58, 0x47, 0x59, 0x30, 0x38, 0x32, 0x4A, 0x41, 0x4D, 0x5A, 0x4B, 0x35, 0x31, 0x33, 0x46, 0x42, 0x45]])))
    solver.add(z3.Implies(flag[i] == 51, z3.Or(*[flag[i+1] == x for x in [0x30, 0x41, 0x47, 0x45, 0x44, 0x36, 0x49, 0x52, 0x5A, 0x48, 0x4F, 0x56, 0x54, 0x57, 0x31, 0x4E, 0x51, 0x4A, 0x53, 0x4D, 0x50, 0x58, 0x32, 0x46]])))
    solver.add(z3.Implies(flag[i] == 52, z3.Or(*[flag[i+1] == x for x in [0x4E, 0x48, 0x4A, 0x39, 0x47, 0x32, 0x56, 0x37, 0x4C, 0x4B, 0x59, 0x49, 0x33, 0x44, 0x4D, 0x52, 0x50, 0x43, 0x54, 0x34, 0x58, 0x38, 0x41, 0x35]])))
    solver.add(z3.Implies(flag[i] == 53, z3.Or(*[flag[i+1] == x for x in [0x35, 0x32, 0x51, 0x33, 0x59, 0x37, 0x4A, 0x5A, 0x50, 0x58, 0x44, 0x4C, 0x46, 0x42, 0x38, 0x39, 0x55, 0x4B, 0x47, 0x45, 0x4F, 0x56, 0x48, 0x30]])))
    solver.add(z3.Implies(flag[i] == 54, z3.Or(*[flag[i+1] == x for x in [0x37, 0x53, 0x30, 0x42, 0x41, 0x44, 0x50, 0x4A, 0x33, 0x55, 0x46, 0x49, 0x58, 0x34, 0x48, 0x39, 0x54, 0x35, 0x4F, 0x59, 0x45, 0x47, 0x4B, 0x52]])))
    solver.add(z3.Implies(flag[i] == 55, z3.Or(*[flag[i+1] == x for x in [0x56, 0x52, 0x4C, 0x46, 0x55, 0x48, 0x35, 0x4A, 0x4B, 0x53, 0x4E, 0x42, 0x45, 0x57, 0x36, 0x49, 0x58, 0x43, 0x41, 0x37, 0x54, 0x34, 0x5A, 0x50]])))
    solver.add(z3.Implies(flag[i] == 56, z3.Or(*[flag[i+1] == x for x in [0x59, 0x5A, 0x53, 0x34, 0x36, 0x57, 0x4B, 0x56, 0x33, 0x4F, 0x55, 0x35, 0x52, 0x38, 0x54, 0x49, 0x48, 0x43, 0x31, 0x44, 0x41, 0x32, 0x4C, 0x30]])))
    solver.add(z3.Implies(flag[i] == 57, z3.Or(*[flag[i+1] == x for x in [0x47, 0x39, 0x58, 0x5A, 0x49, 0x35, 0x54, 0x45, 0x44, 0x33, 0x4A, 0x43, 0x55, 0x53, 0x31, 0x46, 0x41, 0x4D, 0x37, 0x52, 0x56, 0x42, 0x36, 0x50]])))

# aarch64 part
solver.add(flag[15] == 89)
solver.add(flag[17] == 77)
solver.add(flag[18] == 56)

solver.add(z3.Implies(flag[0] == 73, flag[18] == 53))
solver.add(z3.Implies(flag[0] == 89, flag[11] == 79))
solver.add(z3.Implies(flag[0] == 86, flag[14] == 85))
solver.add(z3.Implies(flag[0] == 76, flag[6] == 73))
solver.add(z3.Implies(flag[0] == 54, flag[4] == 90))
solver.add(z3.Implies(flag[0] == 55, flag[3] == 87))
solver.add(z3.Implies(flag[0] == 49, flag[17] == 73))
solver.add(z3.Implies(flag[0] == 88, flag[8] == 51))
solver.add(z3.Implies(flag[0] == 55, flag[12] == 77))
solver.add(z3.Implies(flag[0] == 67, flag[13] == 67))
solver.add(z3.Implies(flag[1] == 74, flag[3] == 84))
solver.add(z3.Implies(flag[1] == 85, flag[0] == 52))
solver.add(z3.Implies(flag[1] == 80, flag[11] == 66))
solver.add(z3.Implies(flag[1] == 76, flag[2] == 71))
solver.add(z3.Implies(flag[1] == 86, flag[18] == 54))
solver.add(z3.Implies(flag[1] == 68, flag[15] == 53))
solver.add(z3.Implies(flag[1] == 77, flag[5] == 79))
solver.add(z3.Implies(flag[1] == 77, flag[13] == 84))
solver.add(z3.Implies(flag[1] == 56, flag[7] == 85))
solver.add(z3.Implies(flag[1] == 88, flag[17] == 80))
solver.add(z3.Implies(flag[2] == 88, flag[5] == 68))
solver.add(z3.Implies(flag[2] == 89, flag[0] == 75))
solver.add(z3.Implies(flag[2] == 77, flag[3] == 86))
solver.add(z3.Implies(flag[2] == 89, flag[13] == 90))
solver.add(z3.Implies(flag[2] == 71, flag[12] == 79))
solver.add(z3.Implies(flag[2] == 69, flag[19] == 87))
solver.add(z3.Implies(flag[2] == 49, flag[7] == 88))
solver.add(z3.Implies(flag[2] == 70, flag[8] == 70))
solver.add(z3.Implies(flag[2] == 69, flag[1] == 85))
solver.add(z3.Implies(flag[2] == 82, flag[11] == 81))
solver.add(z3.Implies(flag[3] == 68, flag[19] == 80))
solver.add(z3.Implies(flag[3] == 57, flag[1] == 88))
solver.add(z3.Implies(flag[3] == 78, flag[11] == 81))
solver.add(z3.Implies(flag[3] == 76, flag[9] == 82))
solver.add(z3.Implies(flag[3] == 69, flag[12] == 72))
solver.add(z3.Implies(flag[3] == 89, flag[14] == 48))
solver.add(z3.Implies(flag[3] == 74, flag[6] == 65))
solver.add(z3.Implies(flag[3] == 71, flag[0] == 48))
solver.add(z3.Implies(flag[3] == 82, flag[8] == 56))
solver.add(z3.Implies(flag[3] == 86, flag[7] == 54))
solver.add(z3.Implies(flag[4] == 57, flag[0] == 66))
solver.add(z3.Implies(flag[4] == 74, flag[16] == 69))
solver.add(z3.Implies(flag[4] == 55, flag[6] == 50))
solver.add(z3.Implies(flag[4] == 75, flag[17] == 77))
solver.add(z3.Implies(flag[4] == 74, flag[15] == 89))
solver.add(z3.Implies(flag[4] == 51, flag[8] == 84))
solver.add(z3.Implies(flag[4] == 51, flag[1] == 84))
solver.add(z3.Implies(flag[4] == 76, flag[3] == 66))
solver.add(z3.Implies(flag[4] == 82, flag[13] == 72))
solver.add(z3.Implies(flag[4] == 50, flag[11] == 87))
solver.add(z3.Implies(flag[5] == 66, flag[11] == 86))
solver.add(z3.Implies(flag[5] == 74, flag[19] == 48))
solver.add(z3.Implies(flag[5] == 49, flag[18] == 82))
solver.add(z3.Implies(flag[5] == 54, flag[6] == 77))
solver.add(z3.Implies(flag[5] == 84, flag[0] == 68))
solver.add(z3.Implies(flag[5] == 75, flag[14] == 87))
solver.add(z3.Implies(flag[5] == 66, flag[15] == 74))
solver.add(z3.Implies(flag[5] == 69, flag[16] == 68))
solver.add(z3.Implies(flag[5] == 85, flag[17] == 76))
solver.add(z3.Implies(flag[5] == 75, flag[4] == 75))
solver.add(z3.Implies(flag[6] == 82, flag[5] == 50))
solver.add(z3.Implies(flag[6] == 70, flag[19] == 66))
solver.add(z3.Implies(flag[6] == 79, flag[13] == 77))
solver.add(z3.Implies(flag[6] == 83, flag[11] == 86))
solver.add(z3.Implies(flag[6] == 48, flag[15] == 89))
solver.add(z3.Implies(flag[6] == 50, flag[9] == 77))
solver.add(z3.Implies(flag[6] == 51, flag[10] == 54))
solver.add(z3.Implies(flag[6] == 86, flag[0] == 66))
solver.add(z3.Implies(flag[6] == 90, flag[14] == 48))
solver.add(z3.Implies(flag[6] == 66, flag[1] == 68))
solver.add(z3.Implies(flag[7] == 88, flag[18] == 56))
solver.add(z3.Implies(flag[7] == 49, flag[15] == 87))
solver.add(z3.Implies(flag[7] == 51, flag[2] == 80))
solver.add(z3.Implies(flag[7] == 79, flag[10] == 65))
solver.add(z3.Implies(flag[7] == 52, flag[8] == 74))
solver.add(z3.Implies(flag[7] == 70, flag[17] == 85))
solver.add(z3.Implies(flag[7] == 57, flag[5] == 52))
solver.add(z3.Implies(flag[7] == 82, flag[6] == 81))
solver.add(z3.Implies(flag[7] == 85, flag[14] == 78))
solver.add(z3.Implies(flag[7] == 79, flag[16] == 72))
solver.add(z3.Implies(flag[8] == 78, flag[15] == 75))
solver.add(z3.Implies(flag[8] == 51, flag[18] == 84))
solver.add(z3.Implies(flag[8] == 52, flag[10] == 79))
solver.add(z3.Implies(flag[8] == 56, flag[17] == 57))
solver.add(z3.Implies(flag[8] == 86, flag[11] == 84))
solver.add(z3.Implies(flag[8] == 77, flag[19] == 71))
solver.add(z3.Implies(flag[8] == 67, flag[16] == 88))
solver.add(z3.Implies(flag[8] == 52, flag[12] == 55))
solver.add(z3.Implies(flag[8] == 82, flag[6] == 70))
solver.add(z3.Implies(flag[8] == 78, flag[13] == 80))
solver.add(z3.Implies(flag[9] == 82, flag[5] == 82))
solver.add(z3.Implies(flag[9] == 51, flag[7] == 65))
solver.add(z3.Implies(flag[9] == 73, flag[3] == 71))
solver.add(z3.Implies(flag[9] == 89, flag[17] == 88))
solver.add(z3.Implies(flag[9] == 84, flag[11] == 65))
solver.add(z3.Implies(flag[9] == 50, flag[16] == 51))
solver.add(z3.Implies(flag[9] == 71, flag[0] == 82))
solver.add(z3.Implies(flag[9] == 66, flag[6] == 51))
solver.add(z3.Implies(flag[9] == 81, flag[15] == 76))
solver.add(z3.Implies(flag[9] == 52, flag[13] == 86))
solver.add(z3.Implies(flag[10] == 87, flag[2] == 81))
solver.add(z3.Implies(flag[10] == 48, flag[9] == 78))
solver.add(z3.Implies(flag[10] == 77, flag[6] == 54))
solver.add(z3.Implies(flag[10] == 51, flag[11] == 88))
solver.add(z3.Implies(flag[10] == 73, flag[12] == 56))
solver.add(z3.Implies(flag[10] == 82, flag[15] == 70))
solver.add(z3.Implies(flag[10] == 87, flag[14] == 65))
solver.add(z3.Implies(flag[10] == 69, flag[5] == 52))
solver.add(z3.Implies(flag[10] == 85, flag[17] == 75))
solver.add(z3.Implies(flag[10] == 51, flag[3] == 65))
solver.add(z3.Implies(flag[11] == 79, flag[0] == 52))
solver.add(z3.Implies(flag[11] == 77, flag[8] == 83))
solver.add(z3.Implies(flag[11] == 74, flag[17] == 82))
solver.add(z3.Implies(flag[11] == 90, flag[5] == 71))
solver.add(z3.Implies(flag[11] == 82, flag[12] == 65))
solver.add(z3.Implies(flag[11] == 57, flag[13] == 49))
solver.add(z3.Implies(flag[11] == 50, flag[2] == 80))
solver.add(z3.Implies(flag[11] == 50, flag[14] == 72))
solver.add(z3.Implies(flag[11] == 52, flag[16] == 84))
solver.add(z3.Implies(flag[11] == 66, flag[1] == 80))
solver.add(z3.Implies(flag[12] == 56, flag[1] == 80))
solver.add(z3.Implies(flag[12] == 79, flag[1] == 67))
solver.add(z3.Implies(flag[12] == 84, flag[11] == 49))
solver.add(z3.Implies(flag[12] == 52, flag[13] == 54))
solver.add(z3.Implies(flag[12] == 55, flag[6] == 84))
solver.add(z3.Implies(flag[12] == 53, flag[7] == 69))
solver.add(z3.Implies(flag[12] == 80, flag[19] == 83))
solver.add(z3.Implies(flag[12] == 77, flag[14] == 74))
solver.add(z3.Implies(flag[12] == 80, flag[9] == 73))
solver.add(z3.Implies(flag[12] == 87, flag[16] == 65))
solver.add(z3.Implies(flag[13] == 90, flag[2] == 55))
solver.add(z3.Implies(flag[13] == 78, flag[0] == 56))
solver.add(z3.Implies(flag[13] == 86, flag[8] == 55))
solver.add(z3.Implies(flag[13] == 69, flag[7] == 54))
solver.add(z3.Implies(flag[13] == 85, flag[18] == 67))
solver.add(z3.Implies(flag[13] == 86, flag[16] == 57))
solver.add(z3.Implies(flag[13] == 87, flag[5] == 68))
solver.add(z3.Implies(flag[13] == 86, flag[1] == 80))
solver.add(z3.Implies(flag[13] == 55, flag[15] == 54))
solver.add(z3.Implies(flag[13] == 50, flag[10] == 81))
solver.add(z3.Implies(flag[14] == 52, flag[13] == 78))
solver.add(z3.Implies(flag[14] == 70, flag[9] == 54))
solver.add(z3.Implies(flag[14] == 55, flag[18] == 50))
solver.add(z3.Implies(flag[14] == 75, flag[11] == 72))
solver.add(z3.Implies(flag[14] == 70, flag[1] == 54))
solver.add(z3.Implies(flag[14] == 87, flag[4] == 75))
solver.add(z3.Implies(flag[14] == 65, flag[2] == 70))
solver.add(z3.Implies(flag[14] == 48, flag[6] == 89))
solver.add(z3.Implies(flag[14] == 72, flag[16] == 66))
solver.add(z3.Implies(flag[14] == 78, flag[15] == 84))
solver.add(z3.Implies(flag[15] == 66, flag[9] == 53))
solver.add(z3.Implies(flag[15] == 89, flag[10] == 54))
solver.add(z3.Implies(flag[15] == 72, flag[13] == 48))
solver.add(z3.Implies(flag[15] == 66, flag[11] == 83))
solver.add(z3.Implies(flag[15] == 76, flag[17] == 84))
solver.add(z3.Implies(flag[15] == 80, flag[3] == 87))
solver.add(z3.Implies(flag[15] == 76, flag[1] == 50))
solver.add(z3.Implies(flag[15] == 72, flag[8] == 79))
solver.add(z3.Implies(flag[15] == 81, flag[2] == 67))
solver.add(z3.Implies(flag[15] == 78, flag[16] == 52))
solver.add(z3.Implies(flag[16] == 57, flag[10] == 54))
solver.add(z3.Implies(flag[16] == 79, flag[11] == 81))
solver.add(z3.Implies(flag[16] == 66, flag[6] == 75))
solver.add(z3.Implies(flag[16] == 50, flag[5] == 56))
solver.add(z3.Implies(flag[16] == 73, flag[19] == 73))
solver.add(z3.Implies(flag[16] == 57, flag[17] == 77))
solver.add(z3.Implies(flag[16] == 72, flag[0] == 84))
solver.add(z3.Implies(flag[16] == 74, flag[1] == 50))
solver.add(z3.Implies(flag[16] == 87, flag[15] == 67))
solver.add(z3.Implies(flag[16] == 81, flag[4] == 69))
solver.add(z3.Implies(flag[17] == 76, flag[15] == 68))
solver.add(z3.Implies(flag[17] == 82, flag[4] == 79))
solver.add(z3.Implies(flag[17] == 72, flag[6] == 67))
solver.add(z3.Implies(flag[17] == 56, flag[8] == 50))
solver.add(z3.Implies(flag[17] == 77, flag[2] == 80))
solver.add(z3.Implies(flag[17] == 56, flag[0] == 49))
solver.add(z3.Implies(flag[17] == 90, flag[10] == 90))
solver.add(z3.Implies(flag[17] == 67, flag[13] == 49))
solver.add(z3.Implies(flag[17] == 51, flag[18] == 51))
solver.add(z3.Implies(flag[17] == 75, flag[5] == 57))
solver.add(z3.Implies(flag[18] == 56, flag[5] == 75))
solver.add(z3.Implies(flag[18] == 70, flag[11] == 79))
solver.add(z3.Implies(flag[18] == 77, flag[17] == 85))
solver.add(z3.Implies(flag[18] == 83, flag[0] == 75))
solver.add(z3.Implies(flag[18] == 70, flag[3] == 49))
solver.add(z3.Implies(flag[18] == 49, flag[13] == 71))
solver.add(z3.Implies(flag[18] == 54, flag[4] == 54))
solver.add(z3.Implies(flag[18] == 49, flag[6] == 84))
solver.add(z3.Implies(flag[18] == 69, flag[19] == 55))
solver.add(z3.Implies(flag[18] == 66, flag[8] == 82))
solver.add(z3.Implies(flag[19] == 50, flag[8] == 86))
solver.add(z3.Implies(flag[19] == 71, flag[14] == 70))
solver.add(z3.Implies(flag[19] == 87, flag[9] == 77))
solver.add(z3.Implies(flag[19] == 67, flag[13] == 87))
solver.add(z3.Implies(flag[19] == 86, flag[4] == 71))
solver.add(z3.Implies(flag[19] == 66, flag[2] == 55))
solver.add(z3.Implies(flag[19] == 73, flag[1] == 56))
solver.add(z3.Implies(flag[19] == 71, flag[5] == 50))
solver.add(z3.Implies(flag[19] == 84, flag[12] == 68))
solver.add(z3.Implies(flag[19] == 69, flag[11] == 66))

# riscv part
cnt = [z3.IntVal(0) for _ in range(36)]
for f in flag:
    cnt[0] += z3.If(f == 65, z3.IntVal(1), z3.IntVal(0))
    cnt[1] += z3.If(f == 66, z3.IntVal(1), z3.IntVal(0))
    cnt[2] += z3.If(f == 67, z3.IntVal(1), z3.IntVal(0))
    cnt[3] += z3.If(f == 68, z3.IntVal(1), z3.IntVal(0))
    cnt[4] += z3.If(f == 69, z3.IntVal(1), z3.IntVal(0))
    cnt[5] += z3.If(f == 70, z3.IntVal(1), z3.IntVal(0))
    cnt[6] += z3.If(f == 71, z3.IntVal(1), z3.IntVal(0))
    cnt[7] += z3.If(f == 72, z3.IntVal(1), z3.IntVal(0))
    cnt[8] += z3.If(f == 73, z3.IntVal(1), z3.IntVal(0))
    cnt[9] += z3.If(f == 74, z3.IntVal(1), z3.IntVal(0))
    cnt[10] += z3.If(f == 75, z3.IntVal(1), z3.IntVal(0))
    cnt[11] += z3.If(f == 76, z3.IntVal(1), z3.IntVal(0))
    cnt[12] += z3.If(f == 77, z3.IntVal(1), z3.IntVal(0))
    cnt[13] += z3.If(f == 78, z3.IntVal(1), z3.IntVal(0))
    cnt[14] += z3.If(f == 79, z3.IntVal(1), z3.IntVal(0))
    cnt[15] += z3.If(f == 80, z3.IntVal(1), z3.IntVal(0))
    cnt[16] += z3.If(f == 81, z3.IntVal(1), z3.IntVal(0))
    cnt[17] += z3.If(f == 82, z3.IntVal(1), z3.IntVal(0))
    cnt[18] += z3.If(f == 83, z3.IntVal(1), z3.IntVal(0))
    cnt[19] += z3.If(f == 84, z3.IntVal(1), z3.IntVal(0))
    cnt[20] += z3.If(f == 85, z3.IntVal(1), z3.IntVal(0))
    cnt[21] += z3.If(f == 86, z3.IntVal(1), z3.IntVal(0))
    cnt[22] += z3.If(f == 87, z3.IntVal(1), z3.IntVal(0))
    cnt[23] += z3.If(f == 88, z3.IntVal(1), z3.IntVal(0))
    cnt[24] += z3.If(f == 89, z3.IntVal(1), z3.IntVal(0))
    cnt[25] += z3.If(f == 90, z3.IntVal(1), z3.IntVal(0))
    cnt[26] += z3.If(f == 48, z3.IntVal(1), z3.IntVal(0))
    cnt[27] += z3.If(f == 49, z3.IntVal(1), z3.IntVal(0))
    cnt[28] += z3.If(f == 50, z3.IntVal(1), z3.IntVal(0))
    cnt[29] += z3.If(f == 51, z3.IntVal(1), z3.IntVal(0))
    cnt[30] += z3.If(f == 52, z3.IntVal(1), z3.IntVal(0))
    cnt[31] += z3.If(f == 53, z3.IntVal(1), z3.IntVal(0))
    cnt[32] += z3.If(f == 54, z3.IntVal(1), z3.IntVal(0))
    cnt[33] += z3.If(f == 55, z3.IntVal(1), z3.IntVal(0))
    cnt[34] += z3.If(f == 56, z3.IntVal(1), z3.IntVal(0))
    cnt[35] += z3.If(f == 57, z3.IntVal(1), z3.IntVal(0))

expected = [0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 1, 2, 1]
for i, exp in enumerate(expected):
    solver.add(cnt[i] == exp)

status = solver.check()
if status != z3.sat:
    exit(str(status))

m = solver.model()

key = [chr(m[f].as_long()) for f in flag]
new_key = []
for i in range(0, len(key), 5):
    new_key.extend([*key[i:i+5], '-'])
print("".join(new_key[:-1]))
