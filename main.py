import sys
import time

from container.contaoner import Container
from file_worker.file_worker import *

INPUT_FILE = ""
OUTPUT_FILE = ""
RANDOM_PLANTS = list()


def set_input_file(input_file: str):
    global INPUT_FILE
    INPUT_FILE = input_file


def set_output_file(output_file: str):
    global OUTPUT_FILE
    OUTPUT_FILE = output_file


def main(args):
    start_time = time.perf_counter()
    if (len(args) < 5):
        if (len(args) == 2):
            if (IsFlagCorrect(args[1], kHelpFlag)):
                print(HELP_MESSAGE)
                exit(0)
        print("Error: Incorrect flags or flags number")
        exit(1)

    set_output_file(GetOutputFile(args))
    size = GetRandomSize(args)
    f = open(OUTPUT_FILE, 'w')
    f.close()

    if (size == -1):
        print("Read input file")
        set_input_file(GetInputFile(args))
        container = Container.read_input(INPUT_FILE)
    else:
        print("Generate plant")
        container = Container.random(size)

    container.out(OUTPUT_FILE)
    print("Sorting")
    f = open(OUTPUT_FILE, 'a')
    f.write("\n==================== sort result ====================\n\n")
    f.close()
    container.straight_insertion()
    container.out(OUTPUT_FILE)
    print("End")
    print(f"Work time: {time.perf_counter() - start_time}")


if __name__ == "__main__":
    main(sys.argv)
