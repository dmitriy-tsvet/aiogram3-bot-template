import json


def read_txt(path: str, encoding="utf-8"):
    with open("{}.txt".format(path), "r", encoding=encoding) as file:
        text = file.read()
    return text


def read_json(path: str, encoding="utf-8") -> dict:
    with open(f'{path}.json', 'r', encoding=encoding) as file:
        data = json.load(file)
    return data


def write_json(data: dict, path: str, encoding="utf-8", ensure_ascii=False, indent=4):
    with open(f'{path}.json', 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=ensure_ascii, indent=indent)