import re
import os

def replace_breakpoints_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find rx.breakpoints(...)
    # This regex tries to capture the content inside rx.breakpoints(...)
    # It handles multi-line arguments
    pattern = r'rx\.breakpoints\s*\((.*?)\)'
    
    def replacement(match):
        args_str = match.group(1)
        # Convert args like initial="6", xs="7" to dict format
        # We need to parse the arguments. 
        # Simple approach: replace '=' with ':' and wrap in braces
        
        # Split by comma, but be careful about commas in strings (though unlikely here)
        args = args_str.split(',')
        new_args = []
        for arg in args:
            arg = arg.strip()
            if not arg: continue
            if '=' in arg:
                key, value = arg.split('=', 1)
                key = key.strip()
                value = value.strip()
                # Quote the key if it's not quoted
                if not key.startswith('"') and not key.startswith("'"):
                    key = f'"{key}"'
                new_args.append(f'{key}: {value}')
            else:
                # Might be a positional arg or something else, just keep it?
                # But rx.breakpoints usually takes kwargs.
                pass
        
        return '{\n' + ',\n'.join(['    ' + arg for arg in new_args]) + '\n}'

    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if content != new_content:
        print(f"Modifying {filepath}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    else:
        print(f"No changes in {filepath}")

files = [
    'adeviento_web/views/header.py',
    'adeviento_web/views/navbar.py',
    'adeviento_web/views/calendar.py',
    'adeviento_web/views/day_detail.py',
    'adeviento_web/components/countdown.py',
    'adeviento_web/components/special_effects.py',
    'adeviento_web/components/shanghai_info.py'
]

for file in files:
    if os.path.exists(file):
        replace_breakpoints_in_file(file)
    else:
        print(f"File not found: {file}")
