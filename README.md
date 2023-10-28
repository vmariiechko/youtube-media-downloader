# YouTube Media Downloader

## TODO
* Check if playlist is private
* Handle case when selected to download playlist, but provided link was video

## Feature ideas:
* Allow users to download videos from a provided playlist link based on:
  * Videos that start with the specified text.
  * Videos that contain the specified text in their title.
* Enable downloading a range of videos from a playlist by specifying a start and end point.


## Usage
* Install venv using poetry: `poetry install`
* To start GUI, from project root run:
```
python -m youtube_media_downloader.gui.main
```
* To run CLI, from project root run:
```
python -m youtube_media_downloader.cli.main video --url "https://www.youtube.com/watch?v=XraHq2j2yps"
# or
python -m youtube_media_downloader.cli.main playlist \
    --url "https://www.youtube.com/playlist?list=PLhvGGyZjDqHrmlkJESdvuJkdNvTJnDQ8N" \
    --separate_channel_folders
```
