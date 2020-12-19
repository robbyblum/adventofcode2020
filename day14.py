# day 14...stuff
import re


def main():
    with open("input/day14.txt") as f:
        raw = [line.strip() for line in f.readlines()]
    instructions = [re.split("\\[|\\] = | = ", line) for line in raw]

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
            bvalout = ''.join([d if mask[i] == "X"
                               else mask[i] for i, d in enumerate(bvalin)])
            # convert back to int and "write to memory"
            valout = int(bvalout, 2)
            memory[addr] = valout
    print("Part 1:", sum(memory.values()))

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
