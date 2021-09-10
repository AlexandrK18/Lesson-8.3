import os

may_dict = {}
for files in os.listdir('F:\Lesson opening and reading a file, writing to a file\Lesson 8.3'):
    my_files = []
    if files.endswith('.txt'):
        my_files.append(files)
        may_list = []
        for i in my_files:
            with open(i, encoding='utf-8') as file:
                for line in file:
                    may_list.append(line) 
        may_dict[len(may_list)] = [i, may_list]

file_path = os.path.join(os.path.join(os.getcwd(), 'recording file'), 'shared_file.txt')

for k in sorted(may_dict.keys()):
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'{may_dict[k][0]}\n')
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(f'{str(k)}\n')
    for may_dict1 in may_dict[k][1]:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(may_dict1)



