# Github Guide



## Github Command Line

#### git init

```
git init   # 初始化一个本地的repository，在哪个文件夹下使用git init，该文件夹便是repo
```

#### git add

修改完 需要用git add将修改添加到缓存区stage里等待commit 

```commonlisp
git add .
git add <filename>
git *.txt
```

#### git status

```
git status
```

#### git diff 

查看修改内容

```
git diff
git diff HEAD -- <filename> #查看working directory和repository里最新版本的区别
```

#### git commit

```
git commit -m 'added README.md'
```

#### git log 

查看提交历史，以便找出每个提交记录的commit_id，方便回退到某个具体版本

```
git log
git log --pretty=oneline
```

#### git reset 

回退到某个版本

```
git reset --hard HEAD^       #将版本回退到repository中最新的版本
git reset --hard <commit_id> #将版本回退到repository中某个具体版本
git reset HEAD <fileName>    #把缓存区的修改回退到工作区 HEAD指最新版本
```

#### git reflog

查看命令历史，以便找出未来版本的commit_id，方便回到未来某个具体版本

```
git reflog
```

#### git checkout

不小心删除了工作区的文件，用git checkout可以恢复

撤销/丢弃工作区的修改，回到最近一次git add或git commit的状态：

- 修改了但还没有git add时，撤销修改后的状态和repository的状态一样
- 修改了已经git add 但还没有git commit时，撤销修改后的状态和stage的状态一样

```
git checkout -- <fileName>
git checkout <branchName>
```

#### git rm

```
rm fileName                       # 先删除本地工作区里的文件
git checkout -- <fileName>        # 不小心删错时 可用git checkout一键还原
git rm <fileName>                 # 删除repository里的文件
git commit -m 'deleted fileName'  # 删除后需要commit
```

#### git push

在Github创建好repository后，先关联两个库，再把本地的master branch推送到Github的master branch里

```
# SSH
git remote add origin git@server-name:<path>/<repo-name.git>
git remote add origin git@github.com:Echo226/<repoName>.git
# HTTPS
git remote add origin https://github.com/Echo226/<repoName>.git  
```

```
git push -u origin master  # 第一次推送master分支时 加上-u参数 Git除了推送 还会关联两地的分支
git push  origin master    # 以后的推送不需要-u参数
```

#### git clone

如果是开源项目，先Fork到自己的Github里，再clone到本地，修改完push到自己Github上，再Pull request

```
git clone <repoAddress>
git clone git@github.com:Echo226/Waters.git  # 例子
```



## 分支管理

### 创建并合并分支

#### git branch/checkout

```
git branch xinting         # 创建分支xinting
git checkout xinting       # 切换到分支xinting
git checkout -b xinting    # 创建并切换分支 相当于上面的两条命令
git branch                 # 列出所有分支 当前分支前面标有*号
```

#### git branch/switch

最新版本的git使用swith来切换分支

```
git branch xinting         # 创建分支xinting
git switch xinting         # 切换到分支xinting
git switch -c xinting      # 创建并切换分支 相当于上面的两条命令
git branch                 # 查看所有分支
```

#### git merge

合并指定的分支到**当前分支**：此时是Fast-forward合并模式 直接把master指针指向xinting的当前提交

```
git checkout master        # 先将当前分支切换回master
git merge xinting          # 将指定的xinting分支合并到当前分支master
git branch -d xinting      # 合并后 删除xinting分支
git branch                 # 删除后 查看branch只剩下master
```



### 解决冲突

### 分支管理策略

### Bug分支









## Github SSH





fads 



















