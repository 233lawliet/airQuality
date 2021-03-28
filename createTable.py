
import configparser
import taos
from HandleCities import loadCities
import time



def createCitiesTable(cities, config):
    
   # 预先创建testdb

    # 连接taos数据库
    host = config.get("Server", "host")
    port = int(config.get("Server", "port"))
    user = config.get("Server", "user")
    password = config.get("Server","password")
    configFile = config.get("Server", "config")
    conn = taos.connect(host=host,config=configFile)

    # 连接数据库
    cursor = conn.cursor()
    database = config.get("Server", "database")
    cursor.execute("use " + database);

    # 创建超级表
    superTable = config.get("Server", "superTable")
    try:
        sql = "CREATE TABLE IF NOT EXISTS "+ superTable  +" (curtime timestamp, time timestamp,scoreAQI float, mainPollution nchar(20),pm25 float, pm10 float,o3 float, no2 float, so2 float, co float, temperature float, dew float, press float, humidity float, wind float, forecast_o3 nchar(50), forecast_pm10 nchar(50), forecast_pm25 nchar(50), forecast_uvi nchar(50)) TAGS (adcode int, adname nchar(50), lng float, lat float, url BINARY(150))"
        cursor.execute(sql)
        print("创建超级表: " + superTable + "成功了")
    except Exception as err:
        print("创建超级表:" + superTable + "失败了")
        print(err)

    # 创建子表
    sql = "CREATE TABLE IF NOT EXISTS 't100000' USING '"+superTable+"' TAGS (100000, '中华人民共和国', 116.368324,39.915085 , 'https://api.waqi.info/feed/geo:39.915085;116.3683244/?token=6d1f880100cfeae0325a80fa87cf70465d36e77d')"
    try:
        cursor.execute(sql)
        print("执行了测试的创建语句")
    except:
        print("测试创建")

    for city in cities:
        tableName = "t"+str(city.id)
        sql = "CREATE TABLE IF NOT EXISTS '"+tableName+"' USING '"+superTable+"' TAGS ("+ str(city.id) +", '"+city.name+"', "+ str(city.longitude) +", "+ str(city.latitude)  +", '"+str(city.url)+"')"
        
        try:
            cursor.execute(sql)
        except Exception as err:
            print("创建子表: "+tableName+"失败了")
            print(err)
            print("创建语句: "+sql)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # 加载配置
    config = configparser.ConfigParser()
    config.read("config.ini")

    # 获取城市数据
    outputCitiesFileName = config.get("Cities", "outputCitiesFile2")
    cities = loadCities(outputCitiesFileName)

    # 创建每个数据的表
    createCitiesTable(cities, config)

