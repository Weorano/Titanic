import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted


class AdvancedProcessingTransformer(BaseEstimator, TransformerMixin):
    STEPS = (
        "create_ticket_group_size",
        "create_family_features",
        "fill_missing_age",
        "remove_cabin_features",
        "remove_name",
        "remove_ticket_id",
        "optimize_dtypes"
    )

    GROUP_COLUMNS = (
        "category_significance",
        "social_role",
    )

    ROLE_MAPPING = {
        "Master": "child",
        "Miss": "child",
        "Mrs": "adult",
        "Mr": "adult",
    }

    def fit(self, X: pd.DataFrame, y=None):
        df = X.copy()

        df = self._create_social_role(df)

        self.age_medians_ = (
            df.groupby(
                list(self.GROUP_COLUMNS),
                observed=True,
            )["age"]
            .median()
        )

        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        check_is_fitted(
            self,
            "age_medians_",
        )

        df = X.copy()

        for step in self.STEPS:
            df = getattr(self, step)(df)

        return df

    @staticmethod
    def create_ticket_group_size(df: pd.DataFrame) -> pd.DataFrame:
        """
        См. 02_EDA notebook:
        Иерархические исследования (EDA)

        Какие связи после группировки по билетам?
        Что происходит с fare?
        """

        df["ticket_group_size"] = (
            df.groupby("ticket_id")["ticket_id"]
            .transform("count")
            .astype("uint8")
        )

        return df

    @staticmethod
    def create_family_features(df: pd.DataFrame) -> pd.DataFrame:
        """
        См. 02_EDA notebook:
        Иерархические исследования (EDA)

        Как была устроена семейная структура?
        Что именно внутри family_size работает?
        """

        df["surname"] = (
            df["name"]
            .str.split(",")
            .str[0]
        )

        family_group = (
            df.groupby("surname")
            .agg(
                family_size=(
                    "passenger_id",
                    "count",
                ),
                female_count=(
                    "sex",
                    lambda x: (x == "female").sum(),
                ),
                male_count=(
                    "sex",
                    lambda x: (x == "male").sum(),
                ),
                child_count=(
                    "age",
                    lambda x: (x < 18).sum(),
                ),
            )
        )

        family_group["family_type"] = (
            family_group.apply(
                AdvancedProcessingTransformer.get_family_type,
                axis=1,
            )
        )

        df = df.merge(
            family_group.reset_index(),
            on="surname",
            how="left",
        )

        return df.drop(
            columns=[
                "surname",
                "passenger_id",
            ],
        )

    def fill_missing_age(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Возраст восстанавливается медианой внутри групп:
        category_significance + social_role.

        Медианы рассчитываются на этапе fit()
        только по обучающей выборке.
        """

        df = self._create_social_role(df)

        group_index = pd.MultiIndex.from_frame(
            df[list(self.GROUP_COLUMNS)]
        )

        age_medians = self.age_medians_.reindex(
            group_index,
        )

        df["age"] = (
            df["age"]
            .fillna(
                pd.Series(
                    age_medians.to_numpy(),
                    index=df.index,
                )
            )
        )

        return df.drop(
            columns=["social_role"],
        )

    def _create_social_role(self, df: pd.DataFrame) -> pd.DataFrame:
        df["social_role"] = (
            df["name"]
            .str.extract(
                r"\b(Master|Mr|Miss|Mrs)\.",
                expand=False,
            )
            .map(self.ROLE_MAPPING)
            .fillna("other")
        )

        return df

    @staticmethod
    def remove_cabin_features(df: pd.DataFrame) -> pd.DataFrame:
        """
        См. notebook:
        Доказано от обратного смотреть промежуточный вывод.
        """

        return df.drop(
            columns=["cabin"],
            errors="ignore",
        )

    @staticmethod
    def remove_name(df: pd.DataFrame) -> pd.DataFrame:
        return df.drop(columns=["name"])

    @staticmethod
    def remove_ticket_id(df: pd.DataFrame) -> pd.DataFrame:
        return df.drop(columns=["ticket_id"])

    @staticmethod
    def get_family_type(row: pd.Series) -> str:
        male = row["male_count"]
        female = row["female_count"]
        child = row["child_count"]

        if male > 0 and female == 0 and child == 0:
            return "only_men"

        if female > 0 and male == 0 and child == 0:
            return "only_women"

        if child > 0 and male == 0 and female == 0:
            return "only_children"

        if male > 0 and female > 0 and child == 0:
            return "men_women"

        if female > 0 and child > 0 and male == 0:
            return "women_children"

        if male > 0 and child > 0 and female == 0:
            return "men_children"

        if male > 0 and female > 0 and child > 0:
            return "men_women_children"

        return "other"

    def fill_missing_age_direct(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Заполнение пропусков возраста без использования fit().

        Медианы рассчитываются непосредственно на переданном
        DataFrame. Метод предназначен для исследовательской работы.
        """

        df = df.copy()

        df = self._create_social_role(df)

        age_medians = (
            df.groupby(
                list(self.GROUP_COLUMNS),
                observed=True,
            )["age"]
            .transform("median")
        )

        df["age"] = df["age"].fillna(age_medians)

        return df.drop(
            columns=["social_role"],
        )

    @staticmethod
    def optimize_dtypes(df: pd.DataFrame) -> pd.DataFrame:
        """
        Приведение признаков к оптимальным типам данных.

        Категориальные признаки сохраняются как category,
        чтобы downstream-модели могли использовать native categorical encoding.
        """

        df["family_size"] = df["family_size"].astype("uint8")
        df["female_count"] = df["female_count"].astype("uint8")
        df["male_count"] = df["male_count"].astype("uint8")
        df["child_count"] = df["child_count"].astype("uint8")
        df["family_type"] = df["family_type"].astype("category")

        return df