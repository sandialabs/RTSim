"""Base component class."""

from rtsim import validate


class Base:
    """Base class to include monikers and format components in a uniform manner."""

    def __init__(self, moniker: str) -> None:
        """Initialize a component with a moniker."""
        self.moniker = moniker

    @property
    def moniker(self):
        """Moniker getter."""
        return self._moniker

    @moniker.setter
    def moniker(self, value):
        """Moniker setter."""
        validate.string(value)
        self._moniker = value

    def __repr__(self):
        """Return a string representation of the component."""
        return f"{self.__class__.__name__}({self.moniker})"

    def __str__(self):
        """Return a string representation of the component."""
        return f"{self.__class__.__name__}({self.moniker})"
