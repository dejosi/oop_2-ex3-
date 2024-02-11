import os

def rewrite_file(directory,files):
    txt_list = []
    for file in files:
        if os.path.isfile(os.path.join(directory, file)) and file.endswith('.txt'):
            txt_list.append(file) 

    txt_dict = {}
    for txt_ in txt_list:
        with open(os.path.join(directory, txt_), 'r', encoding='utf-8') as file: 
            text =  file.readlines()
            txt_dict[txt_] = text
            sort_text = sorted(txt_dict, key=lambda x: len(x))   
            with open('file.txt','w',encoding='utf-8') as f:
                for i in sort_text:
                    f.write(i + '\n')
                    f.write(str(len(txt_dict[i])) + '\n')
                    f.write('\n'.join(txt_dict[i]) + '\n')
                f.close()

directory = "C:\\Users\\deyan\\Netology\\OOp_2D\\txt"
files = os.listdir(directory)
rewrite = rewrite_file(directory,files)
print(rewrite)