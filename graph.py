import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import psutil
import collections
import json 
import requests

keyBTC = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
keyETH = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"

def my_function(i):

    dataBTC = requests.get(keyBTC)  
    dataETH = requests.get(keyETH) 

    dataBTC = dataBTC.json()
    btc.popleft()
    btc.append(float(dataBTC['price']))

    dataETH = dataETH.json()
    eth.popleft()
    eth.append(float(dataETH['price']))
    
    ax.cla()
    ax1.cla()
    ax.set_ylim(float(dataBTC['price'])-50,float(dataBTC['price'])+50)
    ax1.set_ylim(float(dataETH['price'])-10,float(dataETH['price'])+10)

    ax.plot(btc, c='#EC5E29')
    ax.scatter(len(btc)-1, btc[-1], c='#EC5E29')
    ax.text(len(btc)-1, btc[-1]+2, "{}".format(btc[-1]))

    ax.set_xticks(np.arange(-1,100,2))
    #ax.set_xticklabels(np.arange(10,-1,-2))
    ax.set_xlabel('Seconds')
    ax.set_title('BTC\n')


    # remove spines
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # grid
    ax.set_axisbelow(True)
    ax.yaxis.grid(linestyle='dashed', alpha=0.8)

    ax1.plot(eth, c='#1787AD')
    ax1.scatter(len(eth)-1, eth[-1], c='#1787AD')
    ax1.text(len(eth)-1, eth[-1]+2, "{}".format(eth[-1]))

    ax1.set_xticks(np.arange(-1,100,2))
    #ax1.set_xticklabels(np.arange(10,-1,-2))
    ax1.set_xlabel('Seconds')
    ax1.set_title('ETH\n')

    # remove spines
    ax1.spines['left'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['top'].set_visible(False)

    # grid
    ax1.set_axisbelow(True)
    ax1.yaxis.grid(linestyle='dashed', alpha=1)

btc = collections.deque(np.zeros(100))
eth = collections.deque(np.zeros(100))

fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')

ax = plt.subplot(121)
ax1 = plt.subplot(122)

ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')



animation = FuncAnimation(plt.gcf(), my_function, interval=60000)

plt.show()