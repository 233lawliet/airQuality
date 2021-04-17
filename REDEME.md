

#### 编程环境

```
python3、Tdengine
```

#### 依赖的包

```
1. configparser
2. taos
3. requests
4. apscheduler
```



### 操作流程

1. 第一次使用：手动建立air数据库

    ```
    手动连接taos数据库
    
    create database air;
    ```

2. 第一次使用：脚本创建superTable +3000子表

    ```
    python3 createTable.py
    ```

    - 注：表命名规范

        ```
        superTable： airquality
        
        子表：t+每个编号
        		例如朝阳区采集器的表名： 't110105'
        ```

3. 执行爬取任务

    ```
    sh spider.sh
    ```






### 结束爬取

```
# 执行爬取任务：sh spider.sh

# 查看爬取进行：ps -aux | grep spider

# 结束爬取任务：kill -9 xxxx
```





### 配置文件

- 服务器配置

    ```
    [Server]
    host = 127.0.0.1
    port = 6030
    user = root
    password = 
    ```

- 爬取配置  （主要的是爬取间隔）

    ```
    [Spider]
    targetUrl=https://api.waqi.info/feed/
    token=6d1f880100cfeae0325a80fa87cf70465d36e77d
    timeInterval=3600
    ```

    

