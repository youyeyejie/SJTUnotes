# Lab4 - MySQL

- [Back to Course Home](index.md)

## MySQL 基础
### 数据库管理 (Database)

- 数据库是一个有组织的数据集合，通常用于存储、管理和检索信息。它可以包含多个表格，每个表格由行和列组成，用于存储相关的数据。数据库广泛应用于各种应用程序和系统中，以便高效地管理大量数据。

- 创建数据库
	```sql
	CREATE DATABASE 数据库名;
	```
	也可以在后面指定字符集和校对规则，确保数据库支持多语言字符。
	```sql
	CREATE DATABASE 数据库名 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
	```

- 删除数据库
	```sql
	DROP DATABASE 数据库名;
	```

- 使用数据库
	```sql
	USE 数据库名;
	```

- 查看所有数据库
	```sql
	SHOW DATABASES;
	```

- 查看当前使用的数据库
	```sql
	SELECT DATABASE();
	```

### 数据表管理 (Table)

- 表是数据库中的基本存储结构，用于组织和存储相关的数据。每个表由行和列组成，行表示记录，列表示字段。表通过定义字段的数据类型和约束来确保数据的完整性和一致性。表之间可以通过外键建立关系，从而实现复杂的数据模型。

- 创建表
	```sql
	CREATE TABLE 表名 (
		字段名1 数据类型 约束,
		字段名2 数据类型 约束,
		...
	);
	```

- 删除表
	```sql
	DROP TABLE 表名;
	```

- 查看所有表
	```sql
	SHOW TABLES;
	```

- 查看表结构
	```sql
	DESCRIBE 表名;
	```

- 常见数据类型

	- 整数类型

		- `TINYINT`：有符号整数类型，取值范围： -128 到 127

		- `TINYINT UNSIGNED`：无符号整数类型，取值范围： 0 到 255

		- `INT`：有符号整数类型，取值范围： -2147483648 到 2147483647

		- `INT UNSIGNED`：无符号整数类型，取值范围： 0 到 4294967295

		- `BIGINT`：有符号大整数类型，取值范围： -9223372036854775808 到 9223372036854775807

		- `BIGINT UNSIGNED`：无符号大整数类型，取值范围： 0 到 18446744073709551615

	- 浮点数类型

		- `FLOAT`：单精度浮点数类型，适用于存储小数

		- `DOUBLE`：双精度浮点数类型，适用于存储更大范围的小数

		- `DECIMAL`：定点数类型，适用于存储精确的小数，常用于财务计算

	- 字符串类型

		- `CHAR(n)`：定长字符串类型，长度为 n

		- `VARCHAR(n)`：变长字符串类型，**最大长度** 为 n

	- 文本类型

		- `TEXT`：大文本类型，适用于存储大量文本数据

		- `TINYTEXT`：小文本类型，适用于存储较小的文本数据

		- `MEDIUMTEXT`：中等文本类型，适用于存储中等量的文本数据

		- `LONGTEXT`：超大文本类型，适用于存储非常大量的文本数据

	- 日期和时间类型

		- `DATE`：日期类型，格式为 'YYYY-MM-DD'

		- `DATETIME`：日期和时间类型，格式为 'YYYY-MM-DD HH:MM:SS'

		- `TIMESTAMP`：时间戳类型，存储自 1970 年 1 月 1 日以来的秒数

		- `TIME`：时间类型，格式为 'HH:MM:SS'

	- 布尔类型

		- `BOOLEAN`：布尔类型，取值为 TRUE 或 FALSE

		- `TINYINT(1)`：通常用于表示布尔值，0 表示 FALSE，非 0 表示 TRUE

- 常见约束

	- `PRIMARY KEY`：主键约束，唯一标识表中的每一行数据

	- `AUTO_INCREMENT`：自动递增约束，通常用于主键

	- `NOT NULL`：非空约束，确保字段不能为空

	- `UNIQUE`：唯一约束，确保字段值唯一

	- `DEFAULT`：默认值约束，为字段指定默认值

	- `FOREIGN KEY`：外键约束，确保字段值在另一个表中存在

- **一般情况下，我们在创建表时都会这样来写**：
	```sql
	create table tb1(
		id int not null auto_increment primary key,
		name varchar(16),
		age int
	) default charset=utf8;
	```
	```
	mysql> desc tb1;
	+-------+-------------+------+-----+---------+----------------+
	| Field | Type		| Null | Key | Default | Extra		  |
	+-------+-------------+------+-----+---------+----------------+
	| id	| int(11)	 | NO   | PRI | NULL	| auto_increment |
	| name  | varchar(16) | YES  |	 | NULL	|				|
	| age   | int(11)	 | YES  |	 | NULL	|				|
	+-------+-------------+------+-----+---------+----------------+
	3 rows in set (0.00 sec)
	```

### 数据行管理

- 行是数据库表中的基本存储单元，表示一条完整的记录。每行由多个字段组成，每个字段对应表中的一个列。行通过主键唯一标识，可以包含各种类型的数据，如整数、字符串、日期等。行之间可以通过外键建立关系，从而实现复杂的数据模型和数据完整性。

- 插入数据
	```sql
	INSERT INTO 表名 (字段1, 字段2, ...) VALUES (值1, 值2, ...);
	INSERT INTO 表名 (字段1, 字段2, ...) VALUES (值1, 值2, ...), (值1, 值2, ...), ...;
	```

- 删除数据
	```sql
	DELETE FROM 表名 WHERE 条件;
	```

- 更新数据
	```sql
	UPDATE 表名 SET 字段=值 WHERE 条件;
	UPDATE 表名 SET 字段1=值1, 字段2=值2, ... WHERE 条件;
	```

- 查询数据
	```sql
	SELECT * FROM 表名;
	SELECT 字段1, 字段2, ... FROM 表名;
	``` 
	也可以添加查询条件
	```sql
	SELECT * FROM 表名 WHERE 条件;
	SELECT 字段1, 字段2, ... FROM 表名 WHERE 条件;
	```

- 常用查询条件

	- `=`：等于

	- `!=` 或 `<>`：不等于

	- `>`：大于

	- `<`：小于

	- `>=`：大于等于

	- `<=`：小于等于

	- `BETWEEN ... AND ...`：在某个范围内

	- `LIKE`：模糊匹配

		- `%`：表示任意数量的字符

		- `_`：表示单个字符

	- `IN`：在某个集合中

	- `IS NULL`：为空

	- `IS NOT NULL`：不为空

- 排序查询结果
	```sql
	SELECT * FROM 表名 ORDER BY 字段 ASC;  -- 升序
	SELECT * FROM 表名 ORDER BY 字段 DESC; -- 降序
	```

- 分页查询
	```sql
	SELECT * FROM 表名 LIMIT 偏移量, 行数;
	```

- 聚合函数

	- `COUNT()`：计算行数

	- `SUM()`：计算总和

	- `AVG()`：计算平均值

	- `MAX()`：计算最大值

	- `MIN()`：计算最小值

- 分组查询
	```sql
	SELECT 字段, 聚合函数(字段) FROM 表名 GROUP BY 字段;
	SELECT 字段, 聚合函数(字段) FROM 表名 GROUP BY 字段 HAVING 条件;
	``` 

- 多表查询

	- 内连接（INNER JOIN）
		```sql
		SELECT * FROM 表1 INNER JOIN 表2 ON 表1.字段 = 表2.字段;
		```

	- 左连接（LEFT JOIN）
		```sql
		SELECT * FROM 表1 LEFT JOIN 表2 ON 表1.字段 = 表2.字段;
		```

	- 右连接（RIGHT JOIN）
		```sql
		SELECT * FROM 表1 RIGHT JOIN 表2 ON 表1.字段 = 表2.字段;
		```

	- 全连接（FULL JOIN）
		```sql
		SELECT * FROM 表1 FULL JOIN 表2 ON 表1.字段 = 表2.字段;
		```

- 子查询
	```sql
	SELECT * FROM 表名 WHERE 字段 IN (SELECT 字段 FROM 另一个表 WHERE 条件);
	```

## 使用 Python 操作 MySQL

- 使用 MySQL 内置工具（命令）

	- 创建数据库：nis3368

	- 数据一张表：admin

		- 表名：admin

		- 列：

			- id，整型，自增，主键

			- username 字符串 不为空

			- password 字符串 不为空

			- mobile 字符串 不为空

- Python 代码实现：

	- 添加用户

	- 删除用户

	- 查看用户

	- 更新用户信息

### 使用 MySQL 内置工具创建表结构

```sql
create database nis3368 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
```

```sql
use nis3368;
```

```sql
create table admin(
	id int not null auto_increment primary key,
	username varchar(16) not null,
	password varchar(64) not null,
	mobile char(11) not null
) default charset=utf8;
```

### 为 Python 安装依赖包
```bash
pip install pymysql
pip install cryptography
```

### 创建数据
```python
import pymysql

## 1.连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="root123", charset='utf8', db='nis3368')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令

## cursor.execute("insert into admin(username,password,mobile) values('刘备','qwe123','15155555555')")

## 防止SQL注入
sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
cursor.execute(sql, ["关羽", "qwe123", "1999999999"])
conn.commit()

## 3.关闭
cursor.close()
conn.close()
```

- 例：从键盘输入用户名、密码和手机号，保存到数据库：

```python
import pymysql

while True:
	user = input("用户名：")
	if user.upper() == 'Q':
		break
	pwd = input("密码：")
	mobile = input("手机号：")

	# 1.连接MySQL
	conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="root123", charset='utf8', db='nis3368')
	cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

	# 2.发送指令（千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入）
	sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
	cursor.execute(sql, [user, pwd, mobile])
	conn.commit()

	# 3.关闭
	cursor.close()
	conn.close()
```

### 查询数据
```python
import pymysql

## 1.连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="root123", charset='utf8', db='nis3368')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令（ *** 千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入***）
cursor.execute("select * from admin where id > %s", [2, ])

## 获取符合条件的所有数据，得到的是 [字典,字典,···]/空列表
data_list = cursor.fetchall()
for row_dict in data_list:
	print(row_dict) # {'id': 3, 'username': '集宁', 'password': 'qwe123', 'mobile': '1999999999'}

## 获取符合条件的第一条数据，字典/None
res = cursor.fetchone()
print(res)  # {'id': 3, 'username': '集宁', 'password': 'qwe123', 'mobile': '1999999999'}

## 3.关闭连接
cursor.close()
conn.close()
```

### 修改数据

- 例：将 id=7 的用户的手机号改为 1888888888

```python
import pymysql

## 1.连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="root123", charset='utf8', db='nis3368')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令（ *** 千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入***）
#将id=7的用户的手机号改为1888888888
cursor.execute("update admin set mobile=%s where id=%s", ["1888888888", 7, ])
conn.commit()

## 3.关闭
cursor.close()
conn.close()
```

### 删除数据

- 将 id=3 的用户删除

```python
import pymysql

## 1.连接MySQL
conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd="root123", charset='utf8', db='nis3368')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

## 2.发送指令（ *** 千万不要用字符串格式化去做SQL的拼接，安全隐患SQL注入***）
cursor.execute("delete from admin where id=%s", [3, ])
conn.commit()

## 3.关闭
cursor.close()
conn.close()
```

### 注意事项

- 在进行 新增、删除、修改时，一定要记得 `commit`，不然数据库没有数据。
	```python
	cursor.execute("..")
	conn.commit()
	```

- 在查询时，不需要 `commit`，执行 `fetchall` / `fetchone`
	```
	cursor.execute("...")

	# 第一条数据，字典，无数据时是空列表
	v1 = cursor.fetchone()

	# 所有数据，列表套字典，无数据时是None
	v1 = cursor.fetchall()
	```

- 对于 SQL 语句不要用 Python 的字符串格式化进行拼接（会被 SQL 注入），一定要用 `execute` + 参数
	```python
	cursor.execute(".%s..... %s", ["xx","xx"])
	```