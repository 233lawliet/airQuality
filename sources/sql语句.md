

### 创建插入语句

#### 插入格式

```

地区编号 adcode
地区名字 adname char
经度 lng double
维度 lat double

当前时间 curtime timestamp
测试时间 time

空气质量评分 scoreAQI 
主要污染物名称 mainPollution
对应污染物
	pm25
	pm10
	o3
	no2
	so2
	co
空气温度 temperature
露点湿度 dew
大气压 press
空气湿度 humidity
风力 wind

o3预测 forecast_o3
pm10预测 forecast_pm10
pm2.5预测 forecast_pm25
uvi预测 forecast_uvi
```

#### 创建表格

- 超级表

    ```
    CREATE TABLE IF NOT EXISTS airquality (curtime timestamp, time timestamp,scoreAQI float, mainPollution nchar(20),pm25 float, pm10 float,o3 float, no2 float, so2 float, co float, temperature float, dew float, press float, humidity float, wind float, forecast_o3 nchar(50), forecast_pm10 nchar(50), forecast_pm25 nchar(50), forecast_uvi nchar(50)) TAGS (adcode int, adname nchar(50), lng float, lat float, url BINARY(150));
    ```

- 建立普通表

    ```
    CREATE TABLE IF NOT EXISTs tableName USING superTable TAGS (adcode, adname, lng, lat, url);
    
    例如：
    CREATE TABLE IF NOT EXISTS t100003 USING airquality TAGS (100000, "中华人民共和国", 116.3683244, 39.915085, "
    https://api.waqi.info/feed/geo:39.915085;116.3683244/?token=6d1f880100cfeae0325a80fa87cf70465d36e77d
    ");
    ```

- 数据插入

    ```
    INSERT INTO t+adcode VALUES (curtime, time, scoreAQI, mainPollution, ...);
    
    例如：
    INSERT INTO t100000 VALUES (, time, scoreAQI, mainPollution, ...);
    ```

    