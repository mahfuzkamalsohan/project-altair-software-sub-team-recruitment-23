#!/bin/bash

DIR="$HOME/altair_software_recruitment/executables"
FILE="$DIR/hello_altair.py"

# python file with shebang and print statement
cat << 'EOF' > "$FILE"
#!/usr/bin/env python3
print("Hello Altair!")
EOF

# root permission
sudo chmod 700 "$FILE"

echo "Python file created at $FILE and executable only by root."
