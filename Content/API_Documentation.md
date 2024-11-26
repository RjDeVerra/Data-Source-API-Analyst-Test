# GitHub API Documentation

## Search Repositories
- **Endpoint**: `GET https://api.github.com/search/repositories`
- **Parameters**:
  - `q`: Search query (e.g., "machine learning").
  - `sort`: Sort by stars, forks, or other fields.
  - `order`: Sort order ("asc" or "desc").
  - **Example**: `https://api.github.com/search/repositories?q=machine+learning&sort=stars&order=desc`

## Retrieve Commits
- **Endpoint**: `GET https://api.github.com/repos/{owner}/{repo}/commits`
- **Parameters**:
  - `since`: Start date for filtering commits (e.g., `2024-11-01`).
  - **Example**: `https://api.github.com/repos/tensorflow/tensorflow/commits?since=2024-11-01`

## Retrieve Contents
- **Endpoint**: `GET https://api.github.com/repos/{owner}/{repo}/contents`
- **Parameters**:
  - `path`: Path to the file or directory in the repository.
  - **Example**: `https://api.github.com/repos/tensorflow/tensorflow/contents/requirements_lock_3_10.txt`
