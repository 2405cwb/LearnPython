# author: cwb
# date: 2025/1/16
# ubuntu学习

# 所有目录
# / 根目录
# /boot boot配置文件 内核和其他启动时需要的文件
# /etc 存放系统配置有关的文件
# /home 存放普通用户目录
# /mnt 硬盘上手动挂载的文件区
# /media 自动挂载的硬盘分区及类似 CD 数码相机等移动介质
# /cdrom 挂载光盘？
# /opt 存放一些可选择的程序，如某个程序的测试版本，安装到该目录的程序的所有数据 库文件都在同个目录下
# /root 系统 管理员目录
# /bin 存放常用程序 命令文件
# /sbin 系统管理命令 存放系统管理员使用的管理程序
# /tmp 临时目录 存放临时文件 系统会定期清理
# /usr 该目录下 可以找到哪些不适合放在/bin或者/etc下的额外工具，如游戏，打印工具等
# /var 存放经常被修改的文件，如日志
# /var/cache 应用程序缓存数据


# 创建目录
# mkdir aa
# 创建多层目录
# mkdir -p aa/dd/cc
#
# 创建文件
# touch 主要用来修改文件的时间
# touch a.txt
#
# 删除文件
# rm a.txt
# 删除目录
# rm -r a
# rm -f a
# sudo rm -rf / home
#
# 重命名文件目录
# mv  qq.py a.py
# 移动文件
# mv qq.py a
# 复制文件
# cp aa.py dd.py
# 递归复制路径
# cp aa -r dd
# 复制并复制权限
# cp a -a d
# 查看具体信息
# stat a.txt
#
# 查看时间
# date
# 查看日历
# cal
# cal -y
#
#
# 清屏
# ctrl+l
# 删除当前光标之后的
# ctrl+k
# 删除之前的
# ctrl+u
# 删除到前方空格
# ctrl+w
# 恢复
# ctrl+y
# 退出当前终端
# ctrl+d
# 帮助手册
# man
# man man
# export LANG=C 英文
# man -k passwd 模糊匹配
# man -f passwd 精确匹配
#
# 使用 cat 创建文件并写入内容





