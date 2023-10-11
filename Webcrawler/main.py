from selenium import webdriver
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import csv
import time
import requests
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.keys as Keys
import pyautogui as pg
import pyperclip as pp
import os



def ret(Xpath, driver):
    try:
        driver.find_element(By.XPATH, Xpath)
    except:
        return False
    else:
        return True

def ret_chapter(Xpath, driver):
    try:
        driver.find_element(By.XPATH, Xpath)
    except:
        return 1
    else:
        cha_lis = driver.find_elements(By.CLASS_NAME, 'chapter-name')
        act_lis = driver.find_elements(By.CLASS_NAME, 'active-name')
        a = driver.find_element(By.XPATH, Xpath)
        if a in cha_lis:
            return 2
        if a in act_lis:
            return 3
#
# # with open('data1.csv', 'w', newline='', encoding='utf-8-sig') as file:
# #     writer = csv.writer(file)
# #     writer.writerow(['学段', '年级', '学科', '版本', '册次', '单元', '文章'])
# #
# option = webdriver.ChromeOptions()  # 禁止网页自动关闭
# option.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=option)  # 创建webdriver实例
# url = 'https://basic.smartedu.cn/syncClassroom'
# driver.get(url)
# time.sleep(2)

# data = driver.page_source
# print('page source is ' + str(data))
#
xueduan = ''
nianji = ''
xueke = ''
banben = ''
ceci = ''
danyuan = ''
content = ''
XueDuan_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[1]/div[2]/label['
Xueduan_right = ']/span[2]'


#
# for xd in range(5,21):
#     if xd != 5:
#         XueDuan = XueDuan_left + str(xd) + Xueduan_right  # xd是学段的缩写
#         try:
#             driver.find_element(By.XPATH, XueDuan).click()
#         except:
#             break  # 如果出错了，就代表这个栏里面没有那么多东西，所以就直接break掉就可以
#         else:
#             xueduan = driver.find_element(By.XPATH, XueDuan).text
#             time.sleep(2)
#             NianJi_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/label['
#             NianJi_right = ']/span[2]'
#             for nj in range(1,21):
#                 NianJi = NianJi_left + str(nj) + NianJi_right
#                 try:
#                     driver.find_element(By.XPATH, NianJi).click()
#                 except:
#                     break
#                 else:
#                     nianji = driver.find_element(By.XPATH, NianJi).text
#                     time.sleep(2)
#                     XueKe_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/label['
#                     XueKe_right = ']/span[2]'
#                     for xk in range(2, 21):
#                         XueKe = XueKe_left + str(xk) + XueKe_right
#                         try:
#                             driver.find_element(By.XPATH, XueKe).click()
#                         except:
#                             break
#                         else:
#                             time.sleep(2)
#                             xueke = driver.find_element(By.XPATH, XueKe).text
#                             BanBen_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[4]/div[' \
#                                           '2]/label[ '
#                             BanBen_right = ']/span[2]'
#                             for bb in range(1,21):
#                                 BanBen = BanBen_left + str(bb) + BanBen_right
#                                 try:
#                                     driver.find_element(By.XPATH, BanBen).click()
#                                 except:
#                                     break
#                                 else:
#                                     time.sleep(2)
#                                     banben = driver.find_element(By.XPATH, BanBen).text
#                                     CeCi_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[' \
#                                                 '5]/div[2]/label[ '
#                                     CeCi_right = ']/span[2]'
#                                     for cc in range(2, 21):
#                                         Ceci = CeCi_left + str(cc) + CeCi_right
#                                         try:
#                                             driver.find_element(By.XPATH, Ceci).click()
#                                         except:
#                                             break
#                                         else:
#                                             time.sleep(2)
#                                             ceci = driver.find_element(By.XPATH, Ceci).text
#                                             # print(xueduan + ' ' + nianji + ' ' + xueke + ' ' + banben + ' ' + ceci)
#                                             # 到这里，已经模拟了所有的点击操作，现在只需要把目录下的每一节课都爬下来就可以了
#                                             # 展开所有的目录
#                                             # driver.find_element(By.XPATH, '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[3]/div/div/div/div[1]/span[3]/span/div/span[2]').click()
#                                             time.sleep(2)
#                                             chapter_lis = driver.find_elements(By.CLASS_NAME, 'chapter-name')
#                                             for i in range(1, len(chapter_lis)):
#                                                 chapter_lis[i].click()
#                                                 time.sleep(2)
#
#                                             driver.execute_script("var q=document.documentElement.scrollTop=0")  # 回到顶部，否则会出现错误
#                                             time.sleep(2)
#
#                                             chapter_lis1 = driver.find_elements(By.CLASS_NAME, 'chapter-name')
#                                             for i in range(1, len(chapter_lis1)):
#                                                 if chapter_lis1[i] not in chapter_lis:
#                                                     chapter_lis1[i].click()
#                                                     time.sleep(2)
#
#                                             driver.execute_script("var q=document.documentElement.scrollTop=0")  # 回到顶部，否则会出现错误
#                                             time.sleep(2)
#
#                                             if len(chapter_lis1) > len(chapter_lis):
#                                                 driver.find_element(By.XPATH, '//*[@id="main-content"]/div[4]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/span[3]/span/div/span[2]').click()
#                                                 driver.execute_script( "var q=document.documentElement.scrollTop=0")  # 回到顶部，否则会出现错误
#                                                 time.sleep(2)
#
#
#                                             # # 从第一个开始，获得信息
#                                             MuLu_left = '//*[@id="main-content"]/div[4]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div['
#                                             MuLu_right = ']/span[3]/span/div/span[1]'
#                                             Content_left = '//*[@id="main-content"]/div[4]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div['
#                                             Content_right = ']/span[3]/span/div/span'
#                                             Spc_right = ']/span[3]/span/div/span[2]'
#                                             for count in range(1,1000):  # 没有那么多课程，所以1000就够用了，最后再break
#                                                 MuLu = MuLu_left + str(count) + MuLu_right
#                                                 Content = Content_left + str(count) + Content_right
#                                                 Spc = Content_left + str(count) + Spc_right
#                                                 if ret_chapter(Content) == 2:  # 2代表的是目录单元
#                                                     danyuan = driver.find_element(By.XPATH, MuLu).text
#                                                     danyuan1 = danyuan
#                                                 elif ret_chapter(Content) == 3:  # 3代表的是内容
#                                                     content = driver.find_element(By.XPATH, Content).text
#                                                 # button = driver.find_element(By.XPATH, Content)
#                                                 # button.click()
#                                                 #
#                                                 # time.sleep(5)
#                                                 # new_url = driver.current_url
#                                                 # print(new_url)
#                                                 # driver.back()
#                                                     lis = [xueduan, nianji, xueke, banben, ceci, danyuan, content]
#                                                     for i in lis:
#                                                         print(i, end=' ')
#                                                     print('END')
#                                                     with open('data1.csv', 'a', newline='', encoding='utf-8-sig') as file:
#                                                         writer = csv.writer(file)
#                                                         writer.writerow(lis)
#                                                 elif ret(Spc):
#                                                     danyuan = danyuan1 + str('---') + driver.find_element(By.XPATH, Spc).text
#
#                                                 else:
#                                                     break
#
#     if xd == 5:
#         ceci = ''
#         XueDuan = XueDuan_left + str(xd) + Xueduan_right  # xd是学段的缩写
#         try:
#             driver.find_element(By.XPATH, XueDuan).click()
#         except:
#             break  # 如果出错了，就代表这个栏里面没有那么多东西，所以就直接break掉就可以
#         else:
#             xueduan = driver.find_element(By.XPATH, XueDuan).text
#             time.sleep(2)
#             XueKe_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/label['
#
#             XueKe_right = ']/span[2]'
#             for xk in range(7, 21):
#                 XueKe = XueKe_left + str(xk) + XueKe_right
#                 try:
#                     driver.find_element(By.XPATH, XueKe).click()
#                 except:
#                     break
#                 else:
#                     xueke = driver.find_element(By.XPATH, XueKe).text
#                     time.sleep(2)
#                     BanBen_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/label['
#                     BanBen_right = ']/span[2]'
#                     for bb in range(2, 21):
#                         BanBen = BanBen_left + str(bb) + BanBen_right
#                         try:
#                             driver.find_element(By.XPATH, BanBen).click()
#                         except:
#                             break
#                         else:
#                             banben = driver.find_element(By.XPATH, BanBen).text
#                             time.sleep(2)
#                             CeCi_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[4]/div[2]/label['
#                             CeCi_right = ']/span[2]'
#                             for cc in range(2, 21):
#                                 Ceci = CeCi_left + str(cc) + CeCi_right
#                                 try:
#                                     driver.find_element(By.XPATH, Ceci).click()
#                                 except:
#                                     break
#                                 else:
#                                     ceci = driver.find_element(By.XPATH, Ceci).text
#                                     time.sleep(2)
#
#                                     chapter_lis = driver.find_elements(By.CLASS_NAME, 'chapter-name')
#                                     for i in range(1, len(chapter_lis)):
#                                         chapter_lis[i].click()
#                                         time.sleep(2)
#                                     driver.execute_script("var q=document.documentElement.scrollTop=0")  # 回到顶部，否则会出现错误
#                                     time.sleep(2)
#                                     chapter_lis1 = driver.find_elements(By.CLASS_NAME, 'chapter-name')
#                                     for i in range(1, len(chapter_lis1)):
#                                         if chapter_lis1[i] not in chapter_lis:
#                                             chapter_lis1[i].click()
#                                             time.sleep(2)
#                                     driver.execute_script("var q=document.documentElement.scrollTop=0")  # 回到顶部，否则会出现错误
#                                     time.sleep(2)
#                                     if len(chapter_lis1) > len(chapter_lis):
#                                         driver.find_element(By.XPATH,
#                                                             '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div[2]/span[3]/span/div/span[2]').click()
#                                         driver.execute_script(
#                                             "var q=document.documentElement.scrollTop=0")  # 回到顶部，否则会出现错误
#                                         time.sleep(2)
#
#                                     MuLu_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div['
#
#                                     MuLu_right = ']/span[3]/span/div/span[1]'
#                                     Content_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div['
#                                     Content_right = ']/span[3]/span/div/span'
#                                     Spc_right = ']/span[3]/span/div/span[2]'
#
#                                     for count in range(1,1000):
#                                         MuLu = MuLu_left + str(count) + MuLu_right
#                                         Content = Content_left + str(count) + Content_right
#                                         Spc = Content_left + str(count) + Spc_right
#                                         if ret_chapter(Content) == 2:
#                                             danyuan = driver.find_element(By.XPATH, MuLu).text
#                                             danyuan1 = danyuan
#                                         elif ret_chapter(Content) == 3:
#                                             content = driver.find_element(By.XPATH, Content).text
#                                             lis = [xueduan, nianji, xueke, banben, ceci, danyuan, content]
#                                             for i in lis:
#                                                 print(i, end=' ')
#                                             print('END')
#                                             with open('data1.csv', 'a', newline='', encoding='utf-8-sig') as file:
#                                                 writer = csv.writer(file)
#                                                 writer.writerow(lis)
#                                         elif ret(Spc):
#                                             danyuan = danyuan1 + str('---') + driver.find_element(By.XPATH, Spc).text
#                                         else:
#                                             break


headers = {
    "accept": '*/*',
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "origin": "https://basic.smartedu.cn",
    "referer": "https://basic.smartedu.cn/",
    "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}

def get_m3u8_file(m3u8_url, file_path):
    """
    下载m3u8文件
    :param m3u8_url: m3u8文件的URL
    :param file_path: 要下载的文件路径
    :return:
    """

    # eventlet.monkey_patch()
    # with eventlet.Timeout(2, False):
    try:
        resp = requests.get(m3u8_url, headers=headers, timeout=15)
    except:
        print('ERROR')
    else:
        if resp.status_code == 200:
            content = resp.text
            with open(file_path, "w") as f:
                f.write(content)

def get_ts_name_list(file_path):

    ts_name_list = []
    with open(file_path, "rb") as f:
        cont_list = f.readlines()
    for cont in cont_list:
        cont = cont.decode().strip()
        if cont.endswith(".ts"):
            ts_name_list.append(cont.split("/")[-1])
            # if not cont.startswith("#"):
            #     ts_name_list.append(cont.split("/")[-1])
    return ts_name_list

def get_ts_files(file_dir, ts_url_template, ts_name_list):
    """
    循环下载ts文件
    :param file_dir: 文件下载所在文件夹
    :param ts_url_template: ts文件请求URL模板
    :param ts_name_list: ts文件名称列表
    :return:
    """
    for ts_name in ts_name_list:
        ts_url = ts_url_template + ts_name
        resp = requests.get(ts_url, headers=headers)
        if resp.status_code == 200:
            with open(os.path.join(file_dir, ts_name), "wb") as f:
                f.write(resp.content)
            print("%s-->下载成功！" % ts_name)
        else:
            print("%s-->下载失败！" % ts_name)

def merge_ts_files(file_dir, file_name, ts_name_list):
    """
    将多个ts文件进行合并
    :param file_dir: ts文件所在文件夹
    :param file_name: 合并后的文件名称
    :param ts_name_list: ts文件名称列表
    :return:
    """
    file_out = os.path.join(file_dir, file_name)
    with open(file_out, 'wb') as f_out:
        for ts_name in ts_name_list:
            with open(os.path.join(file_dir, ts_name), "rb") as f_in:
                f_out.write(f_in.read())
    print("合并ts文件成功！")


def click():
    # ActionChains(driver1).key_down(Keys.Keys.F12).key_up(Keys.Keys.F12).perform()
    # ActionChains(driver).move_to_element_with_offset(s, 100, 20).context_click().perform()
    pg.PAUSE = 1

    pg.click(3472, 216)
    pg.press('shift')
    pg.press('m')
    pg.press('3')
    pg.press('u')
    pg.press('8')
    # pg.moveTo(1327, 504)
    pg.click(3100, 600, button='right')
    pg.moveTo(3206, 773)
    pg.click(3544, 760)
    ur = pp.paste()
    pg.click(3075, 256)
    return ur

# option1 = webdriver.ChromeOptions()  # 禁止网页自动关闭
# option1.add_experimental_option("detach", True)
# option1.add_argument("start-maximized")
# option1.add_argument("--auto-open-devtools-for-tabs")
# option1.add_experimental_option("excludeSwitches", ["enable-automation"])
# option1.add_experimental_option('useAutomationExtension', False)
# driver1 = webdriver.Chrome(options=option1)  # 创建webdriver实例
# url = 'https://basic.smartedu.cn/syncClassroom/classActivity?activityId=0aa162f1-1315-486f-b874-3314919d0cc7'
# url1 = 'https://basic.smartedu.cn/syncClassroom'
# driver1.get(url1)
# time.sleep(3)
#
# for xd in range(2,21):
#     if xd != 5:
#         XueDuan = XueDuan_left + str(xd) + Xueduan_right  # xd是学段的缩写
#         try:
#             driver1.find_element(By.XPATH, XueDuan).click()
#         except:
#             break  # 如果出错了，就代表这个栏里面没有那么多东西，所以就直接break掉就可以
#         else:
#             xueduan = driver1.find_element(By.XPATH, XueDuan).text
#             time.sleep(2)
#             NianJi_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/label['
#             NianJi_right = ']/span[2]'
#             for nj in range(2, 21):
#                 NianJi = NianJi_left + str(nj) + NianJi_right
#                 try:
#                     driver1.find_element(By.XPATH, NianJi).click()
#                 except:
#                     break
#                 else:
#                     nianji = driver1.find_element(By.XPATH, NianJi).text
#                     time.sleep(2)
#                     XueKe_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/label['
#                     XueKe_right = ']/span[2]'
#                     for xk in range(1, 21):
#                         XueKe = XueKe_left + str(xk) + XueKe_right
#                         try:
#                             driver1.find_element(By.XPATH, XueKe).click()
#                         except:
#                             break
#                         else:
#                             time.sleep(2)
#                             xueke = driver1.find_element(By.XPATH, XueKe).text
#                             BanBen_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[4]/div[' \
#                                           '2]/label[ '
#                             BanBen_right = ']/span[2]'
#                             for bb in range(1,21):
#                                 BanBen = BanBen_left + str(bb) + BanBen_right
#                                 try:
#                                     driver1.find_element(By.XPATH, BanBen).click()
#                                 except:
#                                     break
#                                 else:
#                                     time.sleep(2)
#                                     banben = driver1.find_element(By.XPATH, BanBen).text
#                                     CeCi_left = '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[1]/div/div[2]/div/div[' \
#                                                 '5]/div[2]/label[ '
#                                     CeCi_right = ']/span[2]'
#                                     for cc in range(1, 21):
#                                         Ceci = CeCi_left + str(cc) + CeCi_right
#                                         try:
#                                             driver1.find_element(By.XPATH, Ceci).click()
#                                         except:
#                                             break
#                                         else:
#                                             time.sleep(2)
#                                             ceci = driver1.find_element(By.XPATH, Ceci).text
#                                             chapter_lis = driver1.find_elements(By.CLASS_NAME, 'chapter-name')
#                                             for i in range(1, len(chapter_lis)):
#                                                 chapter_lis[i].click()
#                                                 time.sleep(2)
#                                             driver1.execute_script("var q=document.documentElement.scrollTop=0")  # 回到顶部，否则会出现错误
#                                             time.sleep(2)
#                                             con_lis = driver1.find_elements(By.CLASS_NAME, 'active-name')
#                                             driver2 = driver1
#                                             cou = 1
#                                             i_chapter = 0
#                                             count_m = 0
#                                             Len_con_lis = len(con_lis)
#                                             while count_m < Len_con_lis:
#                                                 try:
#                                                     time.sleep(1)
#                                                     con_lis[i_chapter].click()
#                                                     time.sleep(1)
#                                                 except:
#                                                     try:
#                                                         chapter_lis[cou].click()
#                                                         time.sleep(1)
#                                                     except:
#                                                         print('end')
#                                                     else:
#                                                         cou = cou + 1
#                                                         i_chapter = 0
#                                                         time.sleep(1)
#                                                         con_lis1 = driver1.find_elements(By.CLASS_NAME, 'active-name')
#                                                         length = len(con_lis)
#                                                         con_lis.clear()
#                                                         for j in range(length, len(con_lis1)):
#                                                             con_lis.append(con_lis1[j])
#                                                         time.sleep(1)
#
#                                                 else:
#                                                     conten = driver1.find_element(By.XPATH, '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]').text
#                                                     print(conten)
#                                                     driver1.find_element(By.XPATH,
#                                                                          '//*[@id="main-content"]/div[3]/div[4]/div[2]/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]').click()
#                                                     time.sleep(2)
#
#                                                     # 获得m3u8
#                                                     m3u8_url = ''
#                                                     m3u8_url = click()
#
#                                                     file_dir = './video/ts_f-' + str(conten)  # 用来保存ts文件
#                                                     if not os.path.exists(file_dir):
#                                                         os.mkdir(file_dir)
#                                                     # m3u8文件URL
#                                                     # m3u8_url = "https://r1-ndr.ykt.cbern.com.cn/edu_product/65/video/17b0594b547a11eb96b8fa20200c3759/158bfc80999d1a8a01c504fce1012e6b.1920.1080.false/158bfc80999d1a8a01c504fce1012e6b.1920.1080.m3u8"
#                                                     # 提取文件名
#                                                     # file_name = m3u8_url.split('/')[-1]
#                                                     file_name = str(conten)
#                                                     file_path = os.path.join(file_dir, file_name)
#                                                     # 下载m3u8文件
#                                                     print('m3u8_url is ', end='')
#                                                     print(m3u8_url)
#                                                     get_m3u8_file(m3u8_url, file_path)
#                                                     print('here3')
#                                                     # 获取文件中ts文件名称列表
#                                                     ts_name_list = get_ts_name_list(file_path)
#                                                     # ts文件URL模板
#                                                     m = []
#                                                     m = m3u8_url.split('/')
#                                                     print(m)
#                                                     ts_url_template = ''
#                                                     for i in range(len(m) - 1):
#                                                         ts_url_template = ts_url_template + m[i] + str('/')
#                                                     print(ts_url_template)
#                                                     # ts_url_template = "https://r1-ndr.ykt.cbern.com.cn/edu_product/65/video/17b0594b547a11eb96b8fa20200c3759/158bfc80999d1a8a01c504fce1012e6b.1920.1080.false/"
#                                                     # 下载ts文件
#                                                     try:
#                                                         get_ts_files(file_dir, ts_url_template, ts_name_list)
#                                                     except:
#                                                         print('Error' + str(conten))
#                                                     # 合并ts文件
#                                                     else:
#                                                         ts_file_name = file_name.split(".")[0] + ".ts"
#                                                         merge_ts_files(file_dir, ts_file_name, ts_name_list)
#
#
#                                                     count_m = count_m + 1
#                                                     i_chapter = i_chapter + 1
#                                                     print(i_chapter)
#                                                     driver1.back()
#                                                     time.sleep(2)
#                                                     driver1 = driver2
#                                                     chapter_lis = driver1.find_elements(By.CLASS_NAME, 'chapter-name')
#                                                     con_lis = driver1.find_elements(By.CLASS_NAME, 'active-name')


option1 = webdriver.ChromeOptions()  # 禁止网页自动关闭
option1.add_experimental_option("detach", True)
option1.add_argument("start-maximized")
option1.add_argument("--auto-open-devtools-for-tabs")
option1.add_experimental_option("excludeSwitches", ["enable-automation"])
option1.add_experimental_option('useAutomationExtension', False)
driver1 = webdriver.Chrome(options=option1)  # 创建webdriver实例
url = 'https://basic.smartedu.cn/qualityCourse?courseId=8ae7e49f-7c9c-cf01-017c-9dfe22f6021e'
driver1.get(url)
time.sleep(6)

