import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data = pd.read_csv('mm_master_demos.csv')
analyzed_map = 'de_mirage' 

data = data[(data.map_ == analyzed_map) & ((data.round_type == 'PISTOL_ROUND'))]

def pointx_to_resolutionx(xinput,startX=-3217,endX=1912,resX=1024):
    sizeX=endX-startX
    if startX < 0:
        xinput += startX *(-1.0)
    else:
        xinput += startX
    xoutput = float((xinput / abs(sizeX)) * resX);
    return xoutput

def pointy_to_resolutiony(yinput,startY=-3401,endY=1682,resY=1024):
    sizeY=endY-startY
    if startY < 0:
        yinput += startY *(-1.0)
    else:
        yinput += startY
    youtput = float((yinput / abs(sizeY)) * resY);
    return resY-youtput

data['attacker_mapX'] = data['att_pos_x'].apply(pointx_to_resolutionx)
data['attacker_mapY'] = data['att_pos_y'].apply(pointy_to_resolutiony)

ct_data = data[(data.is_bomb_planted == False) & (data.att_side == 'CounterTerrorist') & (data.winner_side == 'CounterTerrorist')]

im = plt.imread('de_mirage.png')
plt.figure(figsize=(20,20))
plt.imshow(im)
plt.scatter(ct_data['attacker_mapX'], ct_data['attacker_mapY'],alpha=0.005,c='blue')

plt.show()