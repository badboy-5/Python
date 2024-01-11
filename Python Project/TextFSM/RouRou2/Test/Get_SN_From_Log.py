import os
import pandas as pd
from textfsm import TextFSM

# 定义文件夹路径和模板文件路径
log_folder = "Log_Files"
template_file = "parser.textfsm"

# 获取文件夹中所有的.log文件
log_files = [f for f in os.listdir(log_folder) if f.endswith('.log')]

# 创建一个空的DataFrame用于存储结果
df = pd.DataFrame(columns=["设备IP", "设备SN"])

# 对于每一个.log文件
for log_file in log_files:
    # 读取文件内容
    with open(os.path.join(log_folder, log_file), 'r') as f:
        log_content = f.read()

        # 使用TextFSM模板进行匹配
    with open(template_file, 'r') as f:
        template = TextFSM(f)
        result = template.ParseText(log_content)

        # 将文件名（不包含文件后缀名）和设备SN添加到DataFrame中
    for row in result:
        df = pd.concat([df, pd.DataFrame([{"设备IP": log_file[:-4], "设备SN": row[0]}])], ignore_index=True)

    # 将结果写入Excel文件
df.to_excel("设备SN.xlsx", index=False)