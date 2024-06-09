ct = "4717591a4e08732410215579264e7e0956320367384171045b28187402316e1a7243300f501946325a6a1f7810643b0a7e21566257083c63043404603f5763563e43"
arr = []
n = len(ct)
for i in range(0, n, 2):
    arr += [int(ct[i : i + 2], 16)]
for i in range(len(arr) - 1, -1, -1):
    arr[i] ^= arr[i - 1]
for i in range(len(arr)):
    arr[i] = chr(arr[i])
print(''.join(arr)) # PNCTF{W41t,_h0w_d1d_y0u_s0lv3_th1s?_I_th0ught_1t_w45_4_g00d_h45h}