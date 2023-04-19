import re

# Path to the stylesheet or script
stylesheet_or_script_path = '{% static \'example/file\' %}'

# Regular expression to match the path
pattern = re.compile(r'\{\%\sstatic\s\'(.+)\'\s\%\}')

# Replace the matched path with your own path
new_path = 'www.example.com/example/file'

# Replace the stylesheet or script path
result = re.sub(pattern, new_path, stylesheet_or_script_path)

# Print the result
print(result)