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

<img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE3%20%E8%A7%86%E9%A2%91%E5%B1%9E%E6%80%A7%E7%9A%84%E5%85%B3%E8%81%94%E7%B3%BB%E6%95%B0.png" width="300px">

## Video - channel network（视频——频道关系网）
https://pan.bnuz.edu.cn/l/g1ydM2 password:bnuz
| Attribute | explanation |
| ----- | ----- |
|videoType	| 视频类型 |
relation	|属于|
channel|	频道标签

<img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE1%20%E7%94%B5%E7%AB%9E%E7%B1%BB%E5%9E%8B%E9%A2%91%E9%81%93%E5%85%B3%E7%B3%BB%E7%BD%91%E5%9B%BE.png" width="260px"><img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE10%20%E9%AC%BC%E7%95%9C%E7%B1%BB%E5%9E%8B%E9%A2%91%E9%81%93%E5%85%B3%E7%B3%BB%E7%BD%91%E5%9B%BE.png" width="260px"><img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE11%20%E5%8A%A8%E6%BC%AB%E7%B1%BB%E5%9E%8B%E9%A2%91%E9%81%93%E5%85%B3%E7%B3%BB%E7%BD%91%E5%9B%BE.png" width="260px">

## Bullet-screen comment corpus（弹幕语料）
### all corpus（所有语料）
uploading...
### Classification of corpus （分类语料）
鬼畜类
uploading...

电竞类
uploading...

动漫类
uploading...

疫情类
uploading

### 文本语料
为了供仅需要文本数据的学者使用，本文也提供了纯文本语料，利于训练语言模型。

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
