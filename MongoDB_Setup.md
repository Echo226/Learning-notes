## 官方安装指导

[官方英文安装指导链接](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x-tarball/)



## 中文安装指导

### 一、下载安装

[Mac版官网下载地址](https://www.mongodb.com/download-center/community)

下载后解压得到mongodb-4.0.8这个文件夹，复制到 /usr/local/路径下



### 二、设置路径

进入terminal，打开bash_profile添加如下路径，并更新bash_profile

```commonlisp
open -e .bash_profile
```

```
# added MangoDB Home path
export MONGODB_HOME=/usr/local/mongodb-4.0.8
export PATH=${MONGODB_HOME}/bin:$PATH
```

```
source .bash_profile
```



### 三、运行MongoDB

#####3.1 创建data directory

```
默认：sudo mkdir -p /data/db
指定目录：sudo mkdir -p /usr/local/mongodb-4.0.8/data/db
```



#####3.2 为data directory授权

参考 [Mongo基本命令](https://blog.51cto.com/linuxg/1895805)，搜索 <u>三、MongoDB使用</u>  或 <u>Read and write access to data and configuration is unrestricted</u>

参考 [Access control is not enabled for the database.](https://blog.csdn.net/ttxsely/article/details/77726164)



##### 3.3 启动MongoDB

法一：直接运行

```
mongod
```

法二：指定mongod的路径

```
cd /usr/local/mongodb-4.0.8/bin
mongod
```

法三：指定data directory的路径

```
mongod --dbpath /usr/local/mongodb-4.0.8/data/db
```



##### 3.4 测试是否成功启动MongoDB

如果上一部会输出以下结果，则证明MongoDB已成功启动。

```
[initandlisten] waiting for connections on port 27017
```



##### 3.5 开始使用MongoDB

法一：使用 **command+T** 开启mongo shell，然后输入 **mongo**，启动后输入1+1得到2

法二：新建一个terminal窗口，输入**mongo**，启动后输入1+1得到2。这个步骤是在操作数据库，不需要重新进入bin目录，新建窗口直接执行命令即可。

此时在浏览器中输入 **localhost:27017**，会在浏览器中显示 “It looks like you are trying to access MongoDB over HTTP on the native driver port.”



##### 3.6 正确退出MongoDB



—————— 网上说要用以下操作来退出数据库 但我还没成功过 ——————

每次使用完MongdoDB后都要正确退出，否则下次再此链接数据库会出现问题。

在操作数据库的terminal窗口中执行以下代码：

```
use admin;
db.shutdownServer();
```

但我好像还没成功退出过？我的输出如下，似乎没有关掉，最后用了quit() 溜了。

```
> use admin
switched to db admin
> db.shutdownServer()
server should be down...
I NETWORK  [js] trying reconnect to 127.0.0.1:27017 failed
I NETWORK  [js] reconnect 127.0.0.1:27017 failed failed 
>
```

此时再次输入mongo使用数据库会报如下错误：

```
Echo:~ echo$ mongo
MongoDB shell version v4.0.8
connecting to: mongodb://127.0.0.1:27017/?gssapiServiceName=mongodb
2019-04-06T00:33:54.029-0400 E QUERY    [js] Error: couldn't connect to server 127.0.0.1:27017, connection attempt failed: SocketException: Error connecting to 127.0.0.1:27017 :: caused by :: Connection refused :
connect@src/mongo/shell/mongo.js:343:13
@(connect):2:6
exception: connect failed
```

但是重新运行3.3 - 3.6似乎就可以了？

—————————————————————————————————

—————— 官网说只需要用quit() 或 command+C 退出shell即可 ———



##### 备注

如果安装成功后，以后只需要运行3.3 - 3.6即可使用MongoDB。





## 常见错误

### 一、错误代号100

启动MongdoDB时，使用法一直接输入mongod后显示错误代码100，如下：

```
autoreg-178397:bin echo$ mongod
2019-04-05T20:21:28.863-0400 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten] MongoDB starting : pid=59408 port=27017 dbpath=/data/db 64-bit host=Echo.local
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten] db version v4.0.8
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten] git version: 9b00696ed75f65e1ebc8d635593bed79b290cfbb
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten] allocator: system
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten] modules: none
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten] build environment:
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten]     distarch: x86_64
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten]     target_arch: x86_64
2019-04-05T20:21:28.872-0400 I CONTROL  [initandlisten] options: {}
2019-04-05T20:21:28.873-0400 I STORAGE  [initandlisten] exception in initAndListen: NonExistentPath: Data directory /data/db not found., terminating
2019-04-05T20:21:28.873-0400 I NETWORK  [initandlisten] shutdown: going to close listening sockets...
2019-04-05T20:21:28.873-0400 I NETWORK  [initandlisten] removing socket file: /tmp/mongodb-27017.sock
2019-04-05T20:21:28.873-0400 I CONTROL  [initandlisten] now exiting
2019-04-05T20:21:28.873-0400 I CONTROL  [initandlisten] shutting down with code:100
```

#### 1.1 原因解析

MongoDB starting : pid=59408 port=27017 **dbpath=/data/db** 64-bit host=Echo.local

NonExistentPath: **Data directory /data/db not found**., terminating

这是目录指定的问题。官网对于storage.dbPath的说明如下，由于默认的dbpath路径为/data/db，而我将该文件夹创建在 /usr/local/mongodb-4.0.8/data/db 里，所以会导致 Data directory not found.

![Screen Shot 2019-04-05 at 21.05.36](/Users/echo/Desktop/Screen Shot 2019-04-05 at 21.05.36.png)



#### 1.2 解决方案

##### 方案一 声明data directory的路径

用 **mongod --dbpath /usr/local/mongodb-4.0.8/data/db** 来声明data directory的路径，但是每次重新启动Mongodb时都要声明。

##### 方案二 修改mongod.conf文件

mongod.conf一般默认在/usr/local/etc/路径下，而我在/usr/local/mongodb-4.0.8/ect/里自行创建了一个mongod.conf文件并输入以下设置：

```
systemLog:
   destination: file
   path: "/usr/local/mongodb-4.0.8/log/mongod.log"
   logAppend: true
storage:
   dbPath: "/usr/local/mongodb-4.0.8/data/db"
   journal:
      enabled: true
processManagement:
   fork: true
net:
   bindIp: 127.0.0.1
   port: 27017
setParameter:
   enableLocalhostAuthBypass: false
```

保存后，如果要配置mongod，需运行以下代码来使用configuration文件：

```
mongod --config /usr/local/mongodb-4.0.8/etc/mongod.conf
```

但是我没有成功，下次运行还是只能使用1.2.1的方法。



### 二、错误代号48

如果在3.5打开的shell里直接用quit()退出shell后，下次再使用3.3启动MongoDB，会显示错误代码48，具体如下：

```
autoreg-178397:bin echo$ mongod --dbpath /usr/local/mongodb-4.0.8/data/db
2019-04-06T00:55:34.520-0400 I CONTROL  [main] Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] MongoDB starting : pid=59687 port=27017 dbpath=/usr/local/mongodb-4.0.8/data/db 64-bit host=autoreg-178397.dyn.wpi.edu
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] db version v4.0.8
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] git version: 9b00696ed75f65e1ebc8d635593bed79b290cfbb
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] allocator: system
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] modules: none
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] build environment:
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten]     distarch: x86_64
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten]     target_arch: x86_64
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] options: { storage: { dbPath: "/usr/local/mongodb-4.0.8/data/db" } }
2019-04-06T00:55:34.530-0400 E STORAGE  [initandlisten] Failed to set up listener: SocketException: Address already in use
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] now exiting
2019-04-06T00:55:34.530-0400 I CONTROL  [initandlisten] shutting down with code:48
```

#### 2.1 原因解析

```
[initandlisten] Failed to set up listener: SocketException: Address already in use
```

这是上次使用MongoDB后，27017端口没有关闭，此时在浏览器输入localhost:27017仍能显示端口。

#### 2.2 解决方案

查看使用某端口的进程，代码如下：

```
lsof -i :端口号
```

```
lsof -i :27017
得到如下结果：
COMMAND   PID USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
mongod  59665 echo   10u  IPv4 0x66eec2e3fbf1857f      0t0  TCP localhost:27017 (LISTEN)
```

关闭某进程的命令，代码如下：

```
sudo kill -9 PID
```

```
sudo kill -9 59665
```

执行该代码就可以关闭了，此时在浏览器输入localhost:27017会显示无法连接服务器，完成！





## Reference

https://www.cnblogs.com/haonanZhang/p/8213947.html

https://blog.51cto.com/linuxg/1895805

https://blog.csdn.net/ttxsely/article/details/77726164

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x-tarball/

https://hikalu-z.github.io/2017/04/13/mongoDB/