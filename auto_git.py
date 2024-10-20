import subprocess

def git_add_commit_push(commit_message):
    try:
        # Stage all changes (equivalent to git add .)
        subprocess.run(["git", "add", "."], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to stage changes: {e}")
        return

    try:
        # Commit with the given message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to commit changes: {e}")
        return

    try:
        # Push changes to the remote repository (default branch)
        subprocess.run(["git", "push"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to push changes: {e}")
        return

if __name__ == "__main__":
    # Example commit message
    commit_message = "Automated commit message"
    git_add_commit_push(commit_message)