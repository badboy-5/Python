from jinja2 import Environment, FileSystemLoader
import json


def render_template_from_json(server_json, function_json, mgmt_json, location_json):
    # 读取管理服务器 JSON 文件
    with open(server_json, 'r', encoding='utf-8') as file:
        servers = json.load(file)

    # 读取功能 JSON 文件
    with open(function_json, 'r', encoding='utf-8') as file:
        functions = json.load(file)

    # 读取管理 JSON 文件
    with open(mgmt_json, 'r', encoding='utf-8') as file:
        mgmts = json.load(file)

    # 读取位置信息 JSON 文件
    with open(location_json, 'r', encoding='utf-8') as file:
        locations = json.load(file)

    # 定义设备信息和对应的模式
    device = {'server': servers, 'function': functions, 'mgmt': mgmts, 'location': locations}

    # 定义模板文件路径
    template_loader = FileSystemLoader(searchpath="./")
    env = Environment(loader=template_loader)
    template = env.get_template('Test_Muban.j2')

    # 渲染模板并传递变量
    rendered_template = template.render(device=device)

    # 打印渲染后的模板内容
    print(rendered_template)


if __name__ == "__main__":
    # 传入 JSON 文件名来渲染模板
    render_template_from_json('外网管理服务器.json', '功能配置.json', '管理接口.json', '位置信息.json')
