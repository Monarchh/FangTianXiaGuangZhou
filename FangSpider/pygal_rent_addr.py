import json
import pygal

# 将文件定义为变量filename
filename = 'rent_address.json'
# 读取JSON格式的工作数据
with open (filename, 'r', True, 'utf-8') as f:
    addr_list = json.load(f)

# 定义addr_dict来保存房子所在地区的位数
addr_dict = {}

# 遍历列表的每个元素，每个元素都是一个地区信息
for addr in addr_list:
    if addr['address'] in addr_dict:
        addr_dict[addr['address']] += 1
    else:
        addr_dict[addr['address']] = 1

# 创建pygal.Pie对象（饼图）
pie = pygal.Pie()
other_num = 0

# 采用循环为饼图添加数据
for k in addr_dict.keys():
    # 如果该行业的招聘位数少于5个，则归类到“其它”中
    if addr_dict[k] < 5:
        other_num += addr_dict[k]
    else:
        pie.add(k, addr_dict[k])

# 添加其它行业的招聘职位数
pie.add('其它', other_num)
pie.title = '广州出租房屋热点区域'
# 设置将图例放到底部
pie.legend_at_bottom = True
# 指定将数据图输出到SVG文件中
pie.render_to_file('rent_addr.svg')