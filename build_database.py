import sqlite_utils
import git
import json


def iterate_file_versions(repo_path, filepath, ref="main"):
    repo = git.Repo(repo_path, odbt=git.GitDB)
    commits = reversed(list(repo.iter_commits(ref, paths=filepath)))
    for commit in commits:
        blob = [b for b in commit.tree.blobs if b.name == filepath][0]
        yield commit.committed_datetime, commit.hexsha, blob.data_stream.read()


if __name__ == "__main__":
    it = iterate_file_versions(".", "states.json")
    count = 0
    db = sqlite_utils.Database("cdc.db")
    for i, (when, hash, content) in enumerate(it):
        try:
            states = json.loads(content)["vaccination_data"]
        except ValueError:
            # Bad JSON
            continue
        for state in states:
            id = state["Location"] + "-" + state["Date"]
            db["daily_reports"].insert(
                dict(state, id=id), pk="id", alter=True, replace=True
            )
