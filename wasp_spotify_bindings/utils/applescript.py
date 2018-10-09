import subprocess
from typing import Optional


class AppleScript:
    def __init__(self, script_txt: str) -> None:
        self.script_txt: str = script_txt

    def __repr__(self) -> str:
        return f'AppleScript({self.script_txt})'

    def run(self) -> Optional[str]:
        c = subprocess.check_output(['osascript', '-e', self.script_txt], encoding='utf-8')
        res = str(c).strip()
        return res if res != '' else None
