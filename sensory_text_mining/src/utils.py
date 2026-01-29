import numpy as np

def counter_most_common_list_to_dict(counter_most_common_list:list[tuple], scale="linear"):
    """
    将Counter.most_common()返回的列表转换为字典
    """
    item_dict = {}
    for item, count in counter_most_common_list:
        if scale == "linear":
            item_dict[item] = count
        if scale == "log":
            item_dict[item] = np.log(count)
        if scale == "square":
            item_dict[item] = count ** 1.5
    return item_dict

def province_list(products):
    """
    从产品列表中提取所有出现的省份
    """
    province_set = set()
    for product in products:
        if product.get("province"):
            province_set.add(product["province"])
    return list(province_set)