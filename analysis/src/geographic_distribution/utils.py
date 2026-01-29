def counter_most_common_list_to_dict(counter_most_common_list:list[tuple]):
    """
    将Counter.most_common()返回的列表转换为字典
    """
    item_dict = {}
    for item, count in counter_most_common_list:
        item_dict[item] = count
    return item_dict