from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#创建数据库链接
engine=create_engine('sqlite:///stock_data.db?check_same_thread=False')

#建立实体类映射
Base = declarative_base()
#code,name,changepercent,trade,open,high,low,settlement,volume,turnoverratio,amount,per,pb,mktcap,nmc,date

# engine是2.2中创建的连接
Session = sessionmaker(bind=engine)

# 创建Session类实例
session = Session()
import csv

class stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer,primary_key=True)
    code = Column(Integer)
    name = Column(String(255))
    changepercent = Column(String(255))
    trade =  Column(String(255))
    open = Column(String(255))
    high = Column(String(255))
    low = Column(String(255))
    settlement = Column(String(255))
    volume = Column(String(255))
    turnoverratio = Column(String(255))
    amount = Column(String(255))
    per = Column(String(255))
    pb = Column(String(255))
    mktcap = Column(String(255))
    nmc = Column(String(255))
    date = Column(String(255))



def readData():
    with open('stock_data.csv','r',encoding='utf-8') as csvFile:
        data = csv.reader(csvFile)
        i = 0
        for row in data:
            if i != 0:
                insertData(row)
            i+=1

table_columName = "code,name,changepercent,trade,open,high,low,settlement,volume,turnoverratio,amount,per,pb,mktcap,nmc,date"

def generateTableColumn():
    columns = table_columName.split(",")
    return columns

listData = []
def insertData(row):
    code = row[0]
    name = row[1]
    changepercent = row[2]
    trade = row[3]
    open = row[4]
    high = row[5]
    low = row[6]
    settlement = row[7]
    volume = row[8]
    turnoverratio = row[9]
    amount = row[10]
    per = row[11]
    pb = row[12]
    mktcap = row[13]
    nmc = row[14]
    date = row[15]

    s = stock(code=code,name=name,changepercent=changepercent,
          trade=trade,open=open,high=high,low=low,settlement=settlement,
          volume=volume,turnoverratio=turnoverratio,amount=amount,per=per,pb=pb,mktcap=mktcap,nmc=nmc,date=date
          )
    listData.append(s)
    if len(listData) >= 100:
        session.add_all(listData)
        listData.clear()
        session.commit()

def create_table():
    Base.metadata.create_all(engine, checkfirst=True)

def search():
    stocks = session.query(stock).filter_by(name='中芯国际')


def searchByName(name):
    stocks = session.query(stock).filter_by(name=name)
    strs = 'The information I found out about this stock is'
    for item in stocks:
      return  strs + ':' + 'code: '+ str(item.code) + '   price:' + item.amount + '  name:' + item.name

def searchByNameReturnVolum(name):
    stocks = session.query(stock).filter_by(name=name)
    strs = 'The information I found out about this stock is'
    for item in stocks:
        return strs + 'volume: ' + item.volume

def searchByNameReturnMarket(name):
    stocks = session.query(stock).filter_by(name=name)
    rs = 'The information I found out about this stock is'
    for item in stocks:
        return rs + 'market price: ' + item.settlement

