import requests

def import_gists_to_database(db, username, commit=True):
    resp = requests.get('https://api.github.com/users/{}/gists'.format(username))
    if resp.status_code != 200:
        raise requests.HTTPError()
    dict_resp = resp.json()
    c = 1
    for gist in dict_resp:
        db.execute('insert into gists values (?,?,?,?,?,?,?,?,?,?,?,?)',(c,gist['id'],gist['html_url'],gist['git_pull_url'],gist['git_push_url'],gist['commits_url'],gist['forks_url'],gist['public'],gist['created_at'],gist['updated_at'],gist['comments'],gist['comments_url']))
        c += 1
    if commit:
        db.commit()