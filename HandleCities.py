import csv
import configparser

from City import City

def removeSameCities(fileName):
    """
    加载cities文件数据，消除重复数据
    :param fileName:
    :return:
    """
    with open(fileName, "r", encoding="GBK") as file:
        reader = csv.reader(file)

        # 去重
        citiesIdSet = set()
        citiesList = list()  # 已去重

        readerCities = list(reader)[1:]
        for city in readerCities:
            cityId = city[0]
            if cityId not in citiesIdSet:
                citiesList.append(City(city[0], city[1], city[2], city[3]))
                citiesIdSet.add(cityId)

        return citiesList

def addUrl(targetUrl, token, cities):
    """
    组装URL
    :param targetUrl:
    :param token:
    :param cities:
    :return:
    """
    for city in cities:
        city.addUrl(targetUrl, token)

def writeCities(fileName,cities):
    """
    将城市数据写入outCities
    :param fileName:
    :param cities:
    :return:
    """
    with open(fileName, "w", encoding="utf8") as file:
        writer = csv.writer(file, delimiter=',')
        for city in cities:
            writer.writerow(city.__dict__.values())


def loadCities(fileName):
    with open(fileName, "r", encoding="utf8") as file:
        reader = csv.reader(file)
        readerCities = list(reader)[:]

        citiesList = list()
        for city in readerCities:
            citiesList.append(City(city[0], city[1], city[2], city[3],city[4]))
        return citiesList


if __name__ == '__main__':
    # 加载配置
    config = configparser.ConfigParser()
    config.read("../config.ini")

    # 获取城市数据
    inputCitiesFileName = config.get("Cities", "inputCitiesFile")
    cities = loadCities(inputCitiesFileName)

    # 组装Url
    targetUrl = config.get("Spider", "targetUrl")
    token = config.get("Spider", "token")
    addUrl(targetUrl, token, cities)

    # 写出城市数据
    outputCitiesFileName = config.get("Cities", "outputCitiesFile")
    writeCities(outputCitiesFileName, cities)

    print("数据写完了")






