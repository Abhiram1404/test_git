import subprocess

def git_add_commit_push(commit_message):
    # Stage all changes (equivalent to git add .)
    subprocess.run(["git", "add", "."])
    
    # Commit with the given message
    subprocess.run(["git", "commit", "-m", commit_message])
    
    # Push changes to the remote repository (default branch)
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    # Example commit message
    commit_message = "Automated commit message"
    git_add_commit_push(commit_message)
