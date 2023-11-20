import os
import sys 
import csv
def file_search(dirname, ret, list_avoid_dir=[]): 
    filenames = os.listdir(dirname)
    for filename in filenames: 
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            if full_filename.split("/")[-1] in list_avoid_dir:
                continue
            else: 
                file_search(full_filename, ret, list_avoid_dir)
        else: 
            ret.append(full_filename)
            
def find_encoding(filename):
    rawdata = open(filename, 'rb').read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    
def create_folder(dir_name): 
    if not os.path.exists(dir_name): 
        os.makedirs(dir_name)
        
def extract_trans(list_in_file, out_file):
    lines = []
    for in_file in list_in_file:
        cnt = 0
        encodings_to_try = ['latin-1', 'ISO-8859-1', 'utf-16']
        lines = None
        
        for encoding in encodings_to_try:
            try:
                with open(in_file, 'r', encoding=encoding) as f1:
                    lines = f1.readlines()
                break  # If successful, exit the loop
            except UnicodeDecodeError:
                print(f"Failed to decode {in_file} with {encoding} encoding. Trying another encoding.")
                continue
        
        with open(out_file, 'a', encoding='latin-1') as f2:  # Use 'a' for append mode
            csv_writer = csv.writer(f2)
            lines = sorted(lines)
            
            for line in lines:
                name = line.split(':')[0].split(' ')[0].strip()
                if name[:3] != 'Ses': 
                    continue
                elif name[-3: -1] == 'XX': 
                    continue
                trans = line.split(':')[1].strip()
                cnt += 1
                csv_writer.writerow([name, trans])

def find_category(lines):
    list_category = ['ang', 'hap', 'sad', 'neu', 'fru', 'exc', 'fea', 'sur', 'dis', 'oth', 'xxx']
    category = {}
    for cate in list_category: 
        if category.__contains__(cate):
            pass
        else: 
            category[cate] = len(category)
    is_target = True
    id = ''
    c_label = ''
    list_ret = []
    for line in lines: 
        if is_target == True: 
            try: 
                id = line.split('\t')[1].strip()
                label = line.split('\t')[2].strip()
                if not category.__contains__(label):
                    print('ERROR: we can\'t find ', label)
                    sys.exit()
                list_ret.append([id, label])
                is_target = False
            except: 
                print('ERROR ', lone)
                sys.exit()
        else:
            if line == '\n':
                is_target = True
    return list_ret

    

def extract_labels(list_in_file, out_file) :
    id = ''
    lines = []
    list_ret = []
    
    for in_file in list_in_file:
        
        with open(in_file, 'r') as f1:
            lines = f1.readlines()
            lines = lines[2:]                           # remove head
            list_ret = find_category(lines)
            
        list_ret = sorted(list_ret)                   # sort based on first element
    
        with open(out_file, 'a') as f2:
            csv_writer = csv.writer(f2)
            csv_writer.writerows(list_ret)
        