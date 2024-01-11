import os
import paramiko
import time

def send_space(channel):
    channel.send(' ')

def send_return(channel):
    channel.send('\n')

def read_output(channel):
    return channel.recv(65535).decode()

def read_until_more(channel):
    output = ''
    while True:
        output += read_output(channel)
        if '---- More ----' in output:
            send_space(channel)
            time.sleep(1)  # Add a short delay to allow the output to be captured
        else:
            break
    return output

# 读取IP.txt文件中的IP地址
with open('IP.txt', 'r') as ip_file:
    ip_list = ip_file.read().splitlines()

# 配置SSH连接信息
username = 'AAA'
password = 'AAA'
command = 'super\nAAA\ndis cu conf'

# 创建Config文件夹
if not os.path.exists('Config'):
    os.mkdir('Config')

# 循环处理每个IP
for ip in ip_list:
    try:
        # 建立SSH连接
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip, username=username, password=password)

        # 执行命令
        channel = ssh_client.invoke_shell()
        channel.send(command + '\n')
        output = read_until_more(channel)

        # 关闭SSH连接
        ssh_client.close()

        # 提取设备名
        device_name = ip.replace('.', '-')

        # 保存配置信息到文件
        config_filename = f'Config/{device_name}-{ip}.txt'
        with open(config_filename, 'w') as config_file:
            config_file.write(output)

        print(f"Config saved for {ip}")

    except Exception as e:
        print(f"Error connecting to {ip}: {str(e)}")
