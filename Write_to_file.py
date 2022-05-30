import os


def clear_file(path):
    try:
        os.remove(path)
    except OSError:
        pass


def write_to_file(sort_info, path):
    final_lst = sort_info.get_list()
    initial_lst = sort_info.get_initial_list()
    line1 = "Sort method: " + sort_info.get_name() + "\n"
    line2 = "Number of elements: " + str(len(final_lst)) + "\n"
    line3 = "Count of swaps: " + str(sort_info.get_swaps()) + "\n"
    line4 = "Count of comparisons: " + str(sort_info.get_comparisons()) + "\n"
    line5 = "Initial array\n" + ' '.join(map(str, initial_lst)) + "\n"
    line6 = "Final array\n" + ' '.join(map(str, final_lst)) + "\n\n"
    with open(path, 'at') as text_to_file:
        text_to_file.write(line1 + line2 + line3 + line4 + line5 + line6)
