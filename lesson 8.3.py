import os
def read_files(filepath, readfiles):
    may_dict = {}
    for files in os.listdir(filepath):
        my_files = []
        if files.endswith(readfiles):
            my_files.append(files)
            may_list = []
            for i in my_files:
                with open(i, encoding='utf-8') as file:
                    for line in file:
                        may_list.append(line) 
            may_dict[len(may_list)] = [i, may_list]
    return may_dict

result_may_dict = read_files('F:\Lesson opening and reading a file, writing to a file\Lesson 8.3', '.txt')

print(result_may_dict)

def writе_file(data, folder, recordfile):
    file_path = os.path.join(os.path.join(os.getcwd(), folder), recordfile)
    for k in sorted(data.keys()):
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{data[k][0]}\n')
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f'{str(k)}\n')
        for may_dict in data[k][1]:
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write(may_dict)

writе_file(result_may_dict, 'recording file', 'shared_file.txt')

