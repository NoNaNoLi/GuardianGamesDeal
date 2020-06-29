import pymysql
import requests
from flask import Flask, request, render_template
from pyquery import PyQuery as pq

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
        gFree1=bool(gprice[1] == ''),

        # game 2 information
        gName2=gName[2],
        gDiscount2=gDiscount[2],
        gdate2=gdate[2],
        gprice2=gprice[2],
        gStore2="steam",
        gFree2=bool(gprice[2] == ''),

        # game 3 information
        gName3=gName[3],
        gDiscount3=gDiscount[3],
        gdate3=gdate[3],
        gprice3=gprice[3],
        gStore3="steam",
        gFree3=bool(gprice[3] == ''),

        # game 4 information
        gName4=gName[4],
        gDiscount4=gDiscount[4],
        gdate4=gdate[4],
        gprice4=gprice[4],
        gStore4="steam",
        gFree4=bool(gprice[4] == ''),

        # game 5 information
        gName5=gName[5],
        gDiscount5=gDiscount[5],
        gdate5=gdate[5],
        gprice5=gprice[5],
        gStore5="steam",
        gFree5=bool(gprice[5] == ''),

        # game 6 information
        gName6=gName[6],
        gDiscount6=gDiscount[6],
        gdate6=gdate[6],
        gprice6=gprice[6],
        gStore6="steam",
        gFree6=bool(gprice[6] == ''),

        # game 7 information
        gName7=gName[7],
        gDiscount7=gDiscount[7],
        gdate7=gdate[7],
        gprice7=gprice[7],
        gStore7="steam",
        gFree7=bool(gprice[7] == ''),

        # game 8 information
        gName8=gName[8],
        gDiscount8=gDiscount[8],
        gdate8=gdate[8],
        gprice8=gprice[8],
        gStore8="steam",
        gFree8=bool(gprice[8] == ''),

        # game 9 information
        gName9=gName[9],
        gDiscount9=gDiscount[9],
        gdate9=gdate[9],
        gprice9=gprice[9],
        gStore9="steam",
        gFree9=bool(gprice[9] == ''),

        # game 10 information
        gName10=gName[10],
        gDiscount10=gDiscount[10],
        gdate10=gdate[10],
        gprice10=gprice[10],
        gStore10="steam",
        gFree10=bool(gprice[10] == ''),

        # game 11 information
        gName11=gName[11],
        gDiscount11=gDiscount[11],
        gdate11=gdate[11],
        gprice11=gprice[11],
        gStore11="steam",
        gFree11=bool(gprice[11] == ''),

        # game 12 information
        gName12=gName[12],
        gDiscount12=gDiscount[12],
        gdate12=gdate[12],
        gprice12=gprice[12],
        gStore12="steam",
        gFree12=bool(gprice[12] == ''),

        # game 13 information
        gName13=gName[13],
        gDiscount13=gDiscount[13],
        gdate13=gdate[13],
        gprice13=gprice[13],
        gStore13="steam",
        gFree13=bool(gprice[13] == ''),

        # game 14 information
        gName14=gName[14],
        gDiscount14=gDiscount[14],
        gdate14=gdate[14],
        gprice14=gprice[14],
        gStore14="steam",
        gFree14=bool(gprice[14] == ''),

        # game 15 information
        gName15=gName[15],
        gDiscount15=gDiscount[15],
        gdate15=gdate[15],
        gprice15=gprice[15],
        gStore15="steam",
        gFree15=bool(gprice[15] == ''),

        # game 16 information
        gName16=gName[16],
        gDiscount16=gDiscount[16],
        gdate16=gdate[16],
        gprice16=gprice[16],
        gStore16="steam",
        gFree16=bool(gprice[16] == '')
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
