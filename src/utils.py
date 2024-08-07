import json


def json_data():
    try:
        with open(
            r"C:\Users\User\My_Projects\project_2_git\data\operations.json",
            encoding="utf-8",
        ) as f:
            data = json.load(f)
        return data
    except Exception:
        return []
