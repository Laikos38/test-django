class BaseException(Exception):
    msg: str = "Error, please try again later."
    status_code: int = 500
    ok: bool = False

    def __init__(self, msg: str, status_code: int, ok: bool = False):
        self.msg = msg
        self.status_code = status_code
        self.ok = ok
