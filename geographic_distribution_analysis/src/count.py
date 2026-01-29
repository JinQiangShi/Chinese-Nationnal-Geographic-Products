from math import nan
from collections import Counter
from .__init__ import CHINA_PROVINCES

def products_count_province_level(products):
    """
    统计产品在每个省份的出现次数
    """
    count = []
    for product in products:
        if product.get("province"):
            count.append(product["province"])
    return Counter(count).most_common()

def products_count_city_level(products):
    """
    统计产品在每个城市的出现次数
    """
    count = []
    for product in products:
        if product.get("city"):
            count.append(product["city"])
    return Counter(count).most_common()

def product_name_NN_token_count(products):
    """
    统计产品名称分词后的普通名词NN出现的次数
    """
    tokens_count = []

    for product in products:
        nlp_dict = product['tokenized_product_name']
        tok_list = nlp_dict['tok/fine']
        pos_list = nlp_dict['pos/ctb']

        for tok, pos in zip(tok_list, pos_list):
            if pos == "NN":
                tokens_count.append(tok)

    return Counter(tokens_count).most_common()

def name_in_product_name_count_provice_level(products, name):
    """
    统计产品名称中包含指定名称的产品在每个省份的出现次数, 并补全不在products中的省份, 默认为nan
    """
    # 统计产品名称中包含指定名称的产品在每个省份的出现次数
    name_count = Counter(p["province"] for p in products if name in p.get("product_name")).most_common()
    # 补全不在name_count_province_level中的省份, 默认为nan
    for province in CHINA_PROVINCES:
        if province not in name_count:
            name_count.append((province, nan))
    return name_count

def product_name_NN_token_count_province_level(products, province):
    """
    统计产品名称分词后的普通名词NN在指定省份的出现次数
    """
    tokens_count = []

    province_products = [p for p in products if province == p.get("province")]

    for product in province_products:
        nlp_dict = product['tokenized_product_name']
        tok_list = nlp_dict['tok/fine']
        pos_list = nlp_dict['pos/ctb']

        for tok, pos in zip(tok_list, pos_list):
            if pos == "NN":
                tokens_count.append(tok)

    return Counter(tokens_count).most_common()


def product_name_NN_token_count_city_level(products, city):
    """
    统计产品名称分词后的普通名词NN在指定城市的出现次数
    """
    tokens_count = []

    city_products = [p for p in products if city == p.get("city")]

    for product in city_products:
        nlp_dict = product['tokenized_product_name']
        tok_list = nlp_dict['tok/fine']
        pos_list = nlp_dict['pos/ctb']

        for tok, pos in zip(tok_list, pos_list):
            if pos == "NN":
                tokens_count.append(tok)

    return Counter(tokens_count).most_common()