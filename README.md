# 中国国家地理标志产品

我们根据中国国家地理标志产品的官网公告，构建了适用于数据分析、数据可视化和文本挖掘的中国国家地理标志产品数据库。

我们根据该数据库，进行了一些数据分析和可视化的项目。

> 截止2026年1月，在中国国家地理标志产品领域，该数据库是全网最新、最全、最适用于数据分析项目的。

## 项目概述

中国国家地理标志产品是指产自特定地域，所具有的质量、声誉或其他特性本质上取决于该产地的自然因素和人文因素，经审核批准以地理名称进行命名的产品。

本项目对官方发布的地理标志保护产品批准公告进行了系统性的数据收集和分析。

## 项目结构

```
Chinese-National-Geographic-Products/
├── data/                           # 数据目录
│   ├── origin/                     # 原始PDF公告文件
│   ├── extract/                   # 提取的JSON数据
│   ├── polish/                    # 润色后的JSON数据
│   ├── products.json              # 最终产品数据
│   ├── tokenized_products.json    # 分词后的产品数据
│   ├── log.txt                    # 公告日志
│   ├── 下载公告.ipynb             # 数据下载notebook
│   ├── 提取信息.ipynb             # 信息提取notebook
│   ├── 数据预处理.ipynb           # 数据预处理notebook
│   ├── 文本润色.ipynb             # 文本润色notebook
│   └── 自然语言处理.ipynb         # 自然语言处理notebook
├── geographic_distribution_analysis/  # 地理分布分析模块
│   ├── src/                       # 源代码
│   ├── figures/                   # 输出图表
│   └── main.ipynb                 # 地理分布分析notebook
├── sensory_text_mining/           # 感官文本挖掘模块
│   ├── src/                       # 源代码
│   ├── figures/                   # 输出图表
│   └── main.ipynb                 # 感官文本挖掘notebook
├── README.md                     # 项目介绍
├── 技术报告.md                   # 项目技术报告
└── LICENSE
```

## 数据模块

我们从中国国家地理标志产品检索网站（https://ggfw.cnipa.gov.cn/dlbzsq/dbQuery）收集了2005年至2023年的地理标志保护产品批准公告，构建了一个包含4400+个地理标志产品的数据库，包含以下信息：

+ **产品名称**：地理标志产品的名称
+ **产地**：产品产自的*省份*、*城市*和*区县*
+ **感官特征**：公告中对产品感官特征的文本描述

### 数据统计

- **产品总数**：4400+ 个地理标志产品
- **覆盖省份**：31个省级行政区（不含港澳台）
- **覆盖城市**：300+ 个地级市
- **时间跨度**：2005年至今

### 数据来源

地理标志产品检索网站：https://ggfw.cnipa.gov.cn/dlbzsq/dbQuery

- **原质监总局地理标志保护产品批准公告**（2005-2018年）
- **国家知识产权局地理标志保护产品批准公告**（2019年至今）

原始公告文件以PDF格式存储在 `data/origin/` 目录下。

### 数据获取及处理流程

1. **下载公告** - 从官方网站下载地理标志保护产品批准公告PDF文件
2. **提取信息** - 从PDF中提取产品名称、产地、感官描述等信息
3. **文本润色** - 对文本进行规范化处理
4. **数据预处理** - 清洗数据
5. **自然语言处理** - 使用hanlp进行中文分词/词性标注/命名实体识别/成分句法分析

### 数据结构

经过**提取信息**与**文本润色**后的数据，保存为`data/products.json`，每个产品包含以下字段：

```json
{
    "product_name": "产品名称",
    "province": "省份",
    "city": "城市",
    "districts": ["区县1", "区县2", ...],
    "sensory_characteristics": "感官特征描述",
}
```

再经过**自然语言处理**后，保存为`data/tokenized_products.json`，每个产品包含以下字段：

```json
{
  "product_name": "产品名称",
  "tokenized_product_name": {
      "tok/fine": [],
      "pos/ctb": [],
      "ner/msra": [],
      "con": []
  },
  "province": "省份",
  "city": "城市",
  "districts": ["区县1", "区县2", ...],
  "sensory_characteristics": "感官特征描述",
  "tokenized_sensory_characteristics": {
      "tok/fine": [],
      "pos/ctb": [],
      "ner/msra": [],
      "con": []
  }
}
```

## 分析模块

我们对`tokenized_products.json`中的数据进行分析，主要包括以下几个方面：

1. 地理分布分析

2. 感官文本挖掘

### 1. 地理分布分析

位于 `geographic_distribution_analysis/` 目录，主要功能包括：

- **统计分析**：统计各省份、城市的地理标志产品数量
- **地理分布可视化**：使用热力图展示不同产品类别的地理分布
- **多样性可视化**：使用词云图展示各地区的产品多样性

**输出图表**：
- 地理标志产品地理分布柱状图
- 地理标志产品地理分布热力图
- 省份级产品词云图
- 城市级产品词云图

### 2. 感官文本挖掘

位于 `sensory_text_mining/` 目录，主要功能包括：

- **产品共性分析**：分析同类产品的感官形容词共性
- **地缘差异分析**：对比南北地区产品的感官描述差异
- **颜色图谱**：绘制各省份最热门的颜色分布图

**输出图表**：
- 产品感官共性形容词词云图
- 颜色图谱

## 使用方法

### 数据模块

依次查看并运行 `data/` 目录下的Notebook文件：

1. `下载公告.ipynb` - 下载原始PDF公告
2. `提取信息.ipynb` - 从PDF提取产品信息
3. `数据预处理.ipynb` - 预处理数据
4. `文本润色.ipynb` - 润色文本
5. `自然语言处理.ipynb` - 进行分词处理

### 分析模块

1. **地理分布分析**：
   查看并运行`geographic_distribution_analysis/`目录下的`main.ipynb`文件。

2. **感官文本挖掘**：
   查看并运行`sensory_text_mining/`目录下的`main.ipynb`文件。

## 技术栈

- **Python 3.10+**
- **Jupyter Notebook**
- **数据处理**：json, numpy, pandas
- **自然语言处理**：hanlp
- **数据可视化**：matplotlib, pyecharts, wordcloud
- **地理可视化**：geopandas, pyecharts

## 许可证

本项目采用 [LICENSE](LICENSE) 许可证。
