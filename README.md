# Shock_strategy

## Strategy description 

Up line: the highest price of the past 30 Klines  

Down line: the lowest price of the past 30 Klines  

Range = (UP - DOWN) / (UP + DOWN)

If range < a(threshold) & price breaks up the UP line, open long position, if price falls below the DOWN line, close position.  

If range < a(threshold) & price falls below the UP line, open short position, if  price breaks up the UP line, close position.  

![shock](shock.png)

**The above picture is the simulation operation of the shock strategy, where the blue part represents shorting, the red represents longing, and the width of the area represents the holding time. For each region's income, positive numbers indicate profitability and negative numbers indicate loss**.

**  **Moreover, KuCoin provides the transaction data of level 3, great matching engine, and the commission discount specially offers to the API customers, which could greatly reduce the disadvantages of the trading operations. At the same time, we offer the sandbox environment as the data testing support to avoid the risks.**  

**Notice: The strategy is to predict price fluctuations within a shock range and help you place long or short orders on KuMEX and close positions after price fluctuations, only a simple and incomplete trading strategy is provided here, please do not use it directly in the actual environment, otherwise, you will inevitably lose money!**  

**If you want to use the strategy in the actual environment to earn stable profits, we hope that you can make test adjustments in the sandbox environment with other parameters or strategies to enable you to achieve your goals. We also look forward to sharing your test data and Insights.**    

**Surely, if you encounter any problems in this process, or you have a profitable strategy to share, please reflect in ISSUE, we will try to respond in a timely manner.**  

**If you are interested in this strategy, please click the star in the upper right corner, we will  measure the popularity of this strategy and subsequent optimization priorities based on the amounts of stars. You can also click watching in the upper right corner to continue to follow this project by receiving update notifications**.  

## How to use

* After clone this project to your local, install the dependency: 

  ```shell script
  pip install python-kumex
  ```

* Paste config.json.example,  rename as config.json, then add the relevant configuration information: 

  ```
  {  
    "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
    // if sandbox
    "is_sandbox": true,
    // contract name, e.g.:XBTUSDTM 
    "symbol": "contract name",
    // leverage, e.g.:5
    "leverage": "Leverage of the order",
    // order size, e.g.:1
    "size": "Order size. Must be a positive number",
    // time frame of Kline, mesure time by minute, e.g.:60(60min)
    "resolution": "kline resolution,count by minute,such as 60,it means 60min(1h) kline",
    // threshold
    "valve": "valve"
  }
  ```

  

* Run your strategy:

  ```shell
  ./shock.py
  ```

  