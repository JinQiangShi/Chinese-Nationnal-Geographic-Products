import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

PRODUCT_CATEGORIES = {
    "茶类": ["茶", "茗", "普洱", "龙井", "碧螺春", "毛尖", "铁观音"],
    "水果类": ["苹果", "梨", "桃", "李", "杏", "枣", "柑", "橘", "橙", "柠檬", "荔枝", "芒果", "菠萝", "草莓", "樱桃", "猕猴桃", "葡萄", "西瓜", "瓜"],
    "坚果类": ["核桃", "板栗", "花生", "杏仁", "腰果", "开心果", "榛子", "松子", "瓜子"],
    "谷物类": ["米", "麦", "稻", "玉米", "高粱", "大豆", "绿豆", "红豆", "蚕豆", "豌豆", "荞麦", "燕麦"],
    "蔬菜类": ["茄", "辣椒", "土豆", "红薯", "山药", "藕", "笋", "姜", "蒜", "葱", "萝卜", "白菜", "菠菜", "芹菜", "菜薹"],
    "肉类": ["猪", "牛", "羊", "鸡", "鸭", "鹅", "肉", "腊", "烧鸡", "火腿"],
    "水产类": ["鱼", "虾", "蟹", "贝", "鲍鱼", "海参", "蚝", "鳗", "鳝", "鲤", "鲫", "鲢"],
    "调味品类": ["酱", "醋", "油", "糖", "盐", "花椒", "八角", "桂皮", "丁香", "豆瓣"],
    "酒类": ["酒", "白酒", "黄酒", "啤酒", "葡萄酒"],
    "药材类": ["参", "药", "当归", "黄芪", "枸杞", "灵芝", "茯苓", "厚朴", "乌药", "金银花"],
    "其他类": []
}

def classify_product(product_name):
    """
    根据产品名称判断所属类别
    """
    for category, keywords in PRODUCT_CATEGORIES.items():
        if category == "其他类":
            continue
        for keyword in keywords:
            if keyword in product_name:
                return category
    return "其他类"

def count_product_categories(products):
    """
    统计每个类别的产品数量
    """
    category_count = {category: 0 for category in PRODUCT_CATEGORIES.keys()}
    
    for product in products:
        product_name = product.get("product_name", "")
        category = classify_product(product_name)
        category_count[category] += 1
    
    return category_count

def calculate_category_percentage(category_count):
    """
    计算每个类别的占比
    """
    total = sum(category_count.values())
    category_percentage = {
        category: count / total * 100
        for category, count in category_count.items()
    }
    return category_percentage

def plot_product_category_pie_chart(category_count, save_path, chart_type="pie"):
    """
    绘制产品类别分布饼图或环形图

    Parameters:
    -----
        category_count (dict): 各类别的产品数量
        save_path (str): 保存图表的文件路径
        chart_type (str): "pie" 或 "donut"
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    categories = list(category_count.keys())
    counts = list(category_count.values())
    
    filtered_data = [(cat, count) for cat, count in zip(categories, counts) if count > 0]
    if not filtered_data:
        print("没有数据可绘制")
        return
    
    categories, counts = zip(*filtered_data)
    
    total = sum(counts)
    percentages = [count / total * 100 for count in counts]
    
    colors = plt.cm.Set3(np.linspace(0, 1, len(categories)))
    
    if chart_type == "pie":
        plt.figure(figsize=(10, 10))
        wedges, texts, autotexts = plt.pie(
            counts,
            labels=categories,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90,
            textprops={'fontsize': 12}
        )
        plt.title('产品类别分布饼图', fontsize=16, pad=20)
        
    elif chart_type == "donut":
        plt.figure(figsize=(10, 10))
        wedges, texts, autotexts = plt.pie(
            counts,
            labels=categories,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90,
            pctdistance=0.85,
            textprops={'fontsize': 12}
        )
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        plt.title('产品类别分布环形图', fontsize=16, pad=20)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"{chart_type}图已保存至: {save_path}")
    plt.show()