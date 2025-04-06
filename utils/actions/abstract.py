from abc import ABC, abstractmethod
from typing import Generic

from utils.actions.typing import ActionReturn


class AbstractAction(Generic[ActionReturn], ABC):
    def validate(self):
        """
        Метод в котором происходит какая-то валидация запроса, если она необходима.
        В методе можно возбуждать исключения
        """

    @abstractmethod
    def action(self) -> ActionReturn:
        """
        Метод для определения бизнес логики процесса.
        """

    def execute(self) -> ActionReturn:
        self.validate()
        return self.action()

    def execute_without_validate(self) -> ActionReturn:
        return self.action()
