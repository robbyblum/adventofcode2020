# day 8
import pprint


def main():
    with open("input/day8.txt") as f:
        inst = [i.strip() for i in f.readlines()]

    # is there a more elegant way than this? idk, maybe
    visited = [0] * len(inst)
    i = 0
    acc = 0
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

    print("Part 1:", acc)


if __name__ == '__main__':
    main()
