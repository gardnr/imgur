# Imgur exporter

Uploads to a certian album using the Imgur API

[API client docs](https://github.com/Imgur/imgurpython)

```
python3 -m pip install -r requirements.txt

gardnr add driver imgur imgur.driver:Imgur -c client_id=<client id> client_secret=<client secret> refresh_token=<refresh token> album_id=<album id>
```
