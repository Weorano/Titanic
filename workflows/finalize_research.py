from artifacts.context import Experiment


def finalize_research(experiment_name: str) -> None:
    experiment = Experiment(experiment_name)

    print(
        f"\n{'=' * 60}"
        f"\nФинализация исследования: {experiment.name}"
        f"\n{'=' * 60}"
    )

    print("\nСоздание human-readable dataset...")
    experiment.overview.get()

    print("\nПроверка метаданных...")
    # какая-то хуйня
    # experiment.metadata

    print(
        "\nИсследовательская часть эксперимента "
        "успешно финализирована."
    )