1.安装git:
```
sudo apt-get install git
```
2. 生成ssh key，使用命令 ssh-keygen -t rsa -C “用户名”,一直enter,enter,enter,
```
ssh-keygen -t rsa -C “jc5121”
```
3. 回到github，进入edit profile—personal setting，左边选择SSH Keys，Add SSH Key,title随便填，粘贴key。key就是idrsa.pub内容。用命令：cat id_rsa.pub 查看。

4. 测试ssh key是否成功，使用命令“ssh -T git@github.com”，如果出现You’ve successfully authenticated, but GitHub does not provide shell access 。这就表示已成功连上github。第一次连接可能会问一些问题，yes就可以了。

5.配置Git的配置文件，username和email

git config –global user.name “your name” //配置用户名

git config –global user.email “your email” //配置email

查看配置信息：

git config user.name

git config user.email

6 利用Git从本地上传到GitHub
git init+git remote add origin git@github.com:yourName/yourRepo.git+ git add xxx+git commit -m "this is for test"+git push origin master
```
https://zhuanlan.zhihu.com/p/37685863
```
