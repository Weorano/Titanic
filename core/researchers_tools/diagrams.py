import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def custom_hist_with_boxplot(
        dataframe,
        x_value_name: str,
        bins: int = 30,
        target_name: str | None = None,
        mode: str = "density",  # overlay | density
        hist_title: str | None = None,
        boxplot_title: str | None = None,
        x_label: str | None = None,
        range: tuple[float, float] | None = None,
):
    import pandas as pd

    # --------------------------------------------------
    # подготовка групп
    # --------------------------------------------------

    grouped_dfs = []
    labels = []

    if target_name is not None and x_value_name != target_name:
        for target_value in dataframe[target_name].dropna().unique():
            df_part = dataframe[dataframe[target_name] == target_value]
            if len(df_part) == 0:
                continue
            grouped_dfs.append(df_part)
            labels.append(str(target_value))

    # --------------------------------------------------
    # ГЛОБАЛЬНАЯ гистограмма (ОДНА)
    # --------------------------------------------------

    dataframe[x_value_name].hist(
        bins=bins,
        range=range,
    )

    plt.title(hist_title or f'Распределение по {x_value_name}')
    plt.xlabel(x_label or x_value_name)
    plt.ylabel('Количество')
    plt.show()

    # --------------------------------------------------
    # ГРУППОВАЯ гистограмма
    # --------------------------------------------------

    if target_name is not None and x_value_name != target_name:

        colors = ['green', 'red', 'skyblue']

        for i, df_part in enumerate(grouped_dfs):

            if mode == "overlay":
                plt.hist(
                    df_part[x_value_name].dropna(),
                    bins=bins,
                    label=labels[i],
                    color=colors[i % len(colors)],
                    alpha=1 if i == 0 else 0.7,
                    range=range,
                )

            elif mode == "density":
                plt.hist(
                    df_part[x_value_name].dropna(),
                    bins=bins,
                    density=True,
                    alpha=0.4,
                    label=labels[i],
                    color=colors[i % len(colors)],
                    range=range,
                )

            else:
                raise ValueError("mode must be overlay or density")

        plt.legend()
        plt.title(f'{hist_title or f"Распределение по {x_value_name}"} относительно {target_name}')
        plt.xlabel(x_label or x_value_name)
        plt.ylabel('Количество')
        plt.show()

    # --------------------------------------------------
    # BOXPLOT (СТАБИЛЬНЫЙ)
    # --------------------------------------------------

    if not pd.api.types.is_numeric_dtype(dataframe[x_value_name]):
        return

    boxplot_data = []
    boxplot_labels = []

    grouped_dfs.append(dataframe)
    labels.append('Все данные')

    for df_part, label in zip(grouped_dfs, labels):
        series = df_part[x_value_name].dropna()
        if len(series) == 0:
            continue
        boxplot_data.append(series)
        boxplot_labels.append(label)

    plt.boxplot(
        boxplot_data,
        tick_labels=boxplot_labels,
        vert=False,
        patch_artist=True,
        medianprops={'color': 'red', 'linewidth': 2}
    )

    plt.title(boxplot_title or f'Выбросы по {x_value_name}')
    plt.xlabel(x_label or x_value_name)
    plt.show()

def custom_pie_chart(
        data,
        explode=None,
        autopct='%1.1f%%',
        startangle=120,
        shadow=True,
        colors=None,
        title='',
        legend_loc='upper left',
        legend_bbox_to_anchor=(1, 1),
        legend_fontsize=12,
        legend_frameon=True,
        legend_shadow=True,
        legend_borderpad=2,
        legend_borderaxespad=2,
        legend_handleheight=3,
        legend_handlelength=4,
):
    if colors is None:
        colors = ['#7cb480', '#4da54d', '#2f8f2f']

    wedgeprops = {
        'linewidth': 10,
        'edgecolor': '#008000',
        'linestyle': '-',
        'antialiased': True,
        'alpha': 0.8
    }

    plt.figure(figsize=(10, 8))
    patches, texts, autotexts = plt.pie(
        x=data,
        explode=explode,
        autopct=autopct,
        startangle=startangle,
        shadow=shadow,
        colors=colors,
        wedgeprops=wedgeprops
    )

    for text in texts + autotexts:
        text.set_fontsize(13)

    legend_elements = [
        Patch(
            facecolor=color,
            linewidth=0,
            label=label,
            antialiased=True
        )
        for color, label in zip(colors, data.keys())
    ]

    plt.legend(
        handles=legend_elements,
        loc=legend_loc,
        bbox_to_anchor=legend_bbox_to_anchor,
        fontsize=legend_fontsize,
        frameon=legend_frameon,
        shadow=legend_shadow,
        borderpad=legend_borderpad,
        borderaxespad=legend_borderaxespad,
        handleheight=legend_handleheight,
        handlelength=legend_handlelength
    )

    plt.title(title, fontsize=15)
    plt.axis('equal')
    plt.show()
