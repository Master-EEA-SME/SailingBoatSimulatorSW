def hexDump(x):
    for i in range(len(x)):
        print("0x{0:08X}".format(i))
        for j in range(16):
            if i + j < len(x):
                print(" {0:02X}".format(x[i]))
            else:
                break
        print()
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min