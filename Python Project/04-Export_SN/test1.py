import paramiko
import re

# 创建SSH客户端
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 连接华为交换机
ssh.connect('172.16.18.1', username="wj", password="Evil@12#$")

# 打开shell会话
channel = ssh.invoke_shell()

# 执行命令获取设备名称
command = 'display brief | include sysname'
stdin, stdout, stderr = ssh.exec_command(command)

# 获取输出设备名称
device_name = stdout.read().decode().split('sysame')[1].split('\n')[0]
print('输出设备名称：', device_name)

# 关闭shell会话
channel.close()

# 关闭SSH连接
ssh.close()