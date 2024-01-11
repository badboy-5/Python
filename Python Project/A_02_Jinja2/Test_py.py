from jinja2 import Environment, FileSystemLoader

def render_template(device_mode):
    # 定义内网设备的各类服务器 IP 列表
    internal_servers = {
        'ssh_ips': ['10.137.252.159 0', '10.136.3.0 0.0.0.31', '22.48.7.0 0.0.0.15', '122.48.9.0 0.0.0.15'],
        'ntp_servers': '10.137.252.67',
        'snmp_servers': '10.137.252.159',
        'syslog_servers': '10.137.252.159',
        'tacacs_servers': ['25.194.136.64', '25.194.136.155']
        # 可以继续添加其他服务器类型和对应的 IP 列表
    }

    # 定义外网设备的各类服务器 IP 列表
    external_servers = {
        'ssh_ips': ['172.19.252.50 0', '172.19.5.0 0.0.0.15', '172.19.27.0 0.0.0.15', '172.19.29.0 0.0.0.15'],
        'ntp_servers': ['202.107.201.1', '202.107.201.2'],
        'snmp_servers': '172.19.252.50',
        'syslog_servers': '172.19.252.50',
        'tacacs_servers': ['172.19.225.180', '172.19.225.181'],
        'port_secure': 'enable',
        'dhcp_snooping': 'enable',
        'vrf': 'IPMI',
        'mgmt_port': 'vlan',
        'mgmt_port_id': '4000',
        'mgmt_ip': '172.16.57.11 26',
        'mgmt_gateway': '172.16.57.254'
        # 可以继续添加其他服务器类型和对应的 IP 列表
    }

    # 根据选择的设备类型，确定要使用的服务器 IP 列表
    if device_mode == '内网':
        selected_servers = internal_servers
    elif device_mode == '外网':
        selected_servers = external_servers
    else:
        print("无效的设备类型")
        return

    # 定义设备信息和对应的模式
    device = {'mode': device_mode, 'servers': selected_servers}

    # 定义模板文件路径
    template_loader = FileSystemLoader(searchpath="./")
    env = Environment(loader=template_loader)
    template = env.get_template('Test_Muban.j2')  # 替换为你的模板文件名

    # 渲染模板并传递变量
    rendered_template = template.render(device=device)

    # 打印渲染后的模板内容
    print(rendered_template, end='')


if __name__ == "__main__":
    # 选择设备类型并渲染对应配置
    chosen_device_mode = '外网'  # 在这里设置 '内网' 或 '外网'
    render_template(chosen_device_mode)
