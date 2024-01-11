# 导出华为交换机的配置信息
import os
import subprocess
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
ip_file_path = os.path.join(script_dir, 'IP.txt')

# 读取IP.txt文件中的IP地址
with open(ip_file_path, 'r') as ip_file:
    ip_list = ip_file.read().splitlines()

# 配置SSH连接信息
username = 'wj'
password = 'Evil@12#$'
command = 'display current-configuration configuration'

# 创建Config文件夹
if not os.path.exists('Config'):
    os.mkdir('Config')

# 配置SecurityCRT的安装路径
securityCRT_path = r'D:\Tools\SecureCRT\SecureCRT.exe'

# SecurityCRT宏脚本处理分页
macro_script = """
#$language = "VBScript"
#$interface = "1.0"
Sub main
    crt.screen.Synchronous = True
    crt.screen.Send "{command}" & vbCr
    Do
        crt.Screen.WaitForString "---- More ----"
        crt.Screen.Send " "
    Loop Until crt.Screen.WaitForString("return") = 1
    crt.Screen.Send "{enter}"
    crt.Screen.Synchronous = False
End Sub
"""

for ip in ip_list:
    try:
        # 构建SecurityCRT命令
        securityCRT_command = [
            securityCRT_path, # SecurityCRT可执行文件路径
            '/SSH2', # 使用SSH连接
            f'/L {username}', # 用户名
            f'/P {password}', # 密码
            f'/C "{command}"', # 执行的命令
            f'/T /S {ip}', # 目标IP地址
        ]
        # 执行ssh命令
        subprocess.run(securityCRT_command)

        # 提取设备名
        device_name = ip.replace('.', '-')

        # 保存配置信息到文件
        config_filename = f'Config/{device_name}-{ip}.txt'
        with open(config_filename, 'w') as config_file:
            config_file.write(output)

        print(f"Config saved for {ip}")

    except Exception as e:
        print(f"Error connecting to {ip}：{str(e)}")