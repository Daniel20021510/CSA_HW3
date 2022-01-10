HELP_MESSAGE =   "CSA Homework 3. Plants with Straight Insertion.\n"                             \
"Task: 13, Function: 10\n\n" \
"Program options:\n\n" \
"\t-i - Set input file\n" \
"\t-o - Set output file\n" \
"\t-r - Generate random input\n\n" \
"Examples: " \
"\t-i input.txt -o output.txt\n" \
"\t-r 20 -o output.txt\n\n" \
"Input file specification:\n" \
"Input file starts with number of plants with int_32 type\n" \
"Plants contain fields:\n" \
"\tplant type: 1 - TREE, 2 - BUSH, 3 - FLOWER\n" \
"\tplant name with char[] type and 255 max length\n" \
"\tEvery plant contain fields:\n" \
"\t\t TREE: age with int_64 type.\n" \
"\t\t\t  example: `1 Christmas_tree 12` -> tree: (name = Christmas_tree, age = 12)\n" \
"\t\t BUSH: flowering month with int_32 type.\n" \
"\t\t\t  example: `2 Raspberry 11` -> bush: (name = Raspberry, flowering month = November)\n" \
"\t\t Flower: flower type with int_32 type. (1 - home, 2 - garden, 3- wild)\n" \
"\t\t\t  example: `3 Clever 1` -> flower: (name = Clever, flower type = home)\n" \
"See example at /tests" \

INPUT_FLAG_EXCEPTION_MESSAGE = "Error: Incorrect input flag syntax\n" \
"Try '-h' command for more information.\n"

OUTPUT_FLAG_EXCEPTION_MESSAGE = "Error: Incorrect Output flag syntax\n" \
"Try '-h' command for more information.\n"

RANDOM_FLAG_EXCEPTION_MESSAGE = "Error: Incorrect random input flag syntax\n" \
"Try '-h' command for more information.\n"


INPUT_FILE_NOT_EXIST_MESSAGE = "Input file does not exist\n"

kHelpFlag = "-h"

kInputFlag = "-i"

kOutputFlag = "-o"

kRandomFlag = "-r"

def IsFlagCorrect(input_flag, right_flag):
    if (input_flag == right_flag):
        return 1
    return 0


def FindFlag(argv, right_flag):
    for i in range(len(argv)):
        if (IsFlagCorrect(argv[i], right_flag)):
            return i
    return -1

def GetInputFile(argv):
    input_flag_position = FindFlag(argv, kInputFlag)

    if (input_flag_position != -1):
        if (input_flag_position + 1 < len(argv)):
            return argv[input_flag_position + 1]
        else:
            print(INPUT_FILE_NOT_EXIST_MESSAGE)
            exit(1)
    print(INPUT_FLAG_EXCEPTION_MESSAGE)
    exit(1)

def GetOutputFile(argv):
    output_flag_position = FindFlag(argv, kOutputFlag)

    if (output_flag_position != -1):
        if (output_flag_position + 1 < len(argv)):
            return argv[output_flag_position + 1]

    print(OUTPUT_FLAG_EXCEPTION_MESSAGE)
    exit(1)

def GetRandomSize(argv):
    random_flag_position = FindFlag(argv, kRandomFlag)
    if (random_flag_position != -1):
        if (random_flag_position + 1 < len(argv)):
            size = int(argv[random_flag_position + 1])

            if (size <= 0):
                print(RANDOM_FLAG_EXCEPTION_MESSAGE)
                print("Size could not be equal or less then 0\n")
                exit(1)
            return size
    return -1
