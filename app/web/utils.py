from aiohttp import web
from aiohttp.web import json_response as aiohttp_json_response
from aiohttp.web_response import Response


def json_response(data: dict | None = None, status: str = "ok") -> Response:
    if data is None:
        data = {}

    return aiohttp_json_response(
        data={
            "status": status,
            "data": data,
        }
    )


def error_json_response(http_status: int, status: str = "error", message: str | None = None, data: dict | None = None) -> Response:
    payload = {"status": status, "message": message}
    if data is not None:
        payload["data"] = data
    return web.json_response(payload, status=http_status)