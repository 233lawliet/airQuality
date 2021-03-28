import datetime
import time

class ResponseCity:
    # 解析数据
    def __init__(self, responseData):

        # 时间
        self.curtime = ""  # 当前时间
        self.time = ""  # 采集时间

        # self.idx = ""  # 唯一表示（没用到）
        self.scoreAQI = -1  # 评分
        self.mainPollution = ""  # 主要污染物

        # 详细空气质量
        self.pm25 = -1
        self.pm10 = -1
        self.o3 = -1
        self.no2 = -1
        self.so2 = -1
        self.co = -1
        self.temperature = -1  # 温度
        self.dew = -1  # 露点温度
        self.press = -1  # 大气压
        self.humidity = -1  # 空气湿度
        self.wind = -1  # 风力

        # 预测指标
        self.forecast_o3 = ""
        self.forecast_pm10 = ""
        self.forecast_pm25 = ""
        self.forecast_uvi = ""

        self.ParsingAllData(responseData)

    def ParsingAllData(self, responseData):
        # self.idx = responseData["idx"]
        try:
            self.scoreAQI = float(responseData["aqi"])
        except:
            self.pm25 = -1
        self.mainPollution = responseData["dominentpol"]

        # 解析详细空气质量
        self.ParsingAQI(responseData)

        # 解析时间
        self.ParsingTime(responseData)

        # 解析预测结果
        # self.ParsingPrediction(responseData)

    def ParsingAQI(self, responseData):
        for parameter in responseData["iaqi"]:
            if parameter == "pm25":
                try:
                    self.pm25 = float(responseData["iaqi"]["pm25"]["v"])
                except:
                    self.pm25 = -10000
            elif parameter == "pm10":
                try:
                    self.pm10 = float(responseData["iaqi"]["pm10"]["v"])
                except:
                    self.pm10 = -10000
            elif parameter == "o3":
                try:
                    self.o3 = float(responseData["iaqi"]["o3"]["v"])
                except:
                    self.o3 = -10000
            elif parameter == "no2":
                try:
                    self.no2 = float(responseData["iaqi"]["no2"]["v"])
                except:
                    self.no2 = -10000
            elif parameter == "so2":
                try:
                    self.so2 = float(responseData["iaqi"]["so2"]["v"])
                except:
                    self.so2 = -10000
            elif parameter == "co":
                try:
                    self.co = float(responseData["iaqi"]["co"]["v"])
                except:
                    self.co = -10000

            elif parameter == "t":
                try:
                    self.temperature = float(responseData["iaqi"]["t"]["v"])
                except:
                    self.temperature = -10000
            elif parameter == "dew":
                try:
                    self.dew = float(responseData["iaqi"]["dew"]["v"])
                except:
                    self.dew = -10000
            elif parameter == "p":
                try:
                    self.press = float(responseData["iaqi"]["p"]["v"])
                except:
                    self.press = -10000
            elif parameter == "h":
                try:
                    self.humidity = float(responseData["iaqi"]["h"]["v"])
                except:
                    self.humidity = -10000
            elif parameter == "w":
                try:
                    self.wind = float(responseData["iaqi"]["w"]["v"])
                except:
                    self.wind = -10000
            else:
                pass

    def ParsingTime(self, responseData):
        # 提取时间

        try:
            self.time = datetime.datetime.strptime(responseData["time"]["s"], "%Y-%m-%d %H:%M:%S")
        except Exception as err:
            print(err)
            self.time = datetime.datetime.now()
        
        try:
            self.curtime = str(datetime.datetime.now())
        except Exception as err:
            print(err)
            self.curtime = datetime.datetime.now()

    def ParsingPrediction(self, responseData):
        for parameter in responseData["forecast"]["daily"]:
            if parameter == "o3":
                self.forecast_o3 = responseData["forecast"]["daily"]["o3"]
            elif parameter == "pm10":
                self.forecast_pm10 = responseData["forecast"]["daily"]["pm10"]
            elif parameter == "pm25":
                self.forecast_pm25 = responseData["forecast"]["daily"]["pm25"]
            elif parameter == "uvi":
                self.forecast_uvi = responseData["forecast"]["daily"]["uvi"]
            else:
                pass

