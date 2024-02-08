import json


def generate_diff(filepath1, filepath2):

    with open(filepath1, 'r') as file:
        data1 = json.load(file)
    with open(filepath2, 'r') as file:
        data2 = json.load(file)

    keys1 = set(data1.keys())
    keys2 = set(data2.keys())
    all_keys = sorted(keys1 | keys2)

    diff = []

    for key in all_keys:
        if key in keys1 and key in keys2:
            if data1[key] != data2[key]:
                diff.append(f"  - {key}: {data1[key]}")
                diff.append(f"  + {key}: {data2[key]}")
            else:
                diff.append(f"    {key}: {data1[key]}")
        elif key in keys1:
            diff.append(f"  - {key}: {data1[key]}")
        elif key in keys2:
            diff.append(f"  + {key}: {data2[key]}")

    return '{\n' + '\n'.join(diff) + '\n}'
