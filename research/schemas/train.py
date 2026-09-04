from research.schemas.base import BaseSchema


class TrainSchema(BaseSchema):
    """
    Новая структура данных.

    DataFrame: titanic

    `passenger_id`
        Уникальный номер пассажира.

    `ticket_id`
        Номер билета.

    `name`
        Имя пассажира.

    `sex`
        Пол.

    `age`
        Возраст в годах.

    `same_importance_relatives`
        Количество братьев и сестер / супругов на борту «Титаника».
        Sibling — брат, сестра, сводный брат, сводная сестра.
        Spouse — муж, жена.

    `high_importance_relatives`
        Количество родителей / детей на борту «Титаника».
        Parent — мать, отец.
        Child — дочь, сын, сводная дочь, сводный сын.
        Некоторые дети путешествовали исключительно с няней,
        поэтому для них parch = 0.

    `category_significance`
        Показатель социально-экономического статуса.
        1 — высший класс.
        2 — средний класс.
        3 — низший класс.

    `fare`
        Стоимость проезда.

    `cabin`
        Номер каюты.

    `survived`
        Выживание в катастрофе.
        0 — Нет.
        1 — Да.

    `embarked`
        Место посадки (порт).
        C — Cherbourg.
        Q — Queenstown.
        S — Southampton.
    """

    RENAME_COLUMNS = {
        "PassengerId": "passenger_id",
        "Ticket": "ticket_id",
        "Name": "name",
        "Sex": "sex",
        "Age": "age",
        "SibSp": "same_importance_relatives",
        "Parch": "high_importance_relatives",
        "Pclass": "category_significance",
        "Fare": "fare",
        "Cabin": "cabin",
        "Survived": "survived",
        "Embarked": "embarked",
    }

    ORDER_COLUMNS = [
        "passenger_id",
        "ticket_id",
        "name",
        "sex",
        "age",
        "same_importance_relatives",
        "high_importance_relatives",
        "category_significance",
        "fare",
        "cabin",
        "embarked",
        "survived",
    ]