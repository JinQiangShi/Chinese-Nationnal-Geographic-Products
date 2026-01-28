import os
from pyecharts import options as opts
from pyecharts.charts import Map

def province_heatmap_plot(
    sorted_province_product_dict: dict,
    figure_dir: str
):
    """
    绘制地理标志产品数量的省份级地理分布热力图，支持多个产品的对比展示。

    Parameters:
    -----
        sorted_province_product_dict (dict): 字典，键为产品名称，值为该产品在各省份的分布统计（按数量降序排序的元组列表）。
        figure_dir (str): 保存热力图的目录路径。
    """
    c = (
        Map(init_opts=opts.InitOpts(
            width="100%",
            height="100%",
            page_title="中国地理标志产品分布热力图",
            theme="light"
        ))
    )

    for product, province_data in sorted_province_product_dict.items():
        map_data = [(province, count) for province, count in province_data]
        c = c.add(
            product,
            map_data,
            "china",
            is_map_symbol_show=False,
        )

    product_max_dict = {
        product: max(count for _, count in province_data)
        for product, province_data in sorted_province_product_dict.items()
    }

    c = c.set_global_opts(
        title_opts=opts.TitleOpts(
            title="地理标志产品数量地理分布热力图",
            pos_left="center",
            pos_top="5%"
        ),
        legend_opts=opts.LegendOpts(
            pos_left="left",
            pos_top="15%",
            orient="vertical",
            selected_mode="single"
        ),
        visualmap_opts=opts.VisualMapOpts(
            min_=1,
            max_=max(product_max_dict.values()),
            is_piecewise=False,
            pos_left="right",
            pos_top="center",
            range_color=["#50a3ba", "#eac736", "#d94e5d"],
        ),
        tooltip_opts=opts.TooltipOpts(
            trigger="item",
            formatter="{a}<br/>{b}<br/>数量: {c}"
        ),
    )

    output_path = os.path.join(figure_dir, "地理标志产品地理分布热力图.html")
    c.render(output_path)

    with open(output_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    product_max_json = str(product_max_dict).replace("'", '"')

    html_content = html_content.replace(
        '<html>',
        f'''<html>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            body {{
                width: 100vw;
                height: 100vh;
                overflow: hidden;
            }}
            #chart-container {{
                width: 100vw;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            .chart-container {{
                width: 100% !important;
                height: 100% !important;
            }}
        </style>
        <script>
            var productMaxDict = {product_max_json};
            
            window.onload = function() {{
                var chart = echarts.init(document.querySelector('.chart-container'));
                var option = chart.getOption();
                option.legend[0].top = '15%';
                
                function updateVisualMap(selectedName) {{
                    var newMax = productMaxDict[selectedName];
                    var newOption = chart.getOption();
                    newOption.visualMap[0].max = newMax;
                    newOption.visualMap[0].range = [1, newMax];
                    chart.setOption(newOption);
                }}
                
                chart.on('legendselectchanged', function(params) {{
                    var selectedName = params.name;
                    updateVisualMap(selectedName);
                }});
                
                chart.setOption(option);
                
                setTimeout(function() {{
                    var currentOption = chart.getOption();
                    var selectedSeries = currentOption.legend[0].selected;
                    for (var name in selectedSeries) {{
                        if (selectedSeries[name]) {{
                            updateVisualMap(name);
                            break;
                        }}
                    }}
                }}, 100);
            }};
        </script>'''
    )

    html_content = html_content.replace(
        '<body>',
        '<body><div id="chart-container">'
    )

    html_content = html_content.replace(
        '</body>',
        '</div></body>'
    )

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"热力图已保存至: {output_path}")
