# page replacement policy
# working set replacement policy


def WorkingSetPolicy(addresses, window):
    inmemtable = dict()
    for i in range(0, len(addresses)):
        if addresses[i] in inmemtable:
            print(repr(addresses[i]) + ": HIT")
        else:
            print(repr(addresses[i]) + ": MISS")
        inmemtable[addresses[i]] = i
        deleteset = list()
        for ad in inmemtable.keys():
            if i - inmemtable[ad] >= 4:
                deleteset.append(ad)
        for ad in deleteset:
            del inmemtable[ad]


def main():
    policy = "working"
    addresses = [4, 3, 0, 2, 2, 3, 1, 2, 4, 2, 4, 0, 3]
    window = 4
    WorkingSetPolicy(addresses, window)


if __name__ == "__main__":
    main()
