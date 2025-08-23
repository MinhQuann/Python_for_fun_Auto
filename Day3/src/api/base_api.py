from __future__ import annotations
import time
import requests
from typing import Any, Dict, Optional

class BaseAPI:
    def __init__(self, base_url: str, timeout: int = 10, session: Optional[requests.Session] = None):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = session or requests.Session()
        self.session.headers.update({"Content-Type": "application/json; charset=utf-8"})

    def _retry(self, fn, retries=2, backoff=0.5):
        last = None
        for i in range(retries + 1):
            try:
                return fn()
            except requests.RequestException as e:
                last = e
                if i == retries:
                    raise
                time.sleep(backoff * (2 ** i))
        if last:
            raise last

    def get(self, path: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self._retry(lambda: self.session.get(url, timeout=self.timeout, **kwargs))

    def post(self, path: str, json: Dict[str, Any], **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return self._retry(lambda: self.session.post(url, json=json, timeout=self.timeout, **kwargs))
