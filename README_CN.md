# 震荡突破策略

## 策略说明

上轨：过去30根K线的最高价

下轨：过去30根K线的最低价

区间幅度：（上轨 - 下轨）/ （上轨 + 下轨）

如果区间幅度小于阈值a，价格向上突破上轨，买入开仓，价格跌破下轨平仓

如果区间幅度小于阈值a，价格向下突破上轨，卖出开仓，价格突破上轨平仓  

![shock_CN](/Users/arthur/www/academy/shock-strategy/README_CN.assets/shock_CN.png)

**此外，KuCoin拥有level3级别的交易数据、极优的撮合引擎，以及对api用户提供特别的手续费折扣，极大程度的减少了你在策略实施时的劣势，同时提供sandbox环境作为数据测试支撑，帮助你规避风险**。

**请注意，该策略是在一个震荡区间内预测价格波动，并帮你在KuMEX开多或空以及价格波动后的平仓操作**。

**如果你想在实际环境中利用策略获得盈利，我们希望你能够在sandbox环境配合其他参数或是策略进行测试调整，以使你能够获得盈利**。  

**当然，如果这个过程中，你遇到任何问题需要帮助亦或是有好的想法想要分享，请在ISSUE中反映，我们会努力及时响应**。

## 如何使用

* 克隆该策略项目至本地后，安装依赖：

  ```shell script
  pip install python-kumex
  ```

* 复制config.json.example，并重命名为config.json，然后完善相关的配置信息

  ```
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
    "valve": "valve"
  }
  ```

  

* 让你的策略运行起来：

  ```shell
  ./shock.py
  ```

  