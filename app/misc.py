def response(
        result: str | int | dict | None = None,
        error: str | dict | None = None,
        code: int | None = None
) -> tuple[dict, int]:
    if result is not None:
        return {'result': result}, code or 200
    return {'error': error}, code or 400
