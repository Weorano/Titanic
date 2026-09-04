from dataclasses import dataclass
from typing import List

from notebooks.templates.sections import (
    HeaderSection,
    BootstrapSection,
    MainInfoSection,
    ManualSection,
    # PreprocessingSection,
    # IntermediateConclusionSection,
    # CorrelationSection,
    # EngineeringSection,
    # InDepthPreprocessingSection,
    # EdaSection,
)

from notebooks.templates.sections.template import SectionCommand


@dataclass(frozen=True)
class NotebookSpecification:
    name: str
    sections: List[SectionCommand]


NOTEBOOK_PROJECT_OVERVIEW = NotebookSpecification(
    name="00_Project_Overview",
    sections=[
        HeaderSection()
    ]
)

NOTEBOOK_PREPROCESSING = NotebookSpecification(
    name="01_Preprocessing",
    sections=[
        HeaderSection(),
        BootstrapSection(),
        MainInfoSection(),
        ManualSection(),
        # HeaderSection(),
        # BootstrapSection(),
        # MainInfoSection(),
        # ManualSection(),
        # PreprocessingSection(),
        # IntermediateConclusionSection(
        #     conclusion_after_which="поверхностной предобработки"
        # ),
    ]
)

NOTEBOOK_EDA = NotebookSpecification(
    name="02_EDA",
    sections=[
        HeaderSection(),
        BootstrapSection(),
        MainInfoSection(),
        ManualSection(),

        # EngineeringSection(),
        # CorrelationSection(),
        # IntermediateConclusionSection(
        #     conclusion_after_which="итоговый вывод"
        # ),
    ]
)

NOTEBOOK_ADVANCED_PROCESSING = NotebookSpecification(
    name="03_Advanced_Processing",
    sections=[
        HeaderSection(),
        BootstrapSection(),
        MainInfoSection(),
        ManualSection(),

        # InDepthPreprocessingSection(),
    ]
)