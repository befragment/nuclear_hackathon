import os

FIRST_WRIST_INDEX = 9
SECOND_WRIST_INDEX = 10

def get_last_directory_contents(root_folder):

    num_lst = [int(i[7:]) for i in os.listdir(root_folder) if i[-1].isdigit()]
    max_l = max(num_lst)
    print(num_lst)
    return f'{root_folder}/predict{max_l}'




    