# tests/api/test_ucrm_load_data_smoke.py
import os
import json
import pytest
import requests
from dotenv import load_dotenv

pytestmark = [pytest.mark.api, pytest.mark.smoke]

URL = "https://portal.basebs.net/ucrmapi/expose-api/load-data"

# Các tham số bạn cung cấp
PARAMS = {
    "tenant_id":   "tnt_vtbv3266_64332808",
    "object_id":   "obj_contact_00000001",
    "field_id":    "fld_contact_id_00000001",
    "is_get_details": "true",
    "value":       "VTB9297376",
}

TIMEOUT = 15  # giây

def _auth_headers():
    """
    Nếu API yêu cầu Bearer token, đọc từ .env (API_AUTH_TOKEN).
    Nếu không có, trả về headers rỗng.
    """
    load_dotenv()
    token = os.getenv("API_AUTH_TOKEN", "").strip()
    headers = {
        "Accept": "application/json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers


def _pretty(obj, limit=800):
    """In JSON gọn khi cần debug."""
    try:
        s = json.dumps(obj, ensure_ascii=False, indent=2)
    except Exception:
        s = str(obj)
    return (s[:limit] + "...") if len(s) > limit else s


def test_ucrm_load_data_smoke():
    """
    Smoke test:
    - Gọi GET với params đã cho
    - Expect HTTP 200
    - Payload parse được JSON
    - JSON không rỗng
    - Nếu có các khóa phổ biến (data/items/result/records) thì tối thiểu phải có nội dung
    """
    headers = _auth_headers()
    resp = requests.get(URL, params=PARAMS, headers=headers, timeout=TIMEOUT)

    # 1) HTTP OK
    assert resp.status_code == 200, f"HTTP {resp.status_code} - body: {resp.text[:500]}"

    # 2) Là JSON hợp lệ
    try:
        payload = resp.json()
    except Exception as e:
        pytest.fail(f"Không parse được JSON: {e} — raw: {resp.text[:500]}")

    # 3) Không rỗng
    assert payload is not None, "Payload None"
    if isinstance(payload, (list, tuple)):
        assert len(payload) > 0, f"Payload rỗng: {payload}"
    elif isinstance(payload, dict):
        assert len(payload.keys()) > 0, f"Payload dict rỗng: {payload}"
    else:
        pytest.fail(f"Kiểu payload bất ngờ: {type(payload)} — {_pretty(payload)}")


def test_ucrm_contact_metadata_contract():
    resp = requests.get(URL, params=PARAMS, timeout=20)
    assert resp.status_code == 200, f"HTTP {resp.status_code} - {resp.text[:300]}"

    payload = resp.json()
    assert isinstance(payload, dict) and "data" in payload, "payload phải là dict có key 'data'"
    assert isinstance(payload["data"], list) and payload["data"], "data[] phải là list không rỗng"

    # Validate TẤT CẢ item trong data[], hoặc chỉ 1 vài item đầu để smoke
    errors = []
    for idx, item in enumerate(payload["data"]):
        try:
            rec = ContactRecord.model_validate(item)
            # Nếu yêu cầu 'active' bắt buộc True:
            assert rec.active is True, f"[{idx}] active phải True"
        except Exception as e:
            errors.append(f"[{idx}] {e}")

    assert not errors, "Lỗi contract:\n" + "\n".join(errors)

