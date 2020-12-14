# day 13: buses


def main():
    with open("input/day13.txt") as f:
        raw = f.readlines()
        t0 = int(raw[0])
        bus_list_raw = raw[1].split(",")
        bus_list = []
        for bus in bus_list_raw:
            if bus == 'x':
                continue
            else:
                bus_list.append(int(bus))
        print("bus list, condensed:", bus_list)

        wait_times = []
        for bus in bus_list:
            wait_times.append(bus - (t0 % bus))
        print("wait times:", wait_times)
        waitmin_i = wait_times.index(min(wait_times))
        minbus = bus_list[waitmin_i]
        minwait = wait_times[waitmin_i]
        print(f"Part 1: bus {minbus}, {minwait} minute wait: {minbus * minwait}")

        # part 2, a rather different problem...
        print("Part 2:")
        L = len(bus_list_raw)
        t_offsets = [i for i in range(L)]
        t_off_list = []
        for i, bus in enumerate(bus_list_raw):
            if bus == 'x':
                continue
            else:
                t_off_list.append(t_offsets[i])
        print(bus_list)
        print(t_off_list)
        # the answer is below 1909273434898297, which is the product of all the
        # bus numbers in question. So uh, that helps??? (does it really?)


if __name__ == '__main__':
    main()
