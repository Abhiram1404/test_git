import subprocess

def git_add_commit_push(commit_message, branch_name):
    # Stage all changes (equivalent to git add .)
    add_process = subprocess.run(["git", "add", "."], capture_output=True, text=True)
    if add_process.returncode != 0:
        print(f"Failed to add changes: {add_process.stderr}")
        return
    
    # Commit with the given message
    commit_process = subprocess.run(["git", "commit", "-m", commit_message], capture_output=True, text=True)
    if commit_process.returncode != 0:
        print(f"Failed to commit changes: {commit_process.stderr}")
        return
    
    # Push changes to the specific branch of the remote repository
    push_process = subprocess.run(["git", "push", "origin", branch_name], capture_output=True, text=True)
    if push_process.returncode != 0:
        print(f"Failed to push changes: {push_process.stderr}")
        return
    
    print(f"Changes successfully pushed to branch '{branch_name}' with message: {commit_message}")

if __name__ == "__main__":
    # Example commit message and branch name
    commit_message = "Automated commit message"
    branch_name = "feature-branch"  # Replace with your branch name
    git_add_commit_push(commit_message, branch_name)