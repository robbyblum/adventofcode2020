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
        print(bus_list)

        wait_times = []
        for bus in bus_list:
            wait_times.append(bus - (t0 % bus))
        print(wait_times)
        waitmin_i = wait_times.index(min(wait_times))
        print(f"Part 1: bus {bus_list[waitmin_i]}, {wait_times[waitmin_i]} minute wait: {bus_list[waitmin_i] * wait_times[waitmin_i]}")



if __name__ == '__main__':
    main()
