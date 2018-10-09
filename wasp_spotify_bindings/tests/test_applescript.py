from wasp_spotify_bindings.utils import applescript

example_apple_script = """
set one to 1
set two to 2
set answer to two - one
return answer
"""
apple_script_from_string = applescript.AppleScript(script_txt=example_apple_script)
assert apple_script_from_string.run() == "1"


