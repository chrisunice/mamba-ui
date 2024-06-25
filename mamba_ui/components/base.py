from abc import ABC, abstractmethod


class BaseComponent(ABC):

    name = 'Base Component'

    def __init__(
            self,
            name: str = None,
            index: str = None
    ):
        """
        Base component to be inherited by all other components

        :param name: the name of the component; if no name is given then the class attribute name will be used
        :param index: a unique index that should specify the location of the component
        """
        super().__init__()

        if name is None:
            name = self.name

        if index is None:
            index = ''

        self.id = {
            'name': '-'.join(name.lower().split()),         # base-component
            'index': index                                  # unique index
        }

    def get_child_id(self, childs_name: str) -> dict:
        """
        Adds a `type` key to the component's id dictionary that specifies the child type
        Example:
              {
                'name': 'base-component',
                'index': 'r0c0',
                'type': 'input'
              }

        :param childs_name: a string to specify the child components name
        :return: a child_id dictionary
        """
        child_id = self.id.copy()
        child_id['type'] = childs_name
        return child_id

    @property
    @abstractmethod
    def component(self):
        """ Placeholder property that must be overwritten by inheriting classes """
        pass
