# 一、表内容操作（增删改查）
'''表内容操作

1、增
    1, insert into 表 (列名,列名...) values (值,值,值...)
    2, insert into 表 (列名,列名...) values (值,值,值...),(值,值,值...)
    3, insert into 表 (列名,列名...) select (列名,列名...) from 表

2、删
    1,delete from 表
    2,delete from 表 where id＝1 and name＝'alex'
3、改
    update 表 set name ＝ 'alex' where id>1
4、查
    1,select * from 表
    2,select * from 表 where id > 1
    3,select nid,name,gender as gg from 表 where id > 1
'''
#'5、其他（where,like,limit,order,group,join,union
'''
'5、其他

a、条件
    select * from 表 where id > 1 and name != 'alex' and num = 12;
 
    select * from 表 where id between 5 and 16;
 
    select * from 表 where id in (11,22,33)
    select * from 表 where id not in (11,22,33)
    select * from 表 where id in (select nid from 表)
 
b、通配符
    select * from 表 where name like 'ale%'  - ale开头的所有（多个字符串）
    select * from 表 where name like 'ale_'  - ale开头的所有（一个字符）
 
c、限制
    select * from 表 limit 5;            - 前5行
    select * from 表 limit 4,5;          - 从第4行开始的5行
    select * from 表 limit 5 offset 4    - 从第4行开始的5行
 
d、排序
    select * from 表 order by 列 asc              - 根据 “列” 从小到大排列
    select * from 表 order by 列 desc             - 根据 “列” 从大到小排列
    select * from 表 order by 列1 desc,列2 asc    - 根据 “列1” 从大到小排列，如果相同则按列2从小到大排序
 
e、分组
    select num from 表 group by num
    select num,nid from 表 group by num,nid
    select num,nid from 表  where nid > 10 group by num,nid order nid desc
    select num,nid,count(*),sum(score),max(score),min(score) from 表 group by num,nid
 
    select num from 表 group by num having max(id) > 10
 
    特别的：group by 必须在where之后，order by之前
 
f、连表
    无对应关系则不显示
    select A.num, A.name, B.name
    from A,B
    Where A.nid = B.nid
 
    无对应关系则不显示
    select A.num, A.name, B.name
    from A inner join B
    on A.nid = B.nid
 
    A表所有显示，如果B中无对应关系，则值为null
    select A.num, A.name, B.name
    from A left join B
    on A.nid = B.nid
 
    B表所有显示，如果B中无对应关系，则值为null
    select A.num, A.name, B.name
    from A right join B
    on A.nid = B.nid
 
g、组合
    组合，自动处理重合
    select nickname
    from A
    union
    select name
    from B
 
    组合，不处理重合
    select nickname
    from A
    union all
    select name
    from B
'''
#二、数据表基本
# 创建表create table
'''
1、创建表
create table 表名(
    列名  类型  是否可以为空，
    列名  类型  是否可以为空
    )ENGINE=InnoDB DEFAULT CHARSET=utf8
    
    是否可空，null表示空，非字符串
    not null    - 不可空
    null        - 可空
    '''
# 修改表名RENAME TABLE 旧表名 TO 新表名;
#默认值defalut
'''
    默认值，创建列时可以指定默认值，当插入数据时如果未主动设置，则自动添加默认值
    create table tb1(
        nid int not null default 2,
        num int not null )
    '''
#自增auto_increment
'''
    自增，如果为某列设置自增列，插入数据时无需设置此列，默认将自增（表中只能有一个自增列）
    create table tb1(
        nid int not null auto_increment primary key,
        num int null)
    或
    create table tb1(
        nid int not null auto_increment,
        num int null,
        index(nid) )
    注意：1、对于自增列，必须是索引（含主键）。
         2、对于自增可以设置步长和起始值
             show session variables like 'auto_inc%';
             set session auto_increment_increment=2;
             set session auto_increment_offset=10;

             shwo global  variables like 'auto_inc%';
             set global auto_increment_increment=2;
             set global auto_increment_offset=10;
'''
# 主键primary key
'''
   主键，一种特殊的唯一索引，不允许有空值，如果主键使用单个列，则它的值必须唯一，如果是多列，则其组合必须唯一。
        create table tb1(
            nid int not null auto_increment primary key,
            num int null
        )
        或
        create table tb1(
            nid int not null,
            num int not null,
            primary key(nid,num)
        )  
'''
# 外键foreign key
'''
    外键，一个特殊的索引，只能是指定内容
        creat table color(
            nid int not null primary key,
            name char(16) not null
        )

        create table fruit(
            nid int not null primary key,
            smt char(32) null ,
            color_id int not null,
            constraint fk_cc foreign key (color_id) references color(nid)
        )    
 '''
#4,修改表alter
'''
4,修改表 alter
添加列：alter table 表名 add 列名 类型
删除列：alter table 表名 drop column 列名
修改列：
        alter table 表名 modify column 列名 类型;  -- 类型
        alter table 表名 change 原列名 新列名 类型; -- 列名，类型
  
添加主键：
        alter table 表名 add primary key(列名);
删除主键：
        alter table 表名 drop primary key;
        alter table 表名  modify  列名 int, drop primary key;
  
添加外键：alter table 从表 add constraint 外键名称（形如：FK_从表_主表） foreign key 从表(外键字段) references 主表(主键字段);
删除外键：alter table 表名 drop foreign key 外键名称
  
修改默认值：ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
删除默认值：ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;

'''
#三、数据库操作（显示数据库，创建数据库，用户管理，授权管理，特殊的）
# 显示数据库SHOW DATABASES;
'''默认数据库：
　　mysql - 用户权限相关数据
　　test - 用于用户测试数据
　　information_schema - MySQL本身架构相关数据'''
#2、创建数据库 CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci
'''
(-- utf-8)
CREATE DATABASE 数据库名称 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
 
(-- gbk)
CREATE DATABASE 数据库名称 DEFAULT CHARACTER SET gbk COLLATE gbk_chinese_ci;
'''
# 3、使用数据库 USE db_name;
# 显示当前使用的数据库中所有表：SHOW TABLES;
# 4、用户管理
'''创建用户
    create user '用户名'@'IP地址' identified by '密码';
    删除用户
        drop user '用户名'@'IP地址';
    修改用户
        rename user '用户名'@'IP地址'; to '新用户名'@'IP地址';;
    修改密码
        set password for '用户名'@'IP地址' = Password('新密码')
      
    PS：用户权限相关数据保存在mysql数据库的user表中，所以也可以直接对其进行操作（不建议）'''
# 5、授权管理
''' show grants for '用户'@'IP地址'                  -- 查看权限
    grant  权限 on 数据库.表 to   '用户'@'IP地址'      -- 授权
    revoke 权限 on 数据库.表 from '用户'@'IP地址'      -- 取消权限'''
#对于权限
'''
           all privileges  除grant外的所有权限
            select          仅查权限
            select,insert   查和插入权限
            ...
            usage                   无访问权限
            alter                   使用alter table
            alter routine           使用alter procedure和drop procedure
            create                  使用create table
            create routine          使用create procedure
            create temporary tables 使用create temporary tables
            create user             使用create user、drop user、rename user和revoke  all privileges
            create view             使用create view
            delete                  使用delete
            drop                    使用drop table
            execute                 使用call和存储过程
            file                    使用select into outfile 和 load data infile
            grant option            使用grant 和 revoke
            index                   使用index
            insert                  使用insert
            lock tables             使用lock table
            process                 使用show full processlist
            select                  使用select
            show databases          使用show databases
            show view               使用show view
            update                  使用update
            reload                  使用flush
            shutdown                使用mysqladmin shutdown(关闭MySQL)
            super                   􏱂􏰈使用change master、kill、logs、purge、master和set global。还允许mysqladmin􏵗􏵘􏲊􏲋调试登陆
            replication client      服务器位置的访问
            replication slave       由复制从属使用
'''
#对于数据库
''' 对于目标数据库以及内部其他：
    数据库名.*           数据库中的所有
    数据库名.表          指定数据库中的某张表
    数据库名.存储过程     指定数据库中的存储过程
    *.*                所有数据库'''
#对于用户和ID
'''用户名@IP地址         用户只能在改IP下才能访问
    用户名@192.168.1.%   用户只能在改IP段下才能访问(通配符%表示任意)
    用户名@%             用户可以再任意IP下访问(默认IP地址为%)
    
    示例:
    grant all privileges on db1.tb1 TO '用户名'@'IP'
    grant select on db1.* TO '用户名'@'IP'
    grant select,insert on *.* TO '用户名'@'IP'
    revoke select on db1.tb1 from '用户名'@'IP'
    '''
#特殊的：flush privileges，将数据读取到内存中，从而立即生效。
# 忘记密码
'''
# 启动免授权服务端
mysqld --skip-grant-tables
# 客户端
mysql -u root -p
# 修改用户名密码
update mysql.user set authentication_string=password('666') where user='root';
flush privileges;'''