"""
Git Certification Practice Exercises
For Intocode Weiterbildung
"""

def exercise1():
    """Basic Git commands."""
    commands = {
        'status': 'Check repository status',
        'add': 'Stage changes',
        'commit': 'Save changes',
        'push': 'Upload to remote',
        'pull': 'Download from remote',
        'branch': 'Work with branches'
    }
    for cmd, desc in commands.items():
        print(f"git {cmd:10} - {desc}")

if __name__ == "__main__":
    exercise1()
