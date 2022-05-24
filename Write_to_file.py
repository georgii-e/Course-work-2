import os


def clear_file(path):
    try:
        os.remove(path)
    except OSError:
        pass


def write_to_file(sort_info, path):
    lst = sort_info.get_list()
    line1 = "Sort method: " + sort_info.get_name() + "\n"
    line2 = "Number of elements: " + str(len(lst)) + "\n"
    line3 = "Count of swaps: " + str(sort_info.get_swaps()) + "\n"
    line4 = "Count of comparisons: " + str(sort_info.get_comparisons()) + "\n"
    lst = ' '.join(map(str, lst)) + "\n\n"
    with open(path, 'at') as text_to_file:
        text_to_file.write(line1 + line2 + line3 + line4 + lst)
