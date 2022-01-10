import sys

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
        set_input_file(GetInputFile(args))
        container = Container.read_input(INPUT_FILE)
    else:
        container = Container.random(size)

    container.out(OUTPUT_FILE)
    container.straight_insertion()
    container.out(OUTPUT_FILE)




    # flags_handler = Flags.FlagHandler([RANDOM_INPUT_FLAG, INPUT_FLAG, OUTPUT_FLAG])
    # flags_handler.from_args(args)
    # for flag in flags_handler.known_flags:
    #     print(flag.__repr__())
    # flags_handler.handle_all()
    #
    # #  Checks flags.
    # if not INPUT_FLAG.state:
    #     Logger.log("No input file in parameters!", Logger.LogType.WARNING)
    #     return
    #
    # if not OUTPUT_FLAG.state:
    #     Logger.log("No output file in parameters!", Logger.LogType.WARNING)
    #     return
    #
    # if RANDOM_INPUT_FLAG.state:
    #     Logger.log("Random mode ON.", Logger.LogType.INFO)
    #     write_to_file(INPUT_FILE, RANDOM_PLANTS)
    #
    # #  Reading container.
    # container = Container.Container.from_file(INPUT_FILE)
    #
    # #  Show main information about container on screen.
    # print("Input:")
    # for c in range(container.length()):
    #     print(container[c])
    #
    # #  Sorting.
    # start_time = time.perf_counter()
    # container = Container.Container.from_list(MergeSort.straight_merge(container.c))
    # seconds_left = f"{(time.perf_counter() - start_time):0.6f}"
    # write_result(OUTPUT_FILE, container, seconds_left)
    # print("\nResult:")
    # for elem in container:
    #     print(elem)
    # Logger.log(f"{seconds_left} seconds left.", Logger.LogType.INFO)


if __name__ == "__main__":
    main(sys.argv)
