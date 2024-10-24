"""
Supply a glob with each (not both!) to use this, like:
python3 -m bleanser_pura.modules.smscalls prune --glob 'calls-*'
python3 -m bleanser_pura.modules.smscalls prune --glob 'sms-*'
"""

from pathlib import Path
from typing import Iterator, Any

from my.smscalls import _extract_calls, _extract_messages

from bleanser.core.modules.extract import ExtractObjectsNormaliser


class Normaliser(ExtractObjectsNormaliser):
    def extract_objects(self, path: Path) -> Iterator[Any]:
        if "calls" in path.stem:
            for call in _extract_calls(path):
                if isinstance(call, Exception):
                    continue
                yield f"{call.dt} {call.who}"
        else:
            assert "sms" in path.stem, f"calls or sms needs to be in path name {path}"
            for sms in _extract_messages(path):
                if isinstance(sms, Exception):
                    continue
                yield f"{sms.dt} {sms.who}"


if __name__ == "__main__":
    Normaliser.main()
