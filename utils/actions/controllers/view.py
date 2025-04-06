from typing import Generic

from rest_framework.exceptions import APIException

from utils.actions.abstract import AbstractAction
from utils.actions.exceptions import ActionValidateException
from utils.actions.typing import ActionReturn


class ViewActionController(Generic[ActionReturn]):
    def __init__(self, action: AbstractAction[ActionReturn]):
        self.action = action

    def execute(self) -> ActionReturn:
        try:
            return self.action.execute()
        except ActionValidateException as exception:
            raise APIException(exception)
