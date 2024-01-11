def get_intf(line):
    name, *others, bw = line.split()
    name, intf_state, line_state, _, mtu, bw = line.split()

with open(r'.\Device.log', 'r', encoding='utf8', errors='ignore') as f:
    log = f.readlines()
    for line in log:
        print(line.strip())