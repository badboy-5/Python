# 将CRT的Session转换为MobaXterm会话
import os

sessions_dir = 'Sessions'
output_file = 'Moba.txt'

# 打开输出文件，准备写入
with open(output_file, 'w') as f:
    # 遍历Sessions目录下的所有子目录
    for root, dirs, files in os.walk(sessions_dir):
        # 记录当前目录是否已经写入过路径信息
        has_written_path = False
        # 遍历当前目录下的所有文件
        for file in files:
            # 如果文件名中包含"FolderData"，则跳过这个文件
            if '__FolderData__.ini' in file:
                continue
                # 如果文件以.ini结尾，则去掉这个后缀
            if file.endswith('.ini'):
                file = file[:-4]
                # 如果这是子目录下的第一个文件，且当前目录还没有写入过路径信息，则在其文件名前加上子目录的绝对路径
            if not has_written_path:
                f.write('[Bookmark_]\n')
                f.write('SubRep=' + os.path.join(sessions_dir, root[len(sessions_dir) :]) + '\n')
                f.write('ImgNum=37\n')
                has_written_path = True
                # 将文件名写入到新文件中
            # 分割文件名并获取第一个部分（即"["前的字符）
            ip_address = file.split("[")[0]
            f.write(file + '=#109#0%' + ip_address + '%22%[wj]' + '\n')