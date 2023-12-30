import typing as t


class Result:
    def __init__(
        self, value: t.Any | None = None, error: BaseException | None = None
    ) -> None:
        assert (value is None) != (error is None)

        self._value = value
        self._error = error

    def ok(self) -> t.Any:
        return self._value

    def err(self) -> t.Any:
        return self._error

    def is_ok(self) -> bool:
        return self._value is not None

    def is_err(self) -> bool:
        return self._error is not None

    def expect(self) -> None:
        if self._error is None:
            return self._value

        raise self._error

    def unwrap(self) -> t.Any:
        if self.is_ok():
            return self._value

        raise self._error

    def unwrap_or(self, default: t.Any) -> t.Any:
        return self._value if self.is_ok() else default

    def __repr__(self) -> str:
        return f"Result<{self._value}, {self._error}>"

    def __eq__(self, obj) -> bool:
        try:
            return obj.unwrap() == self._value
        except Exception:
            return False


def Ok(value: t.Any) -> Result:
    return Result(value=value)


def Err(value: t.Any) -> Result:
    if not isinstance(value, BaseException):
        raise ValueError(f"`value` must derive from BaseException")
    return Result(error=value)
