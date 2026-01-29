from collections import Counter

def product_sensort_adj_token_count(products, product_name):
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
