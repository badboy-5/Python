# 导出华为交换机的配置信息
import os
import subprocess
import time

# 读取IP.txt文件中的IP地址
with open('IP.txt', 'r') as ip_file:
    ip_list = ip_file.read().splitlines()

# 配置SSH连接信息
username = 'wj'
password = 'Evil@12#$'
command = 'display current-configuration configuration'

# 创建Config文件夹
if not os.path.exists('Config'):
    os.mkdir('Config')

for ip in ip_list:
    try:
        ssh_command =[
            'ssh', '-oStrictHostKeyChecking=no',
            f'{username}@{ip}',
            command
        ]

        ssh_process = subprocess.Popen(
            ssh_command,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True
        )

        # 读取命令输出，并处理分页
        output = ''
        while True:
            line = ssh_process.stdout.readline()
            if '---- More ----' in line:
                ssh_process.stdin.write(' ')
                ssh_process.stdin.flush()
            else:
                output += line
            if not line:
                break

            ssh_process.stdin.close()
            ssh_process.wait()

        # 保存配置信息到文件
        device_name = ip.replace('.', '-') # 提取设备名
        config_filename = f'Config/{device_name}-{ip}.txt'
        with open(config_filename, 'w') as config_file:
            config_file.write(output)

        print(f"Config saved for {ip}")

    except Exception as e:
        print(f"Error connecting to {ip}：{str(e)}")