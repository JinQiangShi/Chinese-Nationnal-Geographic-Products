from math import nan
from collections import Counter

CHINA_PROVINCES = {
    "北京市", "天津市", "上海市", "重庆市",
    "河北省", "山西省", "辽宁省", "吉林省", "黑龙江省",
    "江苏省", "浙江省", "安徽省", "福建省", "江西省",
    "山东省", "河南省", "湖北省", "湖南省", "广东省",
    "海南省", "四川省", "贵州省", "云南省", "陕西省",
    "甘肃省", "青海省", "台湾省",
    "内蒙古自治区", "广西壮族自治区", "西藏自治区",
    "宁夏回族自治区", "新疆维吾尔自治区",
    "香港特别行政区", "澳门特别行政区"
}

def product_count_province_level(products):
    """
    统计产品在每个省份的出现次数
    """
    return Counter(p["province"] for p in products if p.get("province")).most_common()

def product_count_city_level(products):
    """
    统计产品在每个的出现次数
    """
    return Counter(p["city"] for p in products if p.get("city")).most_common()

def name_count_provice_level(products, name):
    """
    统计产品名称中包含指定名称的产品在每个省份的出现次数, 并补全不在products中的省份, 默认数量为0
    """
    # 统计产品名称中包含指定名称的产品在每个省份的出现次数
    name_count = Counter(p["province"] for p in products if name in p.get("product_name")).most_common()
    # 补全不在name_count_province_level中的省份, 默认为nan
    for province in CHINA_PROVINCES:
        if province not in name_count:
            name_count.append((province, nan))
    return name_count

def product_name_list_province_level(products, province):
    """
    返回指定省份的产品名称列表
    """
    return [p["product_name"] for p in products if province == p.get("province")]

def product_name_list_city_level(products, city):
    """
    返回指定城市的产品名称列表
    """
    return [p["product_name"] for p in products if city == p.get("city")]

