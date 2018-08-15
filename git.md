0.  在GitHub上创建仓库

1.  创建信息
	Repository name: 仓库名称
	Description(可选): 仓库描述介绍
	Public, Private : 仓库权限（公开共享，私有或指定合作者）
	Initialize this repository with a README: 添加一个README.md
	gitignore: 不需要进行版本管理的仓库类型，对应生成文件.gitignore
	license: 证书类型，对应生成文件LICENSE

2.  clone地址，选http形式的

3.  在本地git bush

4.  $git clone 上边的地址

5.  GitHub上的文件夹出现在目录中，把这以外的文件剪切到此文件夹中

6.  cd 此文件夹进入master

7.  git add . （注：别忘记后面的.，此操作是把文件夹下面的文件都添加进来）

8.  git commit -m "xxx" 

9.  git push -u origin master (注：此操作目的是把本地仓库push到github上面，此步骤需要你输入帐号和密码）

10. 注：在commit时候可能会遇到“让你确认身份的步骤”
	$ git config --global user.name "DHT"
	$ git config --global user.email "839338977@qq.com"
