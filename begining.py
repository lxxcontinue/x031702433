import jieba
import re
import cpca

origin_data=[]
origin_data.append("李四,福建省福州13756899511市鼓楼区鼓西街道湖滨路110号湖滨大厦一层")
origin_data.append("张三,福建福州闽13599622362侯县上街镇福州大学10#111")
origin_data.append("王五,福建省福州市鼓楼18960221533区五一北路123号福州鼓楼医院")
origin_data.append("小美,北京市东15822153326城区交道口东大街1号北京市东城区人民法院")
origin_data.append("小陈,广东省东莞市凤岗13965231525镇凤平路13号")



def sortInfo(origin_address):


    return


# 原始数据
origin_address = "小美,北京市东15822153326城区交道口东大街1号北京市东城区人民法院"
print(origin_address)

info = {}

# 切分数据
firstCut_list = jieba.lcut(origin_address)

# 去除名字和逗号
sorted_name = firstCut_list[0]
info["姓名"] = sorted_name
del firstCut_list[0]
del firstCut_list[0]

# 提取出电话号码
for first_value in firstCut_list:
    phone = re.compile('^0\\d{2,3}\\d{7,8}$|^1[358]\\d{9}$|^147\\d{8}')
    phonematch = phone.match(first_value)
    if phonematch:
        info["手机"] = phonematch.group()
        del firstCut_list[firstCut_list.index(first_value)]
        break

# 重新合成地址
firstSorted_address = ''
for second_list in firstCut_list:
    firstSorted_address += second_list

# 切分并填充地址
location_str = [firstSorted_address]

df = cpca.transform(location_str)

newAddr = []
secondCut_list = df.values[0]
for second_list in secondCut_list:
    newAddr.append(second_list)

info["地址"] = newAddr
print(origin_address)
print(info)
