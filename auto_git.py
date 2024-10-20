import subprocess

def git_add_commit_push(commit_message):
    try:
        # Stage all changes (equivalent to git add .)
        subprocess.run(["git", "add", "."], check=True)
        
        # Commit with the given message
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push changes to the remote repository (default branch)
        subprocess.run(["git", "push"], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while executing Git commands: {e}")
        return False  # Indicate failure

    return True  # Indicate success

if __name__ == "__main__":
    # Example commit message
    commit_message = "Automated commit message"
    success = git_add_commit_push(commit_message)

    if not success:
        print("Failed to add, commit, or push changes.")
    else:
        print("Changes were successfully added, committed, and pushed.")