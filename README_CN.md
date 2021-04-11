## 命令行微博热搜
一句命令查看微博热搜榜，了解当下正在发生的大事

有什么用？Linux用户无需离开命令行查看热搜 ~~运维人员上班摸鱼神器~~

Python Script 根据[weibo_Hot_Search项目](https://github.com/Writeup001/weibo_Hot_Search)修改，感谢Writeup大佬的项目支持

English Users [Click here](https://github.com/zhzhzhy/WeiBoHot/blob/master/README.md)

<!-- vim-markdown-toc GFM -->

* [运行环境安装与配置](#运行环境安装与配置)
* [运行](#运行)
	* [Linux用户](#linux用户)
* [数据来源](#数据来源)
* [效果如何？](#效果如何)

<!-- vim-markdown-toc -->

## 运行环境安装与配置
- 安装 Python 3.0 + 
- 安装Python依赖包: requests lxml
```
pip install requests

pip install lxml
```
完成运行环境安装(国内pip换源访问问题请搜索'pip换源'解决)
## 运行
### Linux用户
给予Python脚本运行权限，可直接执行
```
chmod +x WeiBoHot.py
./WeiBoHot.py
```
若无法运行，尝试
```
python WeiBoHot.py
```
或
```
python3 WeiBoHot.py
```
## 数据来源
新浪微博公开热搜榜单: https://s.weibo.com/top/summary/
## 效果如何？
这就是效果：

![result.png](/img/result.png)

