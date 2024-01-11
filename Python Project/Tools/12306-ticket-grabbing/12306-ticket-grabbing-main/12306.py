from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from selenium.webdriver.common.keys import Keys
import time
import select

def isElementExist(driver):
    flag=True
    ele = driver.find_elements(by=By.CSS_SELECTOR, value='.no-br .btn72')
    if len(ele) == 0:
        return flag
    else:
        flag = False
        return flag

def isLogin():
    # 账号密码登录
    try:
        username_tag = driver.find_element(by=By.ID, value='J-userName')
        username_tag.send_keys(conf.username)
        password_tag = driver.find_element(by=By.ID, value='J-password')
        password_tag.send_keys(conf.password)
        login_now = driver.find_element(by=By.ID, value='J-login')
        # login_now = driver.find_element(by=By.CLASS_NAME, value='login-hd-account')
        login_now.click()
    except BaseException as be:
        print("已经登陆过")




def get_ticket(conf, driver, url):
    # 过网站检测，没加这句的话，账号密码登录时滑动验证码过不了，但二维码登录不受影响
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined})"""})
    driver.maximize_window()
    driver.get(url)
    # 最多等待5秒使页面加载进来，隐式等待
    driver.implicitly_wait(5)

    # 获取并点击右上角登录按钮
    login = driver.find_element(by=By.ID, value='J-btn-login')
    login.click()
    driver.implicitly_wait(10)

    # 账号密码登录
    # username_tag = driver.find_element(by=By.ID, value='J-userName')
    # username_tag.send_keys(conf.username)
    # password_tag = driver.find_element(by=By.ID, value='J-password')
    # password_tag.send_keys(conf.password)
    # login_now = driver.find_element(by=By.ID, value='J-login')

    # 扫码登陆
    # login_now = driver.find_element(by=By.CLASS_NAME, value='login-hd-account')

    # login_now.click()
    time.sleep(2)

    # # 过滑动验证码
    # picture_start = driver.find_element(by=By.ID, value='nc_1_n1z')
    # # 移动到相应的位置，并左键鼠标按住往右边拖
    # ActionChains(driver).move_to_element(picture_start).click_and_hold(picture_start).move_by_offset(300, 0).release().perform()

    driver.implicitly_wait(30)

    # 点击车票预订跳转到预订车票页面
    driver.find_element(by=By.XPATH, value='//*[@id="link_for_ticket"]').click()
    driver.implicitly_wait(10)

    # 输入出发地和目的地信息
    # 出发地
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').click()
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').clear()
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').send_keys(conf.fromstation)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="fromStationText"]').send_keys(Keys.ENTER)

    # 目的地
    destination_tag = driver.find_element(by=By.XPATH, value='//*[@id="toStationText"]')
    destination_tag.click()
    destination_tag.clear()
    destination_tag.send_keys(conf.destination)
    time.sleep(1)
    destination_tag.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)

    # 出发日期
    date_tag = driver.find_element(by=By.XPATH, value='//*[@id="train_date"]')
    date_tag.click()
    date_tag.clear()
    date_tag.send_keys(conf.date)
    time.sleep(1)

    start = time.time()

    while True:
        
        try:
            # 点击查询
            driver.find_element(by=By.ID, value='query_ticket').click()
            # 判断页面中有没有“预订”按钮，如果没有预订按钮就不断查询直到车票开售
            if  isElementExist(driver):
                # 车票处于待开售状态，或全部没有票状态
                print(f"14点30分起售，现在是{time.strftime('%H:%M:%S', time.localtime())}，还未开始售票")
                # 每隔两分钟刷新一次，否则3分钟内无购票操作12306系统会自动登出
                if time.time() - start >= 120:
                    driver.refresh()
                    start = time.time()
                    print("页面刷新")
                continue
        except BaseException as ex:
            print("错误：%s"%ex)
        

        # 获取所有车票
        tickets = driver.find_elements(by=By.XPATH, value='//*[@id="queryLeftTable"]/tr')
        # 每张车票有两个tr，但是第二个tr没什么用
        tickets = [tickets[i] for i in range(len(tickets) - 1) if i % 2 == 0]
        for ticket in tickets:
                # 如果车票的车次等于想要的车次并且硬卧的状态不是候补则点击预订
                #if ticket.find_element(by=By.CLASS_NAME,value='cdz').text== conf.fromstation:
                    #print(ticket.find_element(by=By.CLASS_NAME,value='number').text)
                    # value = '//td[8]'表示硬卧，td[10]表示硬座 O 二等座，M 一等座，P 特等座
                td =  "3" if  conf.seatType == "O" else  "2" if  conf.seatType == "M" else "1"
                print(td)
                if ticket.find_element(by=By.CLASS_NAME,value='number').text == conf.trainnumber and ticket.find_element(by=By.XPATH, value='//td['+td+']').text != "候补":
                    print( ticket.find_element(by=By.CLASS_NAME,value='number').text)
                    print( conf.trainnumber )
                    # 点击预订
                    print(ticket.find_element(by=By.CLASS_NAME,value='cdz').text)
                    ticket.find_element(by=By.CLASS_NAME,value="btn72").click()
                    time.sleep(1)
                    #判断是否已经登陆，如果没有登陆会弹出登陆窗口
                    isLogin()
                
                    while True:
                        driver.implicitly_wait(5)
                        try:
                            # 选择乘车人，如果是学生，则需要确认购买学生票
                            driver.find_element(by=By.XPATH, value='//*[@id="normalPassenger_0"]').click()
                            # 点击确认购买学生票，如果不是学生，把这行注释了就行
                            #driver.find_element(by=By.XPATH, value='//*[@id="dialog_xsertcj_ok"]').click()
                            # 第二个乘车人
                            # driver.find_element(by=By.XPATH, value='//*[@id="normalPassenger_1"]').click()
                            # 如果第二个乘车人也是学生，则需要点击确认第二个人也购买学生票
                            # driver.find_element(by=By.XPATH, value='//*[@id="dialog_xsertcj_ok"]').click()
                            #车票类型
                            caType=  driver.find_element(by=By.ID, value='seatType_1')
                            #O 二等座，M 一等座，P 特等座
                            caType.find_element(by=By.CSS_SELECTOR,value="option[value='"+conf.seatType+"']").click() #特等座
                            # 提交订单
                            driver.find_element(by=By.XPATH, value='//*[@id="submitOrder_id"]').click()
                            # 选座  F座
                            time.sleep(1)
                            #这里直接使用id和xpath定位不到，所以直接加上他的路径,可以不用这么长，但是懒得删
                            driver.find_element(by=By.XPATH, value='//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[2]/li[2]/a[@id="1F"]').click()
                            # 确认提交订单，然后这里和上面是一样的
                            # driver.find_element(by=By.XPATH, value='//html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[8]/a[2][@id="qr_submit_id"]').click()
                            # print(f"{conf.trainnumber}次列车抢票成功，请尽快在10分钟内支付！")
                            return
                        except BaseException as e:
                            print("填写购票信息失败！")
            


if __name__ == '__main__':
    # 有关车票的配置信息保存在该类里
    # 请事先在config.py里填好相关信息
    conf = Config()

    url = 'https://www.12306.cn/index/'

    # chromedriver.exe版本为104，可以根据自己浏览器版本重新下载chromedriver.exe替换
    # chromedriver.exe下载地址：http://chromedriver.storage.googleapis.com/index.html
    s = Service('/Users/a123456/Downloads/chromedriver_mac_arm64/chromedriver')
    s = Service('./chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    get_ticket(conf, driver, url)
    time.sleep(10)
    driver.quit()
