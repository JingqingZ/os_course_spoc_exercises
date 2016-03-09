# 2-level page index

data = dict()
pde_base = '11'


def loaddata(filename):
    global data
    data = dict()
    infile = open(filename)
    for line in infile:
        content = line.split(": ")
        page_index = content[0].split()
        data[page_index[1]] = content[1].split()
    infile.close()


def addr_split(addr):
    b = bin(int(addr, 16))[2:].zfill(15)
    return b[:5], b[5:10], b[-5:]


def p1_index(off):
    global data
    return data[pde_base][int(off, 2)]


def phy_index(pde, off):
    b = bin(int(pde, 16))[2:].zfill(8)
    if b[0] == '0':
        return -1
    else:
        h1 = str(hex(int(b[1:4], 2))[2:])
        h2 = str(hex(int(b[4:], 2))[2:])
        return data[h1 + h2][int(off, 2)]


def find_value(addr):
    p1, p2, o = addr_split(addr)
    pde = p1_index(p1)
    pte = phy_index(pde, p2)
    if pte == -1:
        return -1
    pad = phy_index(pte, o)
    if pad == -1:
        return -1
    return pad


def main():
    loaddata("./03-2-data.txt")
    print(find_value("03df"))
    print(find_value("69dc"))


if __name__ == "__main__":
    main()
