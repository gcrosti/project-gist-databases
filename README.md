Gist Database
===============

This was a project I completed as part of a Data Science course at RMOTR. For this assignment I built a Importer function to pull data from an API, and a Search function to search for specific items in the API data. More details below.

Example:
* Guido's HTML Gists: [https://gist.github.com/gvanrossum](https://gist.github.com/gvanrossum)
* Guido's API Gists: [https://api.github.com/users/gvanrossum/gists](https://api.github.com/users/gvanrossum/gists)

## Tests

Tests are all under `tests/`. We some fixtures and mocking to make testing fast and remove side effects. Don't worry if you don't understand it now. You can just focus on reading the actual test functions. If you feel lost and need to print something out in the screen, you can use the `main.py` script. It's using the testing database. The same one used for `test_search.py`.

## The Importer
Your `import_gists_to_database` function will take three parameters:

 - `db`: The database object to connect to
 - `username`: The GitHub user whose gists we are going to retrieve
 - `commit` *(Optional, defaults to `True`)*: If `True`, automatically commit changes to database

You are going to use the [GitHub gists API](https://developer.github.com/v3/gists/) to retrieve the gists of a given user, insert those gists into a database (schema may be found in the `schema.sql` file), and if `commit` is True, commit those changes to the database.

## The Searcher

Your `search_gists` method should take a `db_connection` parameter (the database connection), as well as two **optional** arguments:
- `github_id`
- `created_at`

If no parameter is provided, all the gists in the database should be returned. If `public_id` or `created_at` parameters are provided, you should filter your SELECT query based on them.
