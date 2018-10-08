import logging
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AppleScript:
    def __init__(self, script_txt: str):
        self.script_txt: str = script_txt

    def __repr__(self):
        return f'AppleScript({self.script_txt})'

    @classmethod
    def from_file(cls, script_path: Path):
        with script_path.open(mode='r') as f:
            return cls(script_txt=f.read())

    @classmethod
    def from_string(cls, script_string: str):
        return cls(script_txt=script_string)

    def run(self):
        logger.debug(f'Running: {self}')
        c = subprocess.check_output(['osascript', '-e', self.script_txt], encoding='utf-8')
        return str(c).strip()
