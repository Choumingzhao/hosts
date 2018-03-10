# hosts
Some blacklist websites I need to block -> [blacklist](blacklist)

## This repo is just a list, you should use these repos
1. [StevenBlack's hosts](https://github.com/StevenBlack/hosts)
2. [AD hosts by vokins](https://github.com/vokins/yhosts)

## How to quickly generate your hosts
1. Clone StevenBlack's repo
2. Add AD hosts and your own personal entries to the file [blacklist](blacklist)
3. replace the `blacklist` file in StevenBlack's repo  with this file and just follow the commands in the README.
4. Enjoy it !

## What does [urls2hosts.py](urls2hosts.py) do?
It's a very small (Python 3 only) script for you to convert your url blacklist to a hosts. Just run:
```bash
# print to the terminal
$ python urls2hosts.py url_blacklist # And copy and paste
# or write to file
$ python urls2hosts.py url_blacklist > filename.you.like
# or directly append to your blacklist
$ python urls2hosts.py url_blacklist >> blacklist
```

# hosts
屏蔽我不喜欢的那些中国网站 -> [blacklist](blacklist)


## 本 repo 只是一个列表，使用以下项目让你更加方便
1. [StevenBlack's hosts](https://github.com/StevenBlack/hosts)
2. [AD hosts by vokins](https://github.com/vokins/yhosts)

## 如何快速生成我的 hosts 文件
1. Clone StevenBlack 的 repo
2. 将 AD hosts 和 你自己的 hosts 加入 [blacklist](blacklist)
3. 使用替换后的 `blacklist` 替换 StevenBlack repo 中的同名文件
4. Enjoy it !

## [urls2hosts.py](urls2hosts.py) 做什么的?
一个十分简单的脚本，将你的黑名单网址列表转化为 hosts 列表。使用如下命令来运行：
```bash
# 打印到 terminal
$ python urls2hosts.py url_blacklist # 复制粘贴到相应文件
# or 写到文件
$ python urls2hosts.py url_blacklist > filename.you.like
# or 直接添加到 blacklist 文件
$ python urls2hosts.py url_blacklist >> blacklist
```
