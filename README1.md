Build a tool that calculates hash values (MD5, SHA-256) of digital evidence to ensure data integrity during investigations, useful for verifying that evidence hasn't been tampered with.
How It Works:

• The user provides a file as input.
• The tool calculates the MD5 and SHA-256 hash values for the file.
• These hash values can then be compared with the original hash values to verify integrity.

Tech Stack:

    • Language: Python
    • Libraries: hashlib for hash calculation, argparse for command-line interface
