import matplotlib.pyplot as plt
import numpy as np
from count import SENSORY_DIMENSIONS

def plot_sensory_radar_chart(normalized_data, selected_provinces, save_path):
    """
    绘制省份感官特征雷达图

    Parameters:
    -----
        normalized_data (dict): 归一化后的省份感官维度数据
        selected_provinces (list): 选择的省份列表，格式为[(省份名, 产品数量), ...]
        save_path (str): 保存雷达图的文件路径
    """
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    dimensions = list(SENSORY_DIMENSIONS.keys())
    angles = np.linspace(0, 2 * np.pi, len(dimensions), endpoint=False).tolist()
    angles += angles[:1]

    plt.figure(figsize=(10, 10))
    ax = plt.subplot(111, polar=True)

    colors = plt.cm.tab10(np.linspace(0, 1, len(selected_provinces)))

    for idx, (province, _) in enumerate(selected_provinces):
        values = [normalized_data[province][dim] for dim in dimensions]
        values += values[:1]

        ax.plot(angles, values, 'o-', linewidth=2, label=province, color=colors[idx])
        ax.fill(angles, values, alpha=0.25, color=colors[idx])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(dimensions, fontsize=12)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
    ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=10)
    ax.grid(True)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    plt.title('省份感官特征雷达图', fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"雷达图已保存至: {save_path}")
    plt.show()