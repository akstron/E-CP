class CodeError(Exception):
    def __init__(self, message, error_type, return_code) -> None:
        super().__init__(message)
        self.error_type = error_type
        self.return_code = return_code

class UnsupportedLanguage(Exception):
    def __init__(self, lang: object) -> None:
        super().__init__(f'{lang} not supported')