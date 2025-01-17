1. crontab 计划任务
   1. 没有的话需要查找一下
      1. apt-cache search crontab
   2. crontab -l 
      1. 列出
   3. crontab -e
      1. 编辑 之后根据提示选择编辑器
   4. 0 5 * * 1 tar -zcf /var/backups/home.taz /home/
      1. 0 5 * * 1
         1. 分钟 小时 日 月 星期 
            1. */1表示每分钟
      2. tar -zcf /var/backups/home.taz /home
         1. 这是实际的备份命令，使用 tar 工具将 /home 目录打包并压缩为一个归档文件。
         2. tar：用于创建归档文件的命令
         3. -z：使用 gzip 压缩归档文件。
         4. -c：创建新的归档文件。
         5. -f：指定归档文件的名称。
         6. /var/backups/home.taz：归档文件的保存路径和名称（.taz 是 .tar.gz 的简写）。
         7. /home：要备份的目录。
      3. 每周一的凌晨 5 点整，将 /home 目录打包并压缩为 /var/backups/home.taz 文件，用于备份。
   5. -u user : 用来设定某个用户的crontab服务
   6. -e： 编辑某个用户的crontab任务
2. tar 压缩 解压缩
   1. -c 建立一个压缩文件得参数指令 create的意思
   2. -x 解开一个压缩文件得参数指令
   3. -t 查看tarfile里面的文件
   4. 特别注意 c/x/t同时只能存在一个 应为不能同时压缩与解压缩
   5. -z 是否同时具有gzip得属性
   6. -j 是否同时具有bzip2得输赢
   7. -v 压缩得过程中显示文件
   8. -f 使用档名，f后要立即接文件名称
   9. -P 使用源文件得原来属性
   10. -p 可以使用绝对路径来压缩
   11. -n 此后面接的日期(yyyy/mm//dd) 还要新的才会被打包进新建得文件中!
3. 