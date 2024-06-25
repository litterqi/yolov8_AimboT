（原数据集过于庞大，无法上传至GitHub，因此只选取了一小部分数据）

以荒漠迷城地图为例，分别描绘了ct_任意武器，ct_awp,t_A点下包,t_B点下包的位置分布图。

ct_awp：
```python
analyzed_map = 'de_mirage'
data = data[(data.map_ == analyzed_map) & ((data.round_type == 'PISTOL_ROUND') | (data.round_type == 'NORMAL'))]
```
选择地图名为'de_mirage'，筛选出回合类型为'PISTOL_ROUND'或 'NORMAL'的数据。

```python
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
```
将游戏中的x,y坐标值映射到指定分辨率(1024)下的x,y坐标值。

```python
data['attacker_mapX'] = data['att_pos_x'].apply(pointx_to_resolutionx)
data['attacker_mapY'] = data['att_pos_y'].apply(pointy_to_resolutiony)
```
将att_pos_x和att_pos_y列中的游戏坐标转换为地图图像上的分辨率坐标，结果存储在新列attacker_mapX和attacker_mapY中。

```python
ct_data_awp = data[(data.is_bomb_planted == False) & (data.att_side == 'CounterTerrorist') & (data.wp == 'AWP') & (data.winner_side == 'CounterTerrorist')]

im = plt.imread('de_mirage.png')
plt.figure(figsize=(20,20))
plt.imshow(im)
plt.scatter(ct_data_awp['attacker_mapX'], ct_data_awp['attacker_mapY'],alpha=0.005,c='blue')
```
筛选出未种炸弹、进攻方是ct、使用了AWP枪支且获胜的数据。绘制ct使用AWP枪支时的位置，用蓝色圆点表示。
