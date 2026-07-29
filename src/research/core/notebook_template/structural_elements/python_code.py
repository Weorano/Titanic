import textwrap

import pandas as pd


class VisualizationCodeStructurer:
    chart_types = {
        'pie_chart': 'generate_pie_chart',
        'countplot_with_all_values': 'generate_countplot_with_all_values',
        'countplot_top_20': 'generate_countplot_top_20',
        'hist_with_boxplot': 'generate_hist_with_boxplot'
    }

    def get_chart_code(
            self,
            table_name: str,
            table_column_name: str,
            data_for_chart: pd.Series,
    ) -> str:
        chart_type = self.defining_visualisation_type(data_for_chart)

        function_name = self.chart_types.get(chart_type, None)

        function_to_call = getattr(self, function_name, None)

        if function_to_call is None:
            raise ValueError(f"Unknown chart type: {chart_type}")

        return function_to_call(table_name, table_column_name)

    @staticmethod
    def defining_visualisation_type(pandas_column: pd.Series) -> str:
        data_type = pandas_column.dtype
        unique_values = pandas_column.nunique()

        if unique_values <= 5:
            return 'pie_chart'
        elif unique_values > 5 and unique_values <= 15:
            return 'countplot_with_all_values'
        elif data_type == 'object' and unique_values > 15:
            return 'countplot_top_20'
        else:
            return 'hist_with_boxplot'


    # тут нужно дописывать под несколько value_counts
    @staticmethod
    def generate_pie_chart(table_name: str, column: str) -> str:
        return textwrap.dedent(f"""
            group_name = {table_name}['{column}'].value_counts()

            colors = ['#7cb480', '#4da54d']

            custom_pie_chart(
                data=group_name,
                colors=colors,
                explode=[0.1, 0],
                startangle=100,
                title='Заголовок',
            )
        """).strip()

    @staticmethod
    def generate_countplot_with_all_values(
            table_name: str,
            column: str
    ) -> str:
        return textwrap.dedent(f"""
            plt.figure(figsize=(13, 6))
        
            sns.countplot(
                y='{column}',
                data={table_name},
                palette='YlGn',
                hue='{column}',
                legend=False
            )

            plt.title('Распределение {column}')
            plt.ylabel('{column}')
            plt.xlabel('Количество')

            plt.show()
        """).strip()

    @staticmethod
    def generate_countplot_top_20(
            table_name: str,
            column: str
    ) -> str:
        return textwrap.dedent(f"""
            top_20_values = (
                {table_name}['{column}']
                .value_counts()
                .nlargest(20)
            )

            sns.countplot(
                y='{column}',
                data={table_name}[
                    {table_name}['{column}'].isin(top_20_values.index)
                ],
                palette='YlGn',
            )

            plt.title('Топ 20 значений для {column}')
            plt.ylabel('{column}')
            plt.xlabel('Количество')

            plt.show()
        """).strip()

    @staticmethod
    def generate_hist_with_boxplot(
            table_name: str,
            column: str
    ) -> str:
        return textwrap.dedent(f"""
            custom_hist_with_boxplot(
                dataframe={table_name},
                x_value_name='{column}',
                bins=80,
                hist_title='Заголовок',
                x_label='Название оси',
            )
        """).strip()