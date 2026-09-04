from typing import Dict, Any


class JupyterCellCreator:
    @staticmethod
    def create_cell_with_shell(shell, code: str) -> None:
        payload = dict(
            source='set_next_input',
            text=code,
            replace=False,
        )
        shell.payload_manager.write_payload(payload, single=False)

    @staticmethod
    def create_code_cell(code: str) -> Dict[str, Any]:
        return {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                line + "\n"
                for line in code.strip().splitlines()
            ]
        }

    @staticmethod
    def create_markdown_cell(markdown: str) -> Dict[str, Any]:
        return {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                line + "\n"
                for line in markdown.strip().splitlines()
            ]
        }