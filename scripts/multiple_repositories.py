import os
import shutil
from git import Repo
from scripts.get_repo_name import get_repo_name_from_url

def multiple_repositories():
    repo_urls = [
        "",
    ] # Introduce the repositories URL's

    base_path = r"" # Introduce the path where you would like to locate your repositories

    for repo_url in repo_urls:
        repo_name = get_repo_name_from_url(repo_url)
        full_path_to_clone = os.path.join(base_path, repo_name)

        if os.path.exists(full_path_to_clone):
            print(f"Deleting the existing directory in {full_path_to_clone}...")
            try:
                shutil.rmtree(full_path_to_clone)
                print("Directory deleted.")
            except Exception as e:
                print(f"The directory could not be deleted: {e}")

        os.makedirs(base_path, exist_ok=True)

        try:
            print(f"Cloning the repository {repo_url} in {full_path_to_clone}...")
            Repo.clone_from(repo_url, full_path_to_clone)
            print("Repository successfully cloned.")
        except Exception as e:
            print(f"An error occurred while cloning the repository {repo_url}: {e}")