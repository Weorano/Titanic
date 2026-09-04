class MetadataError(Exception):
    pass


class Metadata:
    REQUIRED_FEATURE_GROUPS = (
        "target",
        "identifiers",
        "numerical_features",
        "categorical_features",
        "ordinal_features",
        "binary_features",
    )

    def __init__(self, config: dict) -> None:
        self.config = config

    def get(self) -> dict:
        structure = self.config.get("structure", {})

        if structure is None:
            raise MetadataError(
                "В config отсутствует structure"
            )

        if not self._is_valid_structure(structure):
            raise MetadataError(
                "Неправильно построен structure в config"
            )

        return structure

    @classmethod
    def _is_valid_structure(cls, structure: dict) -> bool:
        return all(
            group in structure
            and structure[group] is not None
            for group in cls.REQUIRED_FEATURE_GROUPS
        )

    def print_metadata(
        self,
        structure: dict,
    ) -> None:
        print(
            f"\nМетаданные эксперимента: "
            f"{self.config['experiment_name']}"
        )

        print("\nЦелевой:")
        print(structure.get("target"))

        print("\nИдентификаторы:")
        print(structure.get("identifiers") or [])

        print("\nЧисловые признаки:")
        print(structure.get("numerical_features") or [])

        print("\nКатегориальные признаки:")
        print(structure.get("categorical_features") or [])

        print("\nПорядковые признаки:")
        print(structure.get("ordinal_features") or [])

        print("\nБинарные признаки:")
        print(structure.get("binary_features") or [])