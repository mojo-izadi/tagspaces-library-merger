import os
from collections import defaultdict

def find_duplicate_files_by_name(directory):
    file_dict = defaultdict(list)

    for root, _, files in os.walk(directory):
        for file in files:
            if ("~$" in file):
                continue
            file_path = os.path.join(root, file)
            file_dict[file].append(file_path)

    return {file: paths for file, paths in file_dict.items() if (len(paths) > 1)}


def find_duplicate_files_by_size(directory):
    file_dict = defaultdict(list)

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if (".ts" in file_path) or ("~$" in file):
                continue
            try:
                file_dict[os.path.getsize(file_path)].append(file_path)
            except FileNotFoundError:
                print(f"File '{file_path}' not found.")

    return {file: paths for file, paths in file_dict.items() if (len(paths) > 1)}


def write_duplicates_to_file(duplicate_dicts, output_file):
    with open(output_file, 'a', encoding='utf-8') as f:
        for duplicates in duplicate_dicts:
            if duplicates:
                f.write("Duplicate files found:\n")
                for file, paths in duplicates.items():
                    f.write(f"\n{file} is found in:\n")
                    for path in paths:
                        f.write(f" - {get_path_for_print(path)}\n")
            f.write('################################################\n')

def get_path_for_print(path):
    return '\\'.join(path.split("\\"))

directory_path = 'C:\\Users\\moham\\Desktop\\mo\\edu\\2'
output_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'duplicates.txt')
os.remove(output_file_path)
duplicates = [find_duplicate_files_by_size(directory_path), find_duplicate_files_by_name(directory_path)]
write_duplicates_to_file(duplicates, output_file_path)
print(f"Results have been written to {output_file_path}")