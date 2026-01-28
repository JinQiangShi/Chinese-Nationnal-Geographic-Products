from collections import Counter
from math import nan
from .heatmap import province_heatmap_plot
from .bar import province_bar_plot


def get_product_province_count(products, name):
    """
    统计产品在每个省份的出现次数
    """
    return Counter(p["province"] for p in products if name in p.get("product_name")).most_common()

def complete_product_province_count(product_province_count):
    """
    补全不在product_province_dict中的省份, 默认数量为0
    """

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

    for province in CHINA_PROVINCES:
        if province not in product_province_count:
            product_province_count.append((province, nan))
    
    return product_province_count

def get_complete_product_province_count(products, name):
    """
    统计产品在每个省份的出现次数, 并补全不在products中的省份, 默认数量为0
    """
    product_province_count = get_product_province_count(products, name)
    return complete_product_province_count(product_province_count)