import requests
from bs4 import BeautifulSoup

url = "http://redhat.ytlinux.com/vm/PiFo6IV.aspx"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

div_list=[]
# 找到包含<fieldset>标签的父div
fieldset_parent = soup.find('fieldset', id='fieldset1')

# 检查是否找到了元素
if fieldset_parent is not None:
    # 循环遍历每个子div
    for div_html in fieldset_parent.children:
        if div_html.name == 'div':  # 只处理div标签
            div_list.append(div_html.get('id'))
else:
    print("未找到具有 id='fieldset1' 的 div 元素")
print(div_list)  # 打印每个子div的id

for item in div_list:
    div_html = soup.find('div', id=item)
    div_child=div_html.find('div',class_='topichtml')
    # 题目
    text = div_child.get_text()
    print(text)

    # 提取img标签的src属性
    try:
        img_src = "http:" + div_child.img['src']
        print("img地址：", img_src)
    except Exception as E:
        pass

    if text:
        # 查找所有选项的div元素
        S_options = div_html.find_all('div', class_='ui-radio')
        M_options = div_html.find_all('div', class_='ui-checkbox')
        T_options = div_html.find_all('div', attrs={'ans': True})
        # 遍历每个选项，并提取选项文本内容
        for option in S_options:
            label = option.find('div', class_='label')  # 查找标签元素
            if label:  # 确保标签元素存在
                option_text = label.get_text()  # 提取文本内容
                print(option_text)  # 打印选项文本内容
        if 'ans' in option.attrs:
            print(f"The ans value is: ", option_text)

        for option in M_options:
            label = option.find('div', class_='label')  # 查找标签元素
            if label:  # 确保标签元素存在
                option_text = label.get_text()  # 提取文本内容
                print(option_text)  # 打印选项文本内容