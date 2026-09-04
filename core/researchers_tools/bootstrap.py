import textwrap
from .settings import INLINE_BACKEND_CONFIG


class Bootstrap:
    @staticmethod
    def build_tools_for_working_bootstrap_cell() -> str:
        return textwrap.dedent(
            """
            import pandas as pd
            import numpy as np
            
            import matplotlib.pyplot as plt
            import matplotlib.dates as mdates
            import seaborn as sns
            import plotly.express as px
            
            import missingno as msno
            from phik import phik_matrix
            
            # Обёртки для диаграмм
            from research.core.researchers_tools import (
                custom_pie_chart,
                custom_hist_with_boxplot
            )
            """
        ).strip()

    @staticmethod
    def build_graphical_visualization_bootstrap_cell() -> str:
        return textwrap.dedent(
            """
            {inline}

            from research.core.researchers_tools.settings import (
                GRAPH_STYLES,
                PROP_CYCLE,
            )

            plt.rcParams['axes.prop_cycle'] = plt.cycler(color=PROP_CYCLE)
            plt.rcParams.update(GRAPH_STYLES)
            """
        ).format(
            inline=INLINE_BACKEND_CONFIG.strip()
        ).strip()


