import json
from pathlib import Path

REPORT = Path("/app/report.json")


def _load():
    assert REPORT.exists(), "report.json not found at /app/report.json"
    with REPORT.open() as f:
        return json.load(f)


def test_total_requests():
    """Criterion 1: report contains total_requests == 6 (one entry per log line)."""
    data = _load()
    assert data.get("total_requests") == 6, (
        f"expected total_requests=6, got {data.get('total_requests')}"
    )


def test_unique_ips():
    """Criterion 2: report contains unique_ips == 3 (192.168.0.1, 192.168.0.2, 10.0.0.5)."""
    data = _load()
    assert data.get("unique_ips") == 3, (
        f"expected unique_ips=3, got {data.get('unique_ips')}"
    )


def test_top_path():
    """Criterion 3: report contains top_path == '/index.html' (appears 3 times, most frequent)."""
    data = _load()
    assert data.get("top_path") == "/index.html", (
        f"expected top_path='/index.html', got {data.get('top_path')}"
    )