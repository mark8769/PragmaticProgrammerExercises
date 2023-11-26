import yaml
import os
import json

def get_yaml_file_list(dir):
    return os.listdir(dir)
    
def convert_yaml_to_json_file(filepath, dest_dir):
    
    filename = filepath.split(".")[0].split("/")[1]
    new_name = "JSONFiles/{}.json".format(filename)
    # create_dir_if_not_exist(check_dir_exists(new_name), new_name)
    
    with open(filepath, 'r') as file:
        yaml_file = yaml.safe_load(file)
    
    with open(new_name, 'w') as json_file:
        json.dump(yaml_file, json_file)

def check_dir_exists(dir):
    print("Exists: ", os.path.isdir(dir))
    return os.path.isdir(dir)
    
def create_dir_if_not_exist(is_exist, dir) -> None:
    if (not is_exist):
        print("Making new directory.")
        os.mkdir(dir)

if __name__ == "__main__":
    
    # Relative since this is a quick solution.
    dir = "YamlFiles"
    dest_dir = "JSONFiles"
    create_dir_if_not_exist(check_dir_exists(dest_dir), dest_dir)
    filepaths = get_yaml_file_list(dir)
    
    for filepath in filepaths:
        full_path = "{}/{}"
        convert_yaml_to_json_file(full_path.format(dir, filepath), dest_dir)
    
