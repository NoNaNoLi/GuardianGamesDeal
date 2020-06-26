import requests
from pyquery import PyQuery as pq
import pymysql
# 创建表
def create():
    db = pymysql.connect(host = "127.0.0.1",
                         user = "root",
                         passwd = "233233",
                         db = "test",
                         charset='utf8')

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS STEAM_DISCOUNT")

    sql = """CREATE TABLE STEAM_DISCOUNT(
            ID INT PRIMARY KEY AUTO_INCREMENT,
            NAME CHAR(100),
            DISCOUNT CHAR(100),
            PUBLISH_DATE CHAR(100),
            ORIGINAL_PRICE CHAR(100))"""

    cursor.execute(sql)
    db.close()
#输入信息
def insert(data):
    db = pymysql.connect("localhost","root","233233","test",charset='utf8')
    cursor = db.cursor()
    for i in data:
        game = i
        sql = "INSERT INTO STEAM_DISCOUNT(NAME,DISCOUNT,PUBLISH_DATE,ORIGINAL_PRICE) values(%s,%s,%s,%s)"
        cursor.execute(sql,game)  # 执行sql语句，movie即是指要插入数据库的数据
        db.commit()  # 插入完成后，不要忘记提交操作
        print('sucess')
    cursor.close()
    db.close()

#爬虫
def get_discounted_game_info(page,list_data):
    url = 'https://store.steampowered.com/search/?filter=globaltopsellers'
    for i in range(page):
        newurl = url+str(i)
        print(newurl)
        html = requests.get(newurl).content.decode('utf-8')
        doc = pq(html)
        items = doc('#search_result_container a').items()
        for item in items:
            title =  item.find('.title').text()
            discount = item.find('.search_discount.responsive_secondrow').text()
            publish_date = item.find('.search_released.responsive_secondrow').text()
            original_price = item.find('.search_price.discounted.responsive_secondrow span').text()
            list_data.append([title, discount, publish_date, original_price])
    insert(list_data)
#main
if __name__=='__main__':
    create()
    get_discounted_game_info(5,list_data = [])#页数可以自定义