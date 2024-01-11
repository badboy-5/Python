import os

session_dir = "Sessions/"
output_file = "Moba.txt"

with open(output_file, 'w') as f:
    for dirpath, dirnames, filenames in os.walk(session_dir):
        # 只对第一个文件写入路径
        if dirpath == session_dir:
            relative_path = os.path.relpath(dirpath, session_dir)
            f.write(f"{relative_path}\n")
        for filename in filenames:
            if filename == "__FolderData__.ini":
                continue
            if filename.endswith(".ini"):
                file_name = os.path.splitext(filename)[0]
                # 分割文件名并获取第一个部分（即"["前的字符）
                ip_address = file_name.split("[")[0]
                # 将字符串中的"IPADDR"替换为文件名中的"["前的字符
                modified_string = "AAAA%sB" % ip_address
                # 将修改后的文件名写入文件
                f.write(modified_string + "\n")