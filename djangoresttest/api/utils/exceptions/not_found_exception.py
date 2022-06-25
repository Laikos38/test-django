from djangoresttest.api.utils.exceptions import BaseException


class NotFoundException(BaseException):
    msg: str = "Not found."
    status_code: int = 404
    ok: bool = False

    def __init__(self, msg: str = "Not found.", status_code: int = 404, ok: bool = False):
        self.msg = msg
        self.status_code = status_code
        self.ok = ok
