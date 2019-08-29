
whichis command --> 当前命令所在路径
whereis command --> 包含当前command字符的路径(安装多个版本的命令时)

## 文件及目录管理
**创建，删除,移动,复制**
mkdir dir_name
touch
rm [-d空目录][-r递归的][-f强制]
rm *文件后缀 (文本的匹配,批量进行删除)
mv 源文件 目标文件
cp [源文件/目录] [目标文件/目录]

**目录切换**
cd 目录
cd -
cd ~/cd
pwd


**列出目录里面文件**
ls
ls -a (全部)
ls -l (详细内容,权限,组,创建日期等)
ls -ld (目录信息)
ls -s
ls -asl ()
ls -lrt (时间逆序排序显示)

**文件查找**
find与locate
find ./ -name '*.md'

**查看文件内容**
cat -n file (显示行号)
head -10 file
tail -10 file
diff file1 file2


**查找文件内容**
egrep

**文件与目录权限修改**
chmod
chmod [u/g/o/a] [+/-/=] [r/w/x] file
e.g.: chmod ugoa+rwx dile
chmod [xyz] file  xyz分别对应user,group,other (r=4,w=2,x=1)
chmod 777 file

**文件增添别名**
软硬链接
ln

**管道和重定向**
ls

**设置环境变量**
安装的软件路径一般要加入到path中
PATH=


## 2 磁盘管理
**查看磁盘空间**
df -h

**打包和压缩**
打包 tar -cvf name.tar *.jpg
解包 tar -xvf name.tar
tar -xzvf file.tar.gz
tar -xjvf file.tar.bz2
tar -xZvf file.tar.Z

## 3 进程管理工具
任何事物都是文件

