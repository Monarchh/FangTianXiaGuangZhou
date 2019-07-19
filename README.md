
# 分析广州区域出租房屋热点区域

## [点击进入目标网站](https://gz.zu.fang.com/)

### 创建scrapy项目后先用shell调试工具抓取页面信息，页面返回200，可以使用scrapy“爬取”数据

之后再定义Item类，开发Spider类，使用Xpath从页面中提取房屋位置信息，用这些信息来封装Item对象，最后开发Pipeline，处理Spider获取的Item对象，
可以先用print语句测试是否能在终端显示出爬取的数据。成功后再修改pipeline生成json文件，最后用jupyter notebook编写用json文件生成pygal分析图

> * 操作系统：macOS Mojave

> * 时间：2019-7-19

> * 分析结果只代表时间段结果



