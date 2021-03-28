import csv
import json
import configparser
import taos
from apscheduler.schedulers.blocking import BlockingScheduler
import requests

from ResponseCity import ResponseCity
from HandleCities import loadCities




def spiderAndStore(cities, config):

    # 连接taos数据库
    host = config.get("Server", "host")
    user = config.get("Server", "user")
    password = config.get("Server", "password")
    configFile = config.get("Server", "config")

    conn = taos.connect(host=host)
    cursor = conn.cursor()
    
    # 使用数据库
    database = config.get("Server","database")
    cursor.execute("use "+database );

    for index in range(0, len(cities)):
        # 每个城市信息
        city = cities[index]
        # 爬取空气质量信息
        response = requests.get(city.url)
        
        requests.adapters.DEFAULT_RETRIES = 50  
        session = requests.session() 
        session.keep_alive = False # 短连接
        
        message = json.loads(response.text)
        responseCity = None
        if message["status"] == "ok":
            responseCity = ResponseCity(message["data"])
        # 将爬取数据放入数据库
        try:
            sql = "INSERT INTO t" + str(city.id) + " VALUES ('" + str(responseCity.curtime) + "', '" + str(responseCity.time) + "', " + str(responseCity.scoreAQI) + ", '" + responseCity.mainPollution + "', " + str(responseCity.pm25) + ", " + str(responseCity.pm10) + ", " + str(responseCity.o3) + ", " + str(responseCity.no2) + ", " + str(responseCity.so2) + ", " + str(responseCity.co) + ", " + str(responseCity.temperature) + ", "  + str(responseCity.dew) + ", " + str(responseCity.press) + ", " + str(responseCity.humidity) + ", "  + str(responseCity.wind) + ", '" + responseCity.forecast_o3 + "', '" + responseCity.forecast_pm10 + "', '" + responseCity.forecast_pm25 + "', '" + responseCity.forecast_uvi + "')"
            cursor.execute(sql)
        except Exception as err:
            print(err)
            print("表: "+str(city.id)+"插入数据失败")
            print("插入语句: "+sql)
    cursor.close()
    conn.close()

if __name__ == '__main__':
    # 加载配置
    config = configparser.ConfigParser()
    config.read("config.ini")

    # 获取城市数据
    outputCitiesFileName = config.get("Cities", "outputCitiesFile2")
    cities = loadCities(outputCitiesFileName)

    # 时间调度+爬取
    timeInterval = int(config.get("Spider", "timeInterval"))  # 加载爬取周期
    schedule = BlockingScheduler()
    schedule.add_job(spiderAndStore, "interval", max_instances=10, seconds=timeInterval, kwargs={"cities": cities, "config": config})
    schedule.start()


