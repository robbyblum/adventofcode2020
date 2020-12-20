# day 14...stuff
import re


def addrmask(addr, mask):
    """Applies a bitmask to a memory address, for part 2 of the problem.
    If mask[i] == 0, the corresponding address bit is passed through it.
    Otherwise, address bit i is overwritten with 1 (if mask[i] == 1), or is
    allowed to float (if mask[i] == X). Returns the masked memory address,
    in pseudo-binary representation (i.e., 0/1/X like the mask input). Pass
    this to the next function to expand to a list of memory addresses."""
    baddr = f"{bin(addr)[2:]:>036}"
    baddrmask = "".join([d if mask[i] == "0" else mask[i]
                         for i, d in enumerate(baddr)])
    return baddrmask


def expand_addrmask(addrmask):
    """Expands a masked memory address to a list of all the applicable memory
    addresses it could refer to. That is, a string like "00X1010X" could stand
    for the binary numbers 00010100, 00010101, 00110100, or 00110101, which
    correspond to decimal values 20, 21, 52, or 53, respectively. So if you
    give this function the string "00X1010X", it will output the list
    [20, 21, 52, 53]. """
    out = [""]
    for d in addrmask:
        if d == "X":
            d = "01"
        # wow python list comprehensions are awesome. It took me a while to
        # futz my way to the correct syntax but this is really smooth
        out = [a + i for a in out for i in d]
    return out


def main():
    with open("input/day14.txt") as f:
        raw = [line.strip() for line in f.readlines()]
    instructions = [re.split("\\[|\\] = | = ", line) for line in raw]

    # PART 1
    # Make memory register a dict because it ensures uniqueness automatically.
    # This is kinda ugly conceptually, but who cares.
    memory = {}
    for step in instructions:
        if step[0] == 'mask':
            # change the mask string
            mask = step[1]
        else:
            addr = int(step[1])
            valin = int(step[2])
            # make 36-bit binary representation, w/o the "0b" prefix
            bvalin = f"{bin(valin)[2:]:>036}"
            # apply the mask
            bvalout = "".join([d if mask[i] == "X"
                               else mask[i] for i, d in enumerate(bvalin)])
            # convert back to int and "write to memory"
            valout = int(bvalout, 2)
            memory[addr] = valout
    print("Part 1:", sum(memory.values()))

    # PART 2
    # Now we have a memory address decoder instead of an input mask, or some-
    # thing like that. This needs functions, instead of just a loop in main().

    # # below is just me testing the addrmask function
    # mask = instructions[0][1]
    # addr = int(instructions[1][1])
    # # addr = 2**36 - 1
    # # addr = 0
    # val = int(instructions[1][2])
    # print(f"address: {bin(addr)[2:]:>036}")
    # print(f"mask:    {mask}")
    # print(f"result:  {addrmask(addr, mask)}")

    memory = {}
    for step in instructions:
        if step[0] == 'mask':
            # change the mask string
            mask = step[1]
        else:
            addr = int(step[1])
            val = int(step[2])
            # apply the mask to the address, in 2 steps
            baddrmask = addrmask(addr, mask)
            addrlist = [int(a, 2) for a in expand_addrmask(baddrmask)]
            for a in addrlist:
                memory[a] = val
    print("Part 2:", sum(memory.values()))

    # # below is just testing what my input is like. Memory addresses in the
    # # input are not unique!
    # memaddrs = []
    # for line in raw:
    #     if line[0:3] == "mem":
    #         memaddrs.append(int(re.split("\\[|\\] = ", line)[1]))
    # print(len(memaddrs))
    # print(len(set(memaddrs)))
    # for entr in set(memaddrs):
    #     print(entr, memaddrs.count(entr))


if __name__ == '__main__':
    main()
