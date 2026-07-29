from dataclasses import dataclass
from typing import List

from .sections import (
    HeaderSection,
    BootstrapSection,
    MainInfoSection,
    ManualSection,
    PreprocessingSection,
    IntermediateConclusionSection,
    CorrelationSection,
    EngineeringSection,
    InDepthPreprocessingSection,
    EdaSection,
)

from .sections.template import SectionCommand


@dataclass(frozen=True)
class NotebookSpec:
    sections: List[SectionCommand]


FULL_RESEARCH_SPEC = NotebookSpec(
    sections=[
        HeaderSection(),
        BootstrapSection(),
        MainInfoSection(),
        ManualSection(),
        PreprocessingSection(),

        IntermediateConclusionSection(
            conclusion_after_which="поверхностной предобработки"
        ),

        CorrelationSection(),

        IntermediateConclusionSection(
            conclusion_after_which="корреляционного анализа"
        ),

        EngineeringSection(),
        InDepthPreprocessingSection(),
    ]
)

FULL_RESEARCH_STATE_1 = NotebookSpec(
    sections=[
        HeaderSection(),
        BootstrapSection(),
        MainInfoSection(),
        ManualSection(),
    ]
)

FULL_RESEARCH_STATE_2 = NotebookSpec(
    sections=[
        PreprocessingSection(),

        IntermediateConclusionSection(
            conclusion_after_which="поверхностной предобработки"
        ),

        CorrelationSection(),

        IntermediateConclusionSection(
            conclusion_after_which="корреляционного анализа"
        ),

        EngineeringSection(),
        InDepthPreprocessingSection(),
    ]
)

EXPERIMENTS_SPEC = NotebookSpec(
    sections=[
        HeaderSection(),
        BootstrapSection(),
        MainInfoSection(),
        EngineeringSection(),
        EdaSection(),
    ]
)