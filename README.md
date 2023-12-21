<div align="center"><img src="https://avatars.githubusercontent.com/u/128916285?s=400&u=8ea76106ce0018439d6d6414b26aea62680712d6&v=4" height="100px"/></div>

<h2 align="center"> 📕DDmkTCCorpus: Diachronic Danmaku Text Comments Corpus</h2>

<h4 align="center">
    <a href="https://github.com/DBsCCorpus">中文</a> |
    <a href="https://github.com/DBsCCorpus">English</a>
</h4>

1️⃣ The project provides open source comment data for researchers to conduct in-depth research on the bullet-screen corpus, which mainly focuses on the subculture bullet-screen comment corpus (including but not limited to the guichu, animation and e-sports type).  

2️⃣ Corpus is maintained by TinyTalks, a Community for NLP research in Short Text in Chinese. 


## Video corpus
The video corpus were more than 1 milions plays during the years from 2017 to 2020. The attributes can be as follow.
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

Source: https://pan.bnuz.edu.cn/l/J5z6nP password:bnuz

<img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE3%20%E8%A7%86%E9%A2%91%E5%B1%9E%E6%80%A7%E7%9A%84%E5%85%B3%E8%81%94%E7%B3%BB%E6%95%B0.png" width="300px">

## Video - channel network
https://pan.bnuz.edu.cn/l/g1ydM2 password:bnuz
| Attribute | explanation |
| ----- | ----- |
|videoType	| 视频类型 |
relation	|属于|
channel|	频道标签

<img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE1%20%E7%94%B5%E7%AB%9E%E7%B1%BB%E5%9E%8B%E9%A2%91%E9%81%93%E5%85%B3%E7%B3%BB%E7%BD%91%E5%9B%BE.png" width="260px"><img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE10%20%E9%AC%BC%E7%95%9C%E7%B1%BB%E5%9E%8B%E9%A2%91%E9%81%93%E5%85%B3%E7%B3%BB%E7%BD%91%E5%9B%BE.png" width="260px"><img src="https://github.com/Chen-X666/bullet-screenCorpus/blob/main/%E5%9B%BE11%20%E5%8A%A8%E6%BC%AB%E7%B1%BB%E5%9E%8B%E9%A2%91%E9%81%93%E5%85%B3%E7%B3%BB%E7%BD%91%E5%9B%BE.png" width="260px">

## Bullet-screen comment corpus
The attributes detail can as follow.

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
### All corpus
uploading...
### Classification of corpus 

鬼畜类
https://pan.bnuz.edu.cn/l/pn3Yj5(密码：bnuz)

电竞类
https://pan.bnuz.edu.cn/l/I510mH(密码：bnuz)

动漫类
https://pan.bnuz.edu.cn/l/toTTtQ(密码：bnuz)

疫情类
https://pan.bnuz.edu.cn/l/aoMMOM(密码：bnuz)

https://pan.bnuz.edu.cn/l/onFbAO(密码：bnuz)

https://pan.bnuz.edu.cn/l/QJGkNF(密码：bnuz)

### Text corpus
In order to be used by scholars who only need textual data, this paper also provides a plain text corpus, which is useful for training various language models。

https://pan.bnuz.edu.cn/l/r1Kkfd(密码：bnuz)


## DanmakuMarked-data（弹幕情感标注数据）
数据使用utf-8编码，逗号分隔的csv保存

数据分为数字信息、文本信息、标注分类（未标注数据无标注信息）

数字信息包含：弹幕在视频中出现的时间点、展示模式、字号、字体颜色、发送时间、弹幕池编号、发送用户编号、在弹幕数据库中的编号，信息用逗号分隔

标注类别：0高兴、1难过、2愤怒、3惊、4负样本

https://pan.bnuz.edu.cn/l/snpijm password: bnuz

citation: https://github.com/MelkiorOno/DanmakuMarked-data

## Citation

If you use this corpus in your research, please cite this repository.

```bibtex
@article{
 QBTS202209010,
 author = {陈鑫,张以欣,吴俊潮,郭凌宇,余泽汇 & 杨静},
 title = {历时弹幕语料库的构建与探析——以青年亚文化弹幕为例},
 journal = {情报探索},
 volume = {No.299},
 number = {77-85},
 year = {2022},
 issn = {1005-8095},
 doi ={}
 }
```
