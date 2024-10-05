
To develop a tool that calculates cryptographic hash values for digital evidence files. Hash values are used to confirm the integrity of files, 
ensuring that no changes have been made from the original during the process of investigation or during data transfer. 
The hashes are unique fingerprints of files, and even a small change in the file content will produce a completely different hash value.

How It Works:

The user provides a file as input.
The tool calculates the MD5 and SHA-256 hash values for the file.
These hash values can then be compared with the original hash values to verify integrity.
Tech Stack:

Techstack : 
          Python
          Libraries: hashlib for hash calculation, argparse for command-line interface

The Digital Evidence Integrity Checker is a simple but crucial tool in the digital forensic process. 
It ensures that evidence remains unchanged throughout an investigation, which is key to maintaining its admissibility in legal proceedings. 
This Python implementation is a great starting point for building more sophisticated tools for digital forensic tasks.






