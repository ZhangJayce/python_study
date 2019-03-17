import os

root_path = r"F:\WeGame"

def  recursion_list_all_file_or_dir(path):
    list_tmp = os.listdir(path)

    for file_path in list_tmp:
        file_path = os.path.join(path,file_path)
        if os.path.isdir(file_path):
            print("debug: ",file_path)
            recursion_list_all_file_or_dir(file_path)
        else:
            print(file_path)


print(recursion_list_all_file_or_dir(root_path))



