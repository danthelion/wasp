import logging
import subprocess

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class AppleScript:
    def __init__(self, script_txt: str):
        self.script_txt: str = script_txt

    def __repr__(self):
        return f'AppleScript({self.script_txt})'

    def run(self):
        logger.debug(f'Running: {self}')
        c = subprocess.check_output(['osascript', '-e', self.script_txt], encoding='utf-8')
        return str(c).strip()
