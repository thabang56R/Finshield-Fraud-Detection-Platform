from typing import Any


def build_realtime_features(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "amount": payload.get("amount", 0),
        "device_type": payload.get("device_type", "unknown"),
        "country": payload.get("country", "unknown"),
    }