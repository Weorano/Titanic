from pipelines.create_research_env import ResearchEnvPipeline


if __name__ == "__main__":
    pipeline = ResearchEnvPipeline()
    pipeline.run()
    print("OK: research environment created")