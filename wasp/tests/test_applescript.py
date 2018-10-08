from pathlib import Path

from wasp.utils import applescript

example_apple_script = """
set one to 1
set two to 2
set answer to two - one
return answer
"""
apple_script_from_string = applescript.AppleScript.from_string(script_string=example_apple_script)
assert apple_script_from_string.run() == "1"

example_apple_script_file = Path(__file__).parent / 'sample_applescript.scpt'
apple_script_from_file = applescript.AppleScript.from_file(script_path=example_apple_script_file)
assert apple_script_from_file.run() == "3"

