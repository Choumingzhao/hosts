# hosts
Some blacklist websites I need to block, everything in the file [blacklist](blacklist)

## Some hosts program you should consider
1. [StevenBlack's hosts](https://github.com/StevenBlack/hosts)
2. [AD hosts by vokins](https://github.com/vokins/yhosts)

## How to quickly generate my hosts
After clone StevenBlack's repo, you can add AD hosts and your own personal entries to the file [blacklist](blacklist), replace the `blacklist` file in StevenBlack's repo  with this file and just follow the commands in the README.

## What does [urls2hosts.py](urls2hosts.py) do?
It's a very small script for you to convert your url blacklist to a hosts. Just run:
```bash
$ python urls2hosts.py url_blacklist # And copy and paste
# or
$ python urls2hosts.py url_blacklist > filename.you.like
```
