import matplotlib.pyplot as plt

def province_bar_plot(
    sorted_provinces:list[tuple], 
    save_path:str
    ):
    """
    绘制中国省份级别地理标志产品数量的柱状图

    Parameters:
    -----
        sorted_provinces (list of tuple): 包含省份和产品数量的元组列表。
        save_path (str): 保存柱状图的文件路径。
    """
    # 支持中文显示
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 提取省份和数量
    provinces, counts = zip(*sorted_provinces)

    # 创建柱状图
    plt.figure(figsize=(14, 8))
    barh = plt.barh(provinces, counts, height=0.8)
    plt.bar_label(barh, counts)
    plt.title("地理标志产品数量分布柱状图", size=18)
    plt.xlabel("产品数量", size=16)
    plt.ylabel("省份", size=16)
    plt.tight_layout()
    plt.savefig(save_path, dpi=500)
    print(f"柱状图已保存至: {save_path}")
    plt.show()