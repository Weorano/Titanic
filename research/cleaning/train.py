import pandas as pd

from research.cleaning.base import BaseCleaner


class TrainCleaner(BaseCleaner):
    """
    Очистка исходного Titanic датасета.

    Выполняет одноразовые операции над исходным датасетом,
    которые могут изменять состав строк и не должны входить
    в sklearn pipeline.
    """

    STEPS = (
        "remove_invalid_ticket_group",
    )

    @staticmethod
    def remove_invalid_ticket_group(
        df: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        См. 01_Preprocessing notebook:
        DF @titanic `high_importance_relatives` → Общий вывод
        DF @titanic `high_importance_relatives` → Устранение аномалий
        """

        return df[df["ticket_id"] != "W./C. 6608"].copy()