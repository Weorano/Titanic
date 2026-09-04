# from workflows.create_research_env import ResearchEnvPipeline
from workflows.finalize_research import ProcessedDatasetBuilder


# def run_1():
#     # Создание пустой тетрадки с базовыми настройками
#     pipeline = ResearchEnvPipeline()
#     pipeline.run()
#     print("OK: research environment created")

def run_2():
    # Запуск research pipeline для преобразования experiments
    builder = ProcessedDatasetBuilder('baseline_v1')
    builder.build()

def run_3():
    # Запуск research pipeline для преобразования experiments
    pass

if __name__ == "__main__":
    run_3()
