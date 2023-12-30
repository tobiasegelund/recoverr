import typing as t


class Result:
    def __init__(self, value: t.Optional[t.Any] = None, error: t.Optional[t.Any] = None):
        self.value = value
        self.error = error

    def is_ok(self) -> bool:
        return self.error is None

    def is_err(self) -> bool:
        return self.error is not None

    def expect(self) -> None:
        pass

    def unwrap(self) -> t.Any:
        if self.is_ok():
            return self.value
        else:
            raise ValueError(f"Result is an error: {self.error}")

    def unwrap_or(self, default: t.Any) -> t.Any:
        return self.value if self.is_ok() else default

    def __repr__(self):
        return f"Result<{self.value}, {self.error}>"
