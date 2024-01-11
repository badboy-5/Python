from textfsm import TextFSM
import json

if __name__ == '__main__':
    with open('OutPut_Log.txt', 'r', encoding='utf8') as f:
        show_text = f.read()

    with open('parser.textfsm', encoding='utf8') as textfsm_file:
        template = TextFSM(textfsm_file)
        datas = template.ParseTextToDicts(show_text)
        print(json.dumps(datas, indent=4))