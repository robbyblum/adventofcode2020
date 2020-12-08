# day 8
import pprint


def run_prog(inst):
    # is there a more elegant way than this? idk, maybe
    visited = [0] * len(inst)
    i = 0
    acc = 0
    try:
        while visited[i] == 0:
            visited[i] += 1
            cmd, num = inst[i].split()
            num = int(num)

            if cmd == 'acc':
                acc += num
                i += 1
            elif cmd == 'jmp':
                i += num
            elif cmd == 'nop':
                i += 1

        # if it looped, we should get here
        looped = True
        return acc, looped

    except Exception as e:
        # if it doesn't loop, we should hit an exception and end up here
        looped = False
        return acc, looped


def main():
    with open("input/day8.txt") as f:
        inst = [i.strip() for i in f.readlines()]

    # part 1
    acc, looped = run_prog(inst)
    print("Part 1:", acc)

    # part 2: I could use numpy, bc its indexing is nicer than plain lists, but
    # I'm trying to expand my range somewhat
    inst2 = inst.copy()
    for i, line in enumerate(inst):
        if line[0:3] == 'nop':
            inst2[i] = 'jmp' + line[3:]
            acc, looped = run_prog(inst2)
            if looped:
                # wrong line, reset it
                inst2[i] = line
            else:
                print(f"Part 2: found it! i = {i}, acc = {acc}")
                break
        elif line[0:3] == 'jmp':
            inst2[i] = 'nop' + line[3:]
            acc, looped = run_prog(inst2)
            if looped:
                # wrong line, reset it
                inst2[i] = line
            else:
                print(f"Part 2: found it! i = {i}, acc = {acc}")
                break


if __name__ == '__main__':
    main()
