import typing as t


class Result:
    def __init__(self, value: t.Any | None = None, error: t.Any | None = None):
        if value is None and error is None:
            raise ValueError("Both `value` and `error` cannot be None")

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

    def __repr__(self) -> str:
        return f"Result<{self.value}, {self.error}>"

    def __call__(self):
        pass


@Result
def test():
    pass
