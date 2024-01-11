import json

Json_file = "apipost用例.json"

with open(Json_file, encoding='utf8') as f:
    json_data = f.read()
js_dic = json.loads(json_data)
js = json.dumps(js_dic, sort_keys=True, indent=4, separators=(',', ':'))
print(js)