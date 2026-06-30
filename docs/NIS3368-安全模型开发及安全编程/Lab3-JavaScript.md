# Lab3 - JavaScript

- [Back to Course Home](index.md)

## JavaScript 应用方式

- 当前 HTML 中。
	```html
	<script type="text/javascript">
		// 编写JavaScript代码
	</script>
	```

- 在其他 js 文件中，导入使用。
	```html
	<script src="static/my.js"></script>
	```

## JavaScript 能够以不同方式显示数据：

- 使用 `alert()` 写入警告框 (见上例)

- 使用 `document.write()` 写入 HTML 输出 （只能在测试阶段使用，不建议）

- 使用 `innerHTML` 写入 HTML 元素

- 使用 `console.log()` 写入浏览器控制台

## JavaScript 基础
### 变量

- 声明变量

	- `var`：全局变量，函数内的局部变量

	- `let`：块级作用域变量，声明时可以不初始化，值可以改变

	- `const`：常量，块级作用域变量，声明时必须初始化，且值不能改变

```javascript
	var name = "张三";
	console.log(name);
```

### 字符串类型
```javascript
// 声明
var name = "上海交通大学";

var v1 = name.length;
var v2 = name[0];   // name.charAt(3)
var v3 = name.trim(); //删除字符串两端的空白符：
var v4 = name.substring(0,2); // 前取后不取
```

- 案例：跑马灯

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
	<style>
		span{
			font-size: 30px;
			color: blue;
		}
	</style>  
</head>
<body>

<span id="txt">欢迎访问我的主页</span>

<script type="text/javascript">
	function show() {
		// 1.去HTML中找到某个标签并获取他的内容（DOM）
		var tag = document.getElementById("txt");
		var dataString = tag.innerText;

		// 2.动态起来，把文本中的第一个字符放在字符串的最后面。
		var firstChar = dataString[0];
		var otherString = dataString.substring(1, dataString.length);
		var newText = otherString + firstChar;

		// 3.在HTML标签中更新内容
		tag.innerText = newText;
	}

	// JavaScript中的定时器，如：每1s执行一次show函数。
	setInterval(show, 1000);
</script>
</body>
</html>
```

### 数组
```javascript
// 定义
var v1 = [11,22,33,44];
var v2 = Array([11,22,33,44]);

// 操作
v1[0] = "张三";

v1.push("上海交通大学");		// 尾部追加 [`张三`, 22, 33, 44, `上海交通大学`]
v1.unshift("计算机学院");	   // 头部追加 ['计算机学院', '张三', 22, 33, 44, '上海交通大学']
// v1.splice(索引位置,0,元素);  // 0 表示追加
v1.splice(1,0,"中国");		  // 尾部追加 ['计算机学院', '中国', '张三'，22, 33, 44]
v1.pop();					   // 尾部删除 [`计算机学院`, `中国`, `张三`, 22, 33]
v1.shift();					 // 头部删除 [`中国`, `张三`, 22, 33]
// v1.splice(索引位置,1);		// 1 表示删除
v1.splice(2,1);				 // 索引为2的元素删除 [`中国`, `张三`, 33]

var v1 = [11,22,33,44];
for(var idx in v1){
	// idx=0/1/2/3/	data=v1[idx]
}
for(var i=0; i<v1.length; i++){
	// i=0/1/2/3   data=v1[idx]
}
```

- 案例：动态数据

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
	<ul id="city">
		<!-- <li>北京</li> -->
	</ul>

	<script type="text/javascript">

		// 发送网络请求，获取数据 cityList
		var cityList = ["北京","上海","深圳"];

		// 遍历数据，创建HTML标签，添加到页面中
		for(var idx in cityList){
			var text = cityList[idx];

			// 创建 <li></li>
			var tag = document.createElement("li");
			// 在li标签中写入内容
			tag.innerText = text;

			// 添加到id=city那个标签的里面。DOM
			var parentTag = document.getElementById("city");
			parentTag.appendChild(tag);
		}
	</script>
</body>
</html>
```

### 字典
```javascript
// 添加字典数据
info = {
	"name":"张三",
	"age":18
}
info = {
	name:"张三",
	age:18
}

// 读取字典数据
var age = info.age

// 修改字典数据
info.name = "李四"
info["name"] = "李四"

// 删除字典数据
delete info["age"]

for(var key in info){
	// key=name/age	  data=info[key]
}
```

- 案例：动态表格

	- 单行数据：字典数据读取

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
	</head>
	<body>
	<table border="1">
		<thead>
		<tr>
			<th>ID</th>
			<th>姓名</th>
			<th>年龄</th>
		</tr>
		</thead>
		<tbody id="body">

		</tbody>
	</table>

	<script type="text/javascript">
		// 网络请求获取，写入到页面上。
		// 模拟数据
		var info = {id: 1, name: "李四", age: 19};
		// 创建 <tr></tr>
		var tr = document.createElement("tr");
		for (var key in info) {
			// 在tr标签中写入内容
			var text = info[key];
			var td = document.createElement('td');
			td.innerText = text;
			tr.appendChild(td);
		}
		// 添加到id=body那个标签的里面。DOM
		var bodyTag = document.getElementById("body");
		bodyTag.appendChild(tr);

	</script>
	</body>
	</html>
	```

	- 多行数据表格：字典列表数据读取

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>Title</title>
	</head>
	<body>
		<table border="1">
			<thead>
			<tr>
				<th>ID</th>
				<th>姓名</th>
				<th>年龄</th>
			</tr>
			</thead>
			<tbody id="body">

			</tbody>
		</table>

		<script type="text/javascript">

			// 网络请求获取，写入到页面上。
			// 模拟数据
			var dataList = [
				{id: 1, name: "李四1", age: 19},
				{id: 2, name: "李四2", age: 19},
				{id: 3, name: "李四3", age: 19},
				{id: 4, name: "李四4", age: 19},
				{id: 5, name: "李四5", age: 19},
			];

			// 遍历数据，创建HTML标签，添加到页面中
			for (var idx in dataList) {
				var info = dataList[idx];
				// 创建 <tr></tr>
				var tr = document.createElement("tr");

				for (var key in info) {
					// 在tr标签中写入内容
					var text = info[key];
					var td = document.createElement('td');
					td.innerText = text;
					tr.appendChild(td);
				}

				// 添加到id=body那个标签的里面。DOM
				var bodyTag = document.getElementById("body");
				bodyTag.appendChild(tr);
			}

		</script>
	</body>
	</html>
	```

### 条件语句

```javascript
if ( 条件 )  {
	// 条件成立执行的代码
}else if ( 条件 ){
	// 条件成立执行的代码
}else{
	// 条件不成立执行的代码
}
```

### 函数

```javascript
// 定义函数
function func(){
	// 函数体
}

// 调用函数
func()
```

## DOM

DOM 是 Document Object Model（文档对象模型）的缩写，是一种用于表示和操作 HTML 和 XML 文档的编程接口。DOM 将文档表示为一个树状结构，其中每个节点代表文档的一部分，如元素、属性和文本内容。通过 DOM，开发者可以动态地访问和修改网页的内容、结构和样式，从而实现交互性和动态效果。

### DOM 常用操作

- 获取元素

	- `document.getElementById("id")`：通过 ID 获取元素

	- `document.getElementsByClassName("class")`：通过类名获取元素集合

	- `document.getElementsByTagName("tag")`：通过标签名获取元素集合

	- `document.querySelector("selector")`：通过 CSS 选择器获取第一个匹配的元素

	- `document.querySelectorAll("selector")`：通过 CSS 选择器获取所有匹配的元素集合

- 创建和删除元素

	- `document.createElement("tag")`：创建一个新的元素

	- `parentElement.appendChild(childElement)`：将子元素添加到父元素中

	- `parentElement.removeChild(childElement)`：从父元素中移除子元素

- 修改元素内容

	- `element.innerText`：获取或设置元素的文本内容

	- `element.innerHTML`：获取或设置元素的 HTML 内容

	- `element.textContent`：获取或设置元素的文本内容（包括隐藏的文本）

- 修改元素属性

	- `element.getAttribute("attr")`：获取元素的属性值

	- `element.setAttribute("attr", "value")`：设置元素的属性值

	- `element.removeAttribute("attr")`：移除元素的属性

- 修改元素样式

	- `element.style.property`：获取或设置元素的内联样式属性

- 事件处理

	- `element.addEventListener("event", function)`：为元素添加事件监听器

	- `element.removeEventListener("event", function)`：移除元素的事件监听器

	- `element.onclick = function`：为元素添加点击事件处理函数

- 遍历元素

	- `element.parentNode`：获取元素的父节点

	- `element.childNodes`：获取元素的所有子节点集合

	- `element.firstChild`：获取元素的第一个子节点

	- `element.lastChild`：获取元素的最后一个子节点

	- `element.nextSibling`：获取元素的下一个兄弟节点

	- `element.previousSibling`：获取元素的上一个兄弟节点

- 表单操作

	- `formElement.elements`：获取表单中的所有元素集合

	- `inputElement.value`：获取或设置输入元素的值

	- `selectElement.selectedIndex`：获取或设置选择元素的选中索引

	- `checkboxElement.checked`：获取或设置复选框的选中状态

- 文档操作

	- `document.title`：获取或设置文档的标题

	- `document.body`：获取文档的主体元素

	- `document.head`：获取文档的头部元素

### 使用 DOM 进行事件的绑定

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
	<input type="button" value="点击添加" onclick="addCityInfo()">
	<ul id="city">
		<li>北京</li>
	</ul>
	<script type="text/javascript">
		function addCityInfo() {
			var newTag = document.createElement("li");
			newTag.innerText = "上海";
			var parentTag = document.getElementById("city");
			parentTag.appendChild(newTag);
		}
	</script>
</body>
</html>
```

### 事件监听器 (addEventListener)

```javascript
document.getElementById("btnAdd").addEventListener("click", function() {
	var txtTag = document.getElementById("txtUser");
	var newString = txtTag.value;

	if (newString.length > 0) {
		var newTag = document.createElement("li");
		newTag.innerText = newString;
		var parentTag = document.getElementById("city");
		parentTag.appendChild(newTag);
		txtTag.value = "";
	} else {
		alert("输入不能为空");
	}
});
```

## jQuery

jQuery 是一个快速、小巧且功能丰富的 JavaScript 库。它简化了 HTML 文档遍历和操作、事件处理、动画以及 Ajax 交互，使得开发者能够更轻松地编写跨浏览器兼容的代码。

### 引入 jQuery
```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

### jQuery 选择器

- 基本语法：`$(selector).action()`

- 选择器示例:

	- `$("selector")`：通过 CSS 选择器选择元素

		- `$("#id")`:通过 ID 选择元素

		- `$(".class")`：通过类名选择元素   

		- `$("tag")`:通过标签名选择元素

		- `$("div > .class")` 选择所有 div 下的 class 类元素

		- `$("input[name='n1']")`:选择所有 name 属性为 n1 的 input 元素

	- `$(this)`：选择当前元素

	- `$("*")`:选择所有元素

	- 多选择器

		- `$("#id, .class, tag")`：选择多个不同的元素

	- 过滤器

		- `$("div").filter(".class")`:选择所有 div 中带有 class 类的元素

### 间接寻找

- `$(parent).find("selector")`：在父元素中查找子元素

- `$(child).parent()`:获取子元素的父元素

- `$(sibling).next()`：获取兄弟元素中的下一个元素

- `$(sibling).prev()`:获取兄弟元素中的上一个元素

- `$(element).children("selector")`：获取元素的所有子元素

- `$(element).closest("selector")`:获取元素的最近的祖先元素

### 操作样式

- `$(element).css("property", "value")`：设置元素的样式属性

- `$(element).addClass("class")`:为元素添加类

- `$(element).removeClass("class")`：为元素移除类

- `$(element).toggleClass("class")`：切换元素的类

- 案例：菜单的切换

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
	<style>
		.menus{
			width: 200px;
			height: 800px;
			border: 1px solid red;
		}
		.menus .header{
			background-color: gold;
			padding: 10px 5px;
			border-bottom: 1px dotted #dddddd;
		}
		.menus .content a{
			display: block;
			padding: 5px 5px;
			border-bottom: 1px dotted #dddddd;
		}

		.hide{
			display: none;
		}
	</style>
</head>
<body>
	<div class="menus">
		<div class="item">
			<div class="header" onclick="clickMe(this);">上海</div>
			<div class="content hide">
				<a>宝山区</a>
				<a>青浦区</a>
				<a>浦东新区</a>
				<a>普陀区</a>
			</div>
		</div>

		<div class="item">
			<div class="header" onclick="clickMe(this);">北京</div>
			<div class="content hide">
				<a>海淀区</a>
				<a>朝阳区</a>
				<a>大兴区</a>
				<a>昌平区</a>
			</div>
		</div>
	</div>

	<script src="static/jquery-3.6.0.min.js"></script>
	<script>
		function clickMe(self) {
			// $(self)  -> 表示当前点击的那个标签。
			// $(self).next() 下一个标签
			// $(self).next().removeClass("hide");   删除样式

			// 让自己下面的功能展示出来/隐藏
			/*var hasHide = $(self).next().hasClass("hide");
			if(hasHide){
				$(self).next().removeClass("hide");
			}else{
				$(self).next().addClass("hide");
			} */

			// 让自己下面的功能展示出来
			$(self).next().removeClass("hide");

			// 找父亲，父亲的所有兄弟，再去每个兄弟的子孙中寻找 class=content，添加hide样式
			$(self).parent().siblings().find(".content").addClass("hide");
		}
	</script>
</body>
</html>
```

### 值的操作

- `$(element).text()`:获取元素的文本内容

- `$(element).text("value")`：设置元素的文本内容

- `$(element).val()`:获取表单元素的值

- `$(element).val("value")`：设置表单元素的值

- 案例：动态创建数据

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<input type="text" id="txtUser" placeholder="用户名">
<input type="text" id="txtEmail" placeholder="邮箱">
<input type="button" value="提交" onclick="getInfo()"/>

<ul id="view">
</ul>

<script src="static/jquery-3.6.0.min.js"></script>
<script>
	function getInfo() {
		// 1.获取用户输入的用户名和密码
		var username = $("#txtUser").val();
		var email = $("#txtEmail").val();
		var dataString = username + " - " + email;

		// 2.创建li标签，在li的内部写入内容。 <li>：创建li标签
		var newLi = $("<li>").text(dataString);

		// 3.把新创建的li标签添加到ul里面。
		$("#view").append(newLi);
	}

</script>
</body>
</html>
```

### 绑定事件

- `$(element).on("event", function)`:为元素绑定事件处理函数

- `$(element).off("event", function)`：移除元素的事件处理函数

- `$(element).click(function)`:为元素绑定点击事件处理函数

- `$(element).dblclick(function)`：为元素绑定双击事件处理函数

- `$(element).hover(function1, function2)`:为元素绑定鼠标悬停和离开事件处理函数

- `$(element).remove()`：移除元素

- 为了让页面框架加载完成之后立即执行代码：在 script 中添加声明 `$(function(){})`

- 案例：自动删除

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Title</title>
</head>
<body>
<ul>
	<li>百度</li>
	<li>谷歌</li>
	<li>搜狗</li>
</ul>

<script src="static/jquery-3.6.0.min.js"></script>
<script>
	$(function () {
		// 当页面的框架加载完成之后，自动就执行。
		$("li").click(function () {
			$(this).remove();
		});

	});
</script>
</body>
</html>
```