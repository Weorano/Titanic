from functools import wraps


def log_experiment(func):
    @wraps(func)
    def wrapper(self, name, *args, **kwargs):
        logger = self.logger

        print(f"Starting experiment: {name}")

        logger.info(
            "Starting experiment: %s",
            name,
        )

        try:
            result = func(
                self,
                name,
                *args,
                **kwargs,
            )

        except Exception:
            logger.exception(
                "Experiment failed: %s",
                name,
            )
            raise

        print(f"Finished experiment: {name} | score={result.score}")

        logger.info(
            "Finished experiment: %s | score=%.4f",
            name,
            result.score,
        )

        return result

    return wrapper