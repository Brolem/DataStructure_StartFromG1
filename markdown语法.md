**标题**：用#来表示，#越多，级别越低
## 二级标题
### 三级标题

---
**加粗、斜体**：用星号*包裹文字
- **加粗**
- *斜体*
- ***加粗斜体***

---
1. **列表**：用-或+表示无序列表，用数字加点表示有序列表
- 无序列表项1
- 无序列表项2
1. 有序列表项1
   1. 有序列表项1.1
      1. 有序列表项1.1.1
   2. 有序列表项1.2
2. 有序列表项2

---
**引用**：用>表示，可以嵌套使用
- >这是一段引用
- >>这是嵌套的引用

---
 **代码块**：用反引号`包裹代码，可以指定语言，如python
- ``print("Hello, world!")``用一对`或``包裹是内联代码
- 用三个反引号```包裹代码块，还可以指定语言，如python
```python
print("Hello, world!")
```
- {.line-numbers}添加代码行数
```python{.line-numbers}
print("Hello, world!")
```

---
**导入文件**：用[]和()组合或顶格@import
- [百度](https://www.baidu.com)
- ![图片alt文本](https://ts3.tc.mm.bing.net/th/id/OIP-C.LiXZw0doNJZ7Gvlqf6xZcwHaHa?rs=1&pid=ImgDetMain&o=7&rm=3)

@import "README.md"
![](README.md)


---
**删除线**：用~~包裹文字
- ~~删除线~~


---
**分割线**：用三个或以上的-、*或_
- ***
- ___


---
**任务列表**
- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item


---
**表格**
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column


---
**上标**：30^th^
**下标**：H~2~O

**高亮**：==highlight==

**缩写**
*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium
The HTML specification is maintained by the W3C.


---
**数学**
- $f(x) = sin(x) + 12$ 或者 \(f(x) = sin(x) + 12\) 中的数学表达式将会在行内显示
- $$\sum_{n=1}^{100} x_n$$ 或者 \[\sum_{n=1}^{100} x_n\] 或者 ```math 中的数学表达式将会在块内显示


---
**脚注**：Content [^1][^2]
[^1]: Hi! This is a footnote.
[^2]: Hi! This also is a footnote.