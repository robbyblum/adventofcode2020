# day 12: If logo the turtle commandeered a boat (thanks honu)
# -2d vector class, maybe? as an excuse to make a class?
# -unit vector for orientation, and vector for current position?
# -the 'pure translation, irrespective of heading' commands are just adding
# -simple vectors to your position, which is easy
# -the forward command requires knowing your heading, so unit vector heading
# means you just add `distance*u` where u is the unit vector
# -implement method to rotate the boat. i could go wild and use actual rotation
# matrices if i want, lol. It's all in 90 degree steps so how bad can it be,
# right?
import numpy as np


class boat2d:
    """docstring for boaty mcboatface."""

    def __init__(self, startpos=[0.0, 0.0], startdir=[1.0, 0.0],
                 startway=[10.0, 1.0]):
        """create ye boat"""
        # super(, self).__init__()  # leftover from template, meh
        # initial position, default the origin (0, 0)
        self.pos = np.array(startpos)
        # initial orientation, default east (+1, 0)
        self.dir = np.array(startdir)
        # initial waypoint location (for part 2), default [10, 1]
        self.way = np.array(startway)

    def rotate_arb(self, angle, degrees=True):
        """rotate ye boat...sadly for this problem I don't need to handle
        arbitrary angles so I'm not going to use this one. But I wanted to
        write it anyway, so I did."""
        if degrees:
            angle *= np.pi / 180
        rotmat = np.array([[np.cos(angle), -np.sin(angle)],
                          [np.sin(angle), np.cos(angle)]])
        self.dir = rotmat @ self.dir

    def rotate(self, angle):
        """rotate ye boat...but only by multiples of 90 degrees."""
        if angle % 90 != 0:
            raise ValueError("Hey! Don't do that! 90 degree increments only!")
        angle *= np.pi / 180
        # This is ridiculous, and it produces nonsense if you give it angles
        # that aren't in 90 degree increments. Hence the ValueError above.
        rotmat = np.array([[np.cos(angle).round(), -np.sin(angle).round()],
                          [np.sin(angle).round(), np.cos(angle).round()]])
        self.dir = rotmat @ self.dir

    def forward(self, distance):
        """move ye boat forward"""
        self.pos += distance * self.dir

    def slide(self, vector):
        """slide ye boat in an arbitrary direction, because this problem is
        ridiculous."""
        self.pos += vector

    def info(self):
        """print ye position and heading of ye boat"""
        if (self.dir == [1, 0]).all():
            head = "E"
        elif (self.dir == [0, 1]).all():
            head = "N"
        elif (self.dir == [-1, 0]).all():
            head = "W"
        elif (self.dir == [0, -1]).all():
            head = "S"
        else:
            head = "????"
        return f"position: {self.pos}    heading: {head} ({self.dir})"

    # down here we define weird waypoint-related methods for part 2 of the
    # problem. At least now we're not sliding the boat around...
    def way_slide(self, vector):
        """slide ye waypoint"""
        self.way += vector

    def way_rotate(self, angle):
        """rotate ye waypoint about ye boat, 90 degree increments only"""
        if angle % 90 != 0:
            raise ValueError("Hey! Don't do that! 90 degree increments only!")
        angle *= np.pi / 180
        # This is ridiculous, and it produces nonsense if you give it angles
        # that aren't in 90 degree increments. Hence the ValueError above.
        rotmat = np.array([[np.cos(angle).round(), -np.sin(angle).round()],
                          [np.sin(angle).round(), np.cos(angle).round()]])
        self.way = rotmat @ self.way

    def way_forward(self, N):
        """move ye boat forward to ye waypoint N times"""
        self.pos += N * self.way


def load_instructions(file):
    """loads instructions from file, stores in cryptic tuples"""
    raw = file.readlines()
    dirs = [(l[0], int(l[1:])) for l in raw]
    return dirs


def translate_instruction_part1(boat, instr):
    """translates an instruction out of a cryptic tuple and applies it to the
    boat object instance specified"""
    # just a big ol' switch structure
    if instr[0] == "F":
        # move forward
        boat.forward(instr[1])
    elif instr[0] == "N":
        # slide north
        boat.slide([0, instr[1]])
    elif instr[0] == "E":
        # slide east
        boat.slide([instr[1], 0])
    elif instr[0] == "S":
        # slide south
        boat.slide([0, -instr[1]])
    elif instr[0] == "W":
        # slide west
        boat.slide([-instr[1], 0])
    elif instr[0] == "R":
        # turn to starboard
        boat.rotate(-instr[1])
    elif instr[0] == "L":
        # turn to port
        boat.rotate(instr[1])


def translate_instruction_part2(boat, instr):
    """translates an instruction out of a cryptic tuple and applies it to the
    boat object instance specified"""
    # just a big ol' switch structure
    if instr[0] == "F":
        # move forward
        boat.way_forward(instr[1])
    elif instr[0] == "N":
        # slide north
        boat.way_slide([0, instr[1]])
    elif instr[0] == "E":
        # slide east
        boat.way_slide([instr[1], 0])
    elif instr[0] == "S":
        # slide south
        boat.way_slide([0, -instr[1]])
    elif instr[0] == "W":
        # slide west
        boat.way_slide([-instr[1], 0])
    elif instr[0] == "R":
        # turn to starboard
        boat.way_rotate(-instr[1])
    elif instr[0] == "L":
        # turn to port
        boat.way_rotate(instr[1])


def main():
    # x = boat2d()
    # print(x.info())
    # x.forward(2)
    # print(x.info())
    # x.rotate(90)
    # print(x.info())
    # x.forward(2)
    # print(x.info())
    # x.slide([69, 420])
    # print(x.info())
    # del x

    boaty = boat2d()

    with open("input/day12.txt") as f:
        directions = load_instructions(f)

    for instr in directions:
        translate_instruction_part1(boaty, instr)

    print(boaty.info())
    print("Part 1:", abs(boaty.pos).sum())

    # reset ye boaty
    del boaty
    boaty = boat2d()

    for instr in directions:
        translate_instruction_part2(boaty, instr)

    print(boaty.info())
    print("Part 2:", abs(boaty.pos).sum())


if __name__ == '__main__':
    main()
