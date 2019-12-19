#!/usr/bin/env python3
# encoding=utf-8
#by Eddy
import json,codecs,os,traceback,time

date = time.strftime('%Y%m%d',time.localtime(time.time())) #获取系统时间，格式年月日
prepath = "/mnt/ftp/pingan/"  #文件路径
postpath = os.path.join(prepath, date) #目标路径
files = os.listdir(postpath) #列出目标目录下的所有文件为列表
dest_file = open(file=r"/mnt/datdata/epms_price_parity_result.dat", mode="wb") ##以二进制打开写入文件，每运行一次都会覆盖写，节省磁盘空间

for file in files:
    jsonData = codecs.open(os.path.join(postpath, file), 'r', encoding='utf-8')

    for line in jsonData:
        try:
            dic = json.loads(line)
            # if flag:
                # 获取属性列表
            values = list(dic.values())
            i=0
            for word in values:
                dest_file.write(word.replace("\r\n","").replace("\n","").encode('utf-8'))

                dest_file.write("\u001b".encode('utf-8'))
                if i==len(values)-1:
                    if file.__contains__("benlai.json"):
                        dest_file.write("050000".encode('utf-8'))
                    if file.__contains__("colipu.json"):
                        dest_file.write("080000".encode('utf-8'))
                    if file.__contains__("deli.json"):
                        dest_file.write("090000".encode('utf-8'))
                    if file.__contains__("gome.json"):
                        dest_file.write("070000".encode('utf-8'))
                    if file.__contains__("jd.json"):
                        dest_file.write("010000".encode('utf-8'))
                    if file.__contains__("staples.json"):
                        dest_file.write("060000".encode('utf-8'))
                    if file.__contains__("sundan.json"):
                        dest_file.write("040000".encode('utf-8'))
                    if file.__contains__("suning.json"):
                            dest_file.write("030000".encode('utf-8'))
                    if file.__contains__("womai.json"):
                        dest_file.write("020000".encode('utf-8'))
                    dest_file.write("\n".encode('utf-8'))
                i+=1
                # print(keys)
                # writer.writerow(keys)  # 将属性列表写入文件中
                # flag = False
            # else:
        # 读取json数据的每一行，将values数据一次一行的写入文件中
        # writer.writerow(list(dic.values()))
        except:
            traceback.print_exc()
            # print(line)
    jsonData.close()
dest_file.close()
