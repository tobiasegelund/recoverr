import typing as t

T = t.TypeVar("T")
E = t.TypeVar("E")


class Result:
    """A Result to store a value or error depending on the outcome of the result"""

    def __init__(self, value: T | None = None, error: E | None = None) -> None:
        assert (value is None) != (error is None)

        self._value = value
        self._error = error

    def ok(self) -> T | None:
        """Returns the value and dispatches the error if any

        Note it may return None
        """
        return self._value

    def err(self) -> E | None:
        return self._error

    def is_ok(self) -> bool:
        return self._value is not None

    def is_err(self) -> bool:
        return self._error is not None

    def expect(self) -> None:
        if self._error is None:
            return self._value
        raise self._error

    def or_(self, res):
        if self.is_err():
            return res
        return self

    def unwrap(self) -> T:
        if self.is_ok():
            return self._value

        raise self._error

    def unwrap_err(self) -> E:
        if self.is_ok():
            raise ValueError("Result stores a Ok value")
        return self._error

    def unwrap_or(self, default: T) -> T:
        if self.is_ok():
            return self._value
        return default

    def __repr__(self) -> str:
        return f"Result<{self._value}, {self._error}>"

    def __hash__(self):
        key = (self._value, self._error, self.__class__)
        return hash(key)

    def __eq__(self, obj) -> bool:
        try:
            return obj.unwrap() == self._value
        except Exception as _:
            return False

    def __nq__(self, obj) -> bool:
        try:
            return obj.unwrap() == self._value
        except Exception as _:
            return False


def Ok(value: T) -> Result:
    return Result(value=value)


def Err(value: T) -> Result:
    if not isinstance(value, BaseException):
        raise ValueError(f"`value` must derive from BaseException")
    return Result(error=value)
