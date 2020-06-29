from flask import Flask, request, render_template
import requests
from pyquery import PyQuery as pq
import pymysql

app = Flask(__name__)

# database initialisation
dbHost = "localhost"
dbUser = "root"
dbPass = "Guardian123"
dbase = "test"
dbCharset = 'utf8'

gName = {}
gDiscount = {}
gdate = {}
gprice = {}


def create():
    db = pymysql.connect(host=dbHost,
                         user=dbUser,
                         passwd=dbPass,
                         db=dbase,
                         charset=dbCharset)

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


def insert(data):
    db = pymysql.connect(dbHost, dbUser, dbPass, dbase, charset=dbCharset)
    cursor = db.cursor()
    for i in data:
        game = i
        sql = "INSERT INTO STEAM_DISCOUNT(NAME,DISCOUNT,PUBLISH_DATE,ORIGINAL_PRICE) values(%s,%s,%s,%s)"
        cursor.execute(sql, game)  # 执行sql语句，movie即是指要插入数据库的数据
        db.commit()  # 插入完成后，不要忘记提交操作
        # print("success")
    cursor.close()
    db.close()


def show():
    db = db = pymysql.connect(dbHost, dbUser, dbPass, dbase, charset=dbCharset)
    cursor = db.cursor()
    sql = "select * from STEAM_DISCOUNT"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.commit()
    cursor.close()
    db.close()


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/form_login', methods=['POST', 'GET'])
def form_login():
    name = request.form['username']
    pwd = request.form['password']
    if name != 'root':
        return render_template('login.html', info='Invalid User')
    else:
        if pwd != 'Guardian123':
            return render_template('login.html', info='Invalid Password')
        else:
            return render_template('home.html', name='root')


@app.route("/")
def hello():
    return render_template(
        'index.html',
        # game 1 information
        gName1=gName[1],
        gDiscount1=gDiscount[1],
        gdate1=gdate[1],
        gprice1=gprice[1],
        gStore1="steam",

        # game 2 information
        gName2=gName[2],
        gDiscount2=gDiscount[2],
        gdate2=gdate[2],
        gprice2=gprice[2],
        gStore2="steam",

        # game 3 information
        gName3=gName[3],
        gDiscount3=gDiscount[3],
        gdate3=gdate[3],
        gprice3=gprice[3],
        gStore3="steam",

        # game 4 information
        gName4=gName[4],
        gDiscount4=gDiscount[4],
        gdate4=gdate[4],
        gprice4=gprice[4],
        gStore4="steam",

        # game 5 information
        gName5=gName[5],
        gDiscount5=gDiscount[5],
        gdate5=gdate[5],
        gprice5=gprice[5],
        gStore5="steam",

        # game 6 information
        gName6=gName[6],
        gDiscount6=gDiscount[6],
        gdate6=gdate[6],
        gprice6=gprice[6],
        gStore6="steam"
    )


if __name__ == "__main__":
    create()

    list_data = []
    url = 'https://store.steampowered.com/search/?filter=globaltopsellers'
    for i in range(1):
        newurl = url + str(i)
        print(newurl)
        html = requests.get(newurl).content.decode('utf-8')
        doc = pq(html)
        items = doc('#search_result_container a').items()
        cnt = 0
        for item in items:
            gName[cnt] = item.find('.title').text()
            gDiscount[cnt] = item.find('.search_discount.responsive_secondrow').text()
            gdate[cnt] = item.find('.search_released.responsive_secondrow').text()
            gprice[cnt] = item.find('.search_price.discounted.responsive_secondrow span').text()
            if gDiscount[cnt] == "" or gprice[cnt] == "":
                pass
            else:
                list_data.append([gName[cnt], gDiscount[cnt], gdate[cnt], gprice[cnt]])
                # print(gName[cnt], gDiscount[cnt], gdate[cnt], gprice[cnt])
            cnt = cnt + 1
    insert(list_data)
    app.run(debug=True)
