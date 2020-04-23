# 震荡突破策略

## 策略说明

上轨：过去30根K线的最高价

下轨：过去30根K线的最低价

区间幅度：（上轨 - 下轨）/ （上轨 + 下轨）

如果区间幅度小于阈值a，价格向上突破上轨，买入开仓，价格跌破下轨平仓

如果区间幅度小于阈值a，价格向下突破上轨，卖出开仓，价格突破上轨平仓

**请注意，该策略是在一个震荡区间内帮你在kumex挂出多或空单，请不要在实际环境直接使用，否则，你必然会亏钱！**

## 如何使用

* 克隆该策略项目至本地后，安装依赖：
  ```shell script
  pip install python-kumex
  ```

* 复制config.json.example，并重命名为config.json，然后完善相关的配置信息

  ```json
  {  
    "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
  	// 是否是沙盒环境  
    "is_sandbox": true,
    // 合约名称，比如：XBTUSDTM 
    "symbol": "contract name",
    // 杠杆倍数，比如：5
    "leverage": "Leverage of the order",
    // 开仓数量，比如：1
    "size": "Order size. Must be a positive number",
    // K线图基准，单位是分钟，比如：60，代表60min，即1h为基准的K线图
    "resolution": "kline resolution,count by minute,such as 60,it means 60min(1h) kline",
    // 阈值
    "valve": "valve",
  }
  ```

  

* 让你的策略运行起来：

  ```shell
  ./shock.py
  ```

  