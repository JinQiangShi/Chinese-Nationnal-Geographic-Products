from collections import Counter

SENSORY_DIMENSIONS = {
    "颜色": ["色泽", "颜色", "红", "黄", "绿", "紫", "白", "黑", "透明", "光泽", "亮", "暗", "紫红", "淡黄", "橙黄", "深橙", "青绿", "油润", "黄亮"],
    "气味": ["气味", "香气", "香", "芳香", "芬芳", "清香", "浓郁", "纯正", "辛香", "麻香", "清新", "柔和", "浓烈"],
    "口感": ["口感", "滋味", "鲜", "甜", "酸", "苦", "辣", "咸", "醇", "爽口", "醇和", "鲜美", "微苦", "甜酸", "微带辣", "化渣"],
    "质地": ["皮厚", "薄", "脆", "嫩", "软", "硬", "结实", "弹性", "细腻", "粗糙", "厚实", "肥满", "紧密", "细嫩", "干爽", "挺直"],
    "形态": ["外形", "形状", "圆", "扁", "长", "直", "滑", "匀整", "卵圆", "扁平", "圆筒状", "饱满", "完整", "匀齐", "整洁"]
}

def product_sensory_adj_token_count(products, product_name):
    """
    针对一个产品，统计其感官描述文本中形容词的出现次数。
    """

    adj_tokens = []

    for product in products:
        if product_name in product['product_name']:
            nlp_dict = product['tokenized_sensory_characteristics']
            tok_list = nlp_dict['tok/fine']
            pos_list = nlp_dict['pos/ctb']
            for token, pos in zip(tok_list, pos_list):
                if pos == 'JJ' or pos == 'VA':
                    adj_tokens.append(token)

    return Counter(adj_tokens).most_common()

def province_sensory_adj_tokens(products, province):
    """
    针对一个省份，统计其产品中感官描述文本中形容词的出现次数。
    """

    adj_tokens = []

    for product in products:
        if province in product['province']:
            nlp_dict = product['tokenized_sensory_characteristics']
            tok_list = nlp_dict['tok/fine']
            pos_list = nlp_dict['pos/ctb']
            for token, pos in zip(tok_list, pos_list):
                if pos == 'JJ' or pos == 'VA':
                    adj_tokens.append(token)

    return adj_tokens

def classify_sensory_dimension(token):
    """
    根据关键词判断形容词所属的感官维度
    """
    for dimension, keywords in SENSORY_DIMENSIONS.items():
        for keyword in keywords:
            if keyword in token:
                return dimension
    return None

def count_province_sensory_dimensions(products):
    """
    统计每个省份各感官维度的形容词数量
    """
    province_dimension_count = {}
    
    for product in products:
        province = product.get("province")
        if not province:
            continue
            
        nlp_dict = product.get("tokenized_sensory_characteristics")
        if not nlp_dict:
            continue
            
        tok_list = nlp_dict.get("tok/fine", [])
        pos_list = nlp_dict.get("pos/ctb", [])
        
        if province not in province_dimension_count:
            province_dimension_count[province] = {dim: 0 for dim in SENSORY_DIMENSIONS.keys()}
        
        for token, pos in zip(tok_list, pos_list):
            if pos in ["JJ", "VA"]:
                dimension = classify_sensory_dimension(token)
                if dimension:
                    province_dimension_count[province][dimension] += 1
    
    return province_dimension_count

def normalize_dimension_counts(province_dimension_count):
    """
    对每个维度的数量进行归一化
    """
    normalized_data = {}
    
    dimension_max = {dim: 0 for dim in SENSORY_DIMENSIONS.keys()}
    for province, counts in province_dimension_count.items():
        for dim, count in counts.items():
            dimension_max[dim] = max(dimension_max[dim], count)
    
    for province, counts in province_dimension_count.items():
        normalized_data[province] = {
            dim: count / dimension_max[dim] if dimension_max[dim] > 0 else 0
            for dim, count in counts.items()
        }
    
    return normalized_data

def select_top_provinces(province_dimension_count, top_n=6):
    """
    选择产品数量最多的N个省份
    """
    province_total_count = {
        province: sum(counts.values())
        for province, counts in province_dimension_count.items()
    }
    return sorted(province_total_count.items(), key=lambda x: x[1], reverse=True)[:top_n]