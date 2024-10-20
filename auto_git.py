import subprocess

def git_add_commit_push(commit_message):
    try:
        # Stage all changes (equivalent to git add .)
        result_add = subprocess.run(["git", "add", "."], check=True)
        
        # Commit with the given message
        result_commit = subprocess.run(["git", "commit", "-m", commit_message], check=True)
        
        # Push changes to the remote repository (default branch)
        result_push = subprocess.run(["git", "push"], check=True)
        
        print("Changes were added, committed, and pushed successfully.")
        
    except subprocess.CalledProcessError as e:
        # Handle errors in the subprocess
        print(f"An error occurred: {e}")
        if e.returncode == 1:
            print("Failed to add changes. Make sure there are changes to commit.")
        elif e.returncode == 2:
            print("Commit failed. Make sure your commit message is not empty.")
        elif e.returncode == 128:
            print("Push failed. Check if remote repository is accessible.")
        else:
            print("An unknown error occurred.")

if __name__ == "__main__":
    # Example commit message
    commit_message = "Automated commit message"
    git_add_commit_push(commit_message)