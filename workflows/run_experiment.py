from experiments.model_analysis import ModelAnalysisExperiment
from experiments.model_comparison_v1 import ModelComparisonExperiment
from research.experiments.baseline_v1 import BaselineExperiment


def start_experiment_1():
    BaselineExperiment().run()

def start_experiment_2():
    ModelComparisonExperiment().run()

def start_experiment_3():
    ModelAnalysisExperiment().run()

if __name__ == "__main__":
    start_experiment_2()