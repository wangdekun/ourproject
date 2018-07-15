# 1.安装git:
```
sudo apt-get install git
```
# 2. 生成ssh key，使用命令 ssh-keygen -t rsa -C “用户名”,一直enter,enter,enter,
```
ssh-keygen -t rsa -C “jc5121”
```
# 3. 回到github，进入edit profile—personal setting，左边选择SSH Keys，Add SSH Key,title随便填，粘贴key。key就是idrsa.pub内容。用命令：cat id_rsa.pub 查看。

# 4. 测试ssh key是否成功，使用命令“ssh -T git@github.com”，如果出现You’ve successfully authenticated, but GitHub does not provide shell access 。这就表示已成功连上github。第一次连接可能会问一些问题，yes就可以了。

# 5.配置Git的配置文件，username和email

git config –global user.name “your name” //配置用户名

git config –global user.email “your email” //配置email

查看配置信息：

git config user.name

git config user.email

# 6 利用Git从本地上传到GitHub
```
git init+git remote add origin git@github.com:yourName/yourRepo.git+ git add xxx+git commit -m "this is for test"+git push origin master
```
https://zhuanlan.zhihu.com/p/37685863
```
# 7安装tomcat
```
在官网下载tomcat9.0.10然后放入本地文件夹，进行配置，只需要在/tomcat7/bin 下，编catalina.sh文件，插入JAVA_HOME=/opt/jdk1.6.0_22，注意需要给tomcat文件夹权限，否则idea没法导入tomcat           //--此处依你的jdk安装目录而定
```

```
alter table user_info add password Varchar(10) not null 向表格中扩展一个password字段
```

```
WriteNullListAsEmpty  ：List字段如果为null,输出为[],而非null
WriteNullStringAsEmpty ： 字符类型字段如果为null,输出为"",而非null
DisableCircularReferenceDetect ：消除对同一对象循环引用的问题，默认为false（如果不配置有可能会进入死循环）
WriteNullBooleanAsFalse：Boolean字段如果为null,输出为false,而非null
WriteMapNullValue：是否输出值为null的字段,默认为false
链接：https://juejin.im/post/5ad811e66fb9a0460138ceb1
来源：掘金

```

```
自动生成dao,model,xml文件，首先需要在sql中sql语句写好，建行数据库表，然后创建core→constant→ProjectConstant，这步操作只需要一次就好，接着创建src\test\java\com\example\demo\CodeGenerator.java，在这步只需要修改其中的表名就可以了，配置文件此处省略，详情见掘金网
```

