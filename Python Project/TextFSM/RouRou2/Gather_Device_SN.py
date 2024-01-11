import paramiko
import pandas as pd

# 读取用户名和密码
with open('User&Pass.txt', 'r') as f:
    lines = f.readlines()
username = lines[1].strip()  # 第2行是用户名
password = lines[3].strip()  # 第4行是密码

# 读取IP地址
with open('IP.txt', 'r') as f:
    ip_list = f.read().splitlines()

# SSH连接设备并执行命令
results = []
for ip in ip_list:
    try:
        # 创建SSH客户端
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # 连接设备
        client.connect(ip, username=username, password=password)

        # 执行命令
        stdin, stdout, stderr = client.exec_command('display esn')
        output = stdout.read().decode().strip()

        # 将结果添加到列表中
        results.append((ip, output))

        # 关闭连接
        client.close()
    except Exception as e:
        print(f"连接设备{ip}时发生错误：{e}")

    # 将结果写入Excel文件
df = pd.DataFrame(results, columns=['IP', 'ESN'])
df.to_excel('设备SN.xlsx', index=False)
print("设备SN已写入到设备SN.xlsx文件中。")