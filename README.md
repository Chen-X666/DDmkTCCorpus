# Open source of the bullet-screen comments data（弹幕语料开源数据集）
The project provides open source comment data for researchers to conduct in-depth research on the barrage corpus, which mainly focuses on the subculture bullet-screen comment corpus (including but not limited to the guichu, animation and e-sports type).  

本项目开源弹幕评论数据供科研人员深入研究弹幕语料，语料主要集中在亚文化弹幕语料（包括但不限于鬼畜、动漫与电竞类弹幕）


Corpus is maintained by Xin, Chen (Beijing Normal University, Zhuhai, China).

语料库由陈鑫(北京师范大学，中国珠海)维护。

Now, this project only releases a little bit of corpus. After the paper publish, all the corpus would release 

现在，这个项目只发布了少量的语料库。论文发表后，所有的语料库都将发布

If u have any questions, please contact my email: ChenXinV@outlook.com

如果您有任何问题，请联系我的邮箱:ChenXinV@outlook.com

## Video corpus（视频语料）
2017——2020 播放量大于100w的鬼畜、电竞、动漫视频语料

https://pan.bnuz.edu.cn/l/J5z6nP password:bnuz

| Attribute | explanation |
| ----- | ----- |
|Bvno	| 视频识别号 |
Tname	|主标签|
Tag_name|	标签列表
Owner_mid	|发布者Id
Title	|标题
Pubdate	|发布时间
Duration	|持续时间
View	|观看数量
Danmaku	|弹幕数量
Reply	|转发数量
Favorite	|收藏数量
Coin	|投币数量
Share	|分享数量
Like	|喜欢数量

## Video - channel network（视频——频道关系网）
https://pan.bnuz.edu.cn/l/g1ydM2 password:bnuz
| Attribute | explanation |
| ----- | ----- |
|videoType	| 视频类型 |
relation	|属于|
channel|	频道标签

<img src="https://user-images.githubusercontent.com/55039294/158780362-c48afef9-7e1d-4929-b1a7-2f308e2fdacb.png" width="280px"><img src="https://user-images.githubusercontent.com/55039294/158780565-dec7b2f8-e29c-4b8c-97e4-5e4c08d4c619.png" width="280px"><img src="https://user-images.githubusercontent.com/55039294/158780036-985d0dfc-33ca-4177-addc-3f2308d2c236.png" width="280px">

## Bullet-screen comment corpus（弹幕语料）
### 所有属性语料
uploading...
### 分类语料
鬼畜类
uploading...

电竞类
uploading...

动漫类
uploading...

疫情类
uploading

### 文本属性语料
https://pan.bnuz.edu.cn/l/noXqE7 password:bnuz
| Attribute | type | explanation | Default |
| ----- | ----- |  ----- |  ----- |
text  | (str) | 弹幕文本
dm_time   | (float)  | 弹幕在视频中的位置，单位为秒 | 0.0
send_time |(float)   | 弹幕发送的时间 | time.time()
crc32_id  |(str)     | 弹幕发送者 UID 经 CRC32 算法取摘要后的值 | None
color     |(str)     | 弹幕十六进制颜色 | "ffffff"
weight    |(int)     | 弹幕在弹幕列表显示的权重  | -1
id_       |(int)     | 弹幕 ID | -1
id_str    |(str)     | 弹幕字符串 ID  | ""
action    |(str)     | 暂不清楚 | ""
mode      |(Mode)    | 弹幕模式  | Mode.FLY
font_size |(FontSize)| 弹幕字体大小  | FontSize.NORMAL
is_sub    |(bool)    | 是否为字幕弹幕  | False
pool      |(int)     | 暂不清楚 | -1
attr      |(int)     |暂不清楚 | -1

## word2vec model training by 4000w bullet-screen comments（利用4000w弹幕训练的word2vec模型）
uploading...

## Citation
Papers are being published...
论文正在发表...
