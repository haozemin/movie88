import pymysql
import requests
import re


# 获取资源并下载
def resp(listURL):
    # 连接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='123456',  # 数据库密码请根据自身实际密码输入
        database='movie88',
        charset='utf8'
    )

    # 创建数据库游标
    cursor = conn.cursor()

    # 创建列表t_movieTOP250（执行sql语句）
    cursor.execute('create table t_movie89(id INT PRIMARY KEY auto_increment NOT NULL ,movieName VARCHAR(20) NOT NULL ,pictrue_address VARCHAR(100))')

    try:
        # 爬取数据
        for urlPath in listURL:
            # 获取网页源代码
            response = requests.get(urlPath)
            html = response.text

            # 正则表达式
            namePat = r'alt="(.*?)" src='
            imgPat = r'src="(.*?)" class='

            # 匹配正则（排名【用数据库中id代替，自动生成及排序】、电影名、电影海报（图片地址））
            res2 = re.compile(namePat)
            res3 = re.compile(imgPat)
            textList2 = res2.findall(html)
            textList3 = res3.findall(html)

            # 遍历列表中元素,并将数据存入数据库
            for i in range(len(textList3)):
                cursor.execute('insert into t_movieTOP250(movieName,pictrue_address)VALUES("%s","%s")' % (textList2[i], textList3[i]))

        # 从游标中获取结果
        cursor.fetchall()

        # 提交结果
        conn.commit()
        print("结果已提交")

    except Exception as e:
        # 数据回滚
        conn.rollback()
        print("数据已回滚")

    # 关闭数据库
    conn.close()


# top250所有网页网址
def page(url):
    urlList = []
    for i in range(10):
        num = str(25 * i)
        pagePat = r'?start=' + num + '&filter='
        urL = url + pagePat
        urlList.append(urL)
    return urlList


if __name__ == '__main__':
    url = r"https://movie.douban.com/top250"
    listURL = page(url)
    resp(listURL)
