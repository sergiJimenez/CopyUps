def get_repo_name_from_url(url):
    return url.rstrip('/').split('/')[-1].replace('.git', '')