import json


def read_from_file(filepath="data.json"):
    with open(filepath, 'r', encoding='utf-8') as f_obj:
        data = json.load(f_obj)

    return data


def write_to_file(data, filepath="data.json"):
    with open(filepath, 'w', encoding='utf-8') as f_obj:
        json.dump(data, f_obj, sort_keys=True, indent=4, separators=(',', ': '))
