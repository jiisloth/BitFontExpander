import json
import argparse

X = 0
Y = 1

parser = argparse.ArgumentParser(description='Expand BitFonts from BitFontMaker.', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('expand', choices=["up", "down", "left", "right", "upleft", "upright", "downleft", "downright", "plus", "round", "widen", "stretch"], nargs="?",
                    help='Choose way you want to expand font:\n'
                         'directionals: up, down, left, right\n'
                         'diagonals: upleft, upright, downleft, downright\n'
                         'Specials:\n'
                         '| plus  | round | widen |stretch|\n'
                         '|   X   |  XXX  |       |   X   |\n'
                         '|  XOX  |  XOX  |  XOX  |   O   |\n'
                         '|   X   |  XXX  |       |   X   |')
parser.add_argument('-c', '--custom', metavar='X,Y', type=str, nargs='+',
                    help='Pass offsets as pairs X1,Y1 X2,Y2. X grows righ, Y grows down,')
parser.add_argument('--middle', choices=["hollow", "filled"],
                    help='hollow: Removes the original bitmap from the result\n'
                         'filled: Adds the original bitmap to the result\n')
parser.add_argument('-i', '--input',
                    help='path for input file.\nDefault: ask for input.')
parser.add_argument('-o', '--output',
                    help='path for output file.\nDefault: print output')

offsetstrings = {
    "up": [[0,-1]],
    "down": [[0,1]],
    "left": [[-1,0]],
    "right": [[1,0]],
    "upleft": [[-1,-1]],
    "upright": [[1,-1]],
    "downleft": [[-1,1]],
    "downright": [[1,1]],
    "plus": [[0,-1],[0,1],[-1,0],[1,0]],
    "round": [[0,-1],[0,1],[-1,0],[1,0],[-1,-1],[1,-1],[-1,1],[1,1]],
    "widen": [[-1,0],[1,0]],
    "stretch": [[0,-1],[0,1]]
}

def main():
    args = parser.parse_args()
    offsets = []
    if args.expand:
        offsets = offsetstrings[args.expand]
    if args.custom:
        for offset in args.custom:
            o = offset.split(",")
            if len(o) != 2:
                print("Error in custom offset arguments")
                return 0
            if o[0].isdigit() and o[1].isdigit():
                offsets.append([int(o[0]), int(o[1])])
            else:
                print("Error in custom offset arguments")
                return 0
    if len(offsets) == 0:
        print("No offset defined. Use -h to get help")
        return 0
    if args.input:
        txt = read_file(args.input)
    else:
        txt = input("Paste inputcode: ")
    data = json.loads(txt)
    for key in data.keys():
        if key.isdigit():
            data[key] = offsetchar(data[key], offsets, args.middle)

    if args.output:
        write_file(args.output, data)
    else:
        print(json.dumps(data))
    return 1


def offsetchar(char, offsets, middle):
    bitmap = []
    for row in char:
        binarystring = format(row, '016b')
        bitmap.append(binarystring)
    new = bitmap[:]
    for y in range(len(bitmap)):
        for x in range(len(bitmap[y])):
            for offset in offsets:
                if 0 <= y + offset[Y] < len(bitmap) and 0 <= x + offset[X] < len(bitmap[y]):
                    if bitmap[y][x] == "1":
                        new[y+offset[Y]] = new[y+offset[Y]][:x+offset[X]] + "1" + new[y+offset[Y]][x+offset[X] + 1:]
            if middle == "filled":
                if bitmap[y][x] == "1":
                    new[y] = new[y][:x] + "1" + new[y][x + 1:]
    if middle == "hollow":
        for y in range(len(bitmap)):
            for x in range(len(bitmap[y])):
                if bitmap[y][x] == "1":
                    new[y] = new[y][:x] + "0" + new[y][x + 1:]
    for y in range(len(new)):
        new[y] = int(new[y], 2)
    return new


def read_file(path):
    with open(path, "r") as f:
        txt = f.read()
    return txt


def write_file(path, data):
    with open(path, "w") as f:
        f.write(json.dumps(data))
    return


if __name__ == '__main__':
    main()
