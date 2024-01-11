def add_annotation(target_file, section, command, annotations, matched_sections):
    if section in annotations and section not in matched_sections:
        annotation = annotations[section]
        target_file.write("{}\n".format(annotation))
        matched_sections.add(section)
#    target_file.write("{}\n".format(command))

source_file_path = "1.txt"
with open(source_file_path, "r", encoding="utf-8") as source_file:
    source_lines = source_file.readlines()

target_file_path = "2.txt"
with open(target_file_path,"w", encoding="utf-8") as target_file:
    target_file.write("# Config Huawei Switch\n")
    target_file.write("# Original configuration Source from:{}\n\n".format(source_file_path))

    current_section = None
    annotations = {
        "sysname": "# 配置设备名称",
        "ftp": "# 配置FTP服务器",
        "info-center": "# 配置syslog",
        "device": "# 配置离线设备",
        "ntp": "# 配置NTP服务",
        "dfs-group": "# 配置动态交换服务组",
        "vlan": "# 创建相关VLAN",
        "stp": "# 配置STP",
        "telnet": "# 配置SSH远程管理",
        "hwtacacs": "# 配置Tacacs",
        "traffic-policy": "# 调用流策略",
        "observe-port": "# 配置流量观察端口",
        "ip vpn-instance": "# 配置VRF",
        "acl": "# 配置ACL",
        "aaa": "# 配置AAA",
        "interface Vlanif": "# 配置VLANIF接口",
        "interface MEth0/0/0": "# 配置管理接口",
        "interface Eth-Trunk": "# 配置聚合接口",
        "ip route-static": "# 配置静态路由",
        "snmp-agent": "# 配置SNMP",
        "lldp": "# 配置LLDP",
        "stelnet": "# 配置SSH服务",
        "nqa": "# 配置NQA",
        "user-interface con 0": "# 配置Console接口登录密码",
        "user-interface vty 0 20": "# 配置SSH远程管理"
    }

    matched_sections = set()

    for line in source_lines:
        line = line.strip()
        if line.startswith("#"):
            target_file.write(line + "\n")
            continue
        if line.startswith("sysname") or \
            line.startswith("ftp") or \
            line.startswith("info-center") or \
            line.startswith("device") or \
            line.startswith("ntp") or \
            line.startswith("dfs-group") or \
            line.startswith("vlan") or \
            line.startswith("stp") or \
            line.startswith("telnet") or \
            line.startswith("hwtacacs") or \
            line.startswith("traffic-policy") or \
            line.startswith("observe-port") or \
            line.startswith("ip vpn-instance") or \
            line.startswith("acl") or \
            line.startswith("aaa") or \
            line.startswith("interface Vlanif") or \
            line.startswith("interface MEth0/0/0") or \
            line.startswith("interface Eth-Trunk") or \
            line.startswith("ip route-static") or \
            line.startswith("snmp-agent") or \
            line.startswith("lldp") or \
            line.startswith("stelnet") or \
            line.startswith("nqa") or \
            line.startswith("user-interface con 0") or \
            line.startswith("user-interface vty 0 20"):
            current_section = line.split()[0]
        if current_section:
            add_annotation(target_file, current_section, line, annotations, matched_sections)
        target_file.write(line + "\n")

print("Added and saved to:",target_file_path)