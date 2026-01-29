import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


def color_map(color_dict, hex_map, save_path):
    plt.rcParams['font.sans-serif'] = ['SimHei']

    # 加载中国地图数据 (GeoJSON)
    url = "https://geo.datav.aliyun.com/areas_v3/bound/100000_full.json"
    china = gpd.read_file(url)

    # 数据预处理
    # 将颜色数据转为 DataFrame 并匹配颜色值
    df_color = pd.DataFrame(list(color_dict.items()), columns=['name', 'color_name'])
    df_color['hex'] = df_color['color_name'].map(hex_map)

    # 合并地理数据与颜色数据
    china = china.merge(df_color, on='name', how='left')

    # 绘图
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))

    # 绘制背景（处理缺失数据的省份，如台湾省、港澳）
    china.plot(ax=ax, color='#EEEEEE', edgecolor='#666666', linewidth=0.5)

    # 绘制指定颜色的省份
    for color_name, group in china.groupby('color_name'):
        if pd.notna(color_name):
            color_hex = hex_map[color_name]
            group.plot(ax=ax, color=color_hex, edgecolor='#666666', linewidth=0.5, label=color_name)

    # 细节优化
    plt.title('颜色图谱', fontsize=16, pad=20)
    ax.set_axis_off()  # 隐藏坐标轴

    # 制作自定义图例
    from matplotlib.lines import Line2D
    legend_elements = [Line2D([0], [0], marker='s', color='w', label=k,
                            markerfacecolor=v, markersize=15) for k, v in hex_map.items()]
    ax.legend(handles=legend_elements, loc='lower left', title="色彩分类", frameon=False)

    # 保存图片
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"已生成：{save_path}")
    plt.show()