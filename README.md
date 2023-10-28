# YouTube Media Downloader

YouTube Media Downloader allows users to download audio from YouTube. Whether it's a single video or an entire playlist, this tool is designed to make the process seamless. With both GUI and CLI options, you can choose the interface that's most comfortable for you.

![demo-start]
![demo-success]

---

## Table of Contents
- [YouTube Media Downloader](#youtube-media-downloader)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Latest Release](#latest-release)
  - [Usage](#usage)
    - [GUI](#gui)
    - [CLI](#cli)
  - [Packaging](#packaging)
  - [Future Work](#future-work)
    - [TODO](#todo)
    - [Feature ideas:](#feature-ideas)
  - [License](#license)

---

## Features

- Download audio from individual videos.
- Download audio from entire playlists.
  - Option to segregate videos into separate folders based on the YT channel.
- Intuitive GUI for ease of use.
- CLI for users who prefer command line operations.

---

## Installation

1. Ensure you have Python 3.11 and Poetry installed.
2. Clone the repository:
```bash
$ git clone https://github.com/vmariiechko/youtube-media-downloader.git
```
3. Navigate to the project directory:
```bash
cd youtube-media-downloader
```
4. Set up the virtual environment and install dependencies:
```bash
poetry install
```

---

## Latest Release

Download the initial release of YouTube Media Downloader - v1.0.0 from [here][releases-url].

---

## Usage

### GUI
Start the GUI application:
```bash
python -m youtube_media_downloader.gui.main
```

### CLI
1. For individual videos:
```
python -m youtube_media_downloader.cli.main video --url "https://www.youtube.com/watch?v=XraHq2j2yps"
```
2. For playlists:
```
python -m youtube_media_downloader.cli.main playlist \
    --url "https://www.youtube.com/playlist?list=PLhvGGyZjDqHrmlkJESdvuJkdNvTJnDQ8N" \
    --separate_channel_folders
```

---

## Packaging
To package the GUI application for distribution, run:
```bash
python package.py
```

---

## Future Work

### TODO
- Validate whether a playlist is private and handle it accordingly.
- Handle cases where users select to download a playlist, but the provided link is for an individual video.

### Feature ideas:
- Enable users to filter videos from a playlist based on their titles:
  - Download videos that start with a specified text.
  - Download videos containing a specified text in their title.
- Allow users to specify a range of videos from a playlist for downloading, indicating a start and end point.

---

## License

>You can check out the full license [here][license-url].

This project is licensed under the terms of the **MIT** license.

---

> Gmail [vmariiechko@gmail.com](mailto:vmariiechko@gmail.com) &nbsp;&middot;&nbsp;
> GitHub [@vmariiechko](https://github.com/vmariiechko) &nbsp;&middot;&nbsp;
> LinkedIn [@mariiechko](https://www.linkedin.com/in/mariiechko/)


<!-- Markdown links and images -->
[license-url]: https://github.com/vmariiechko/youtube-media-downloader/blob/main/LICENSE
[releases-url]: https://github.com/vmariiechko/youtube-media-downloader/releases/tag/v1.0.0

[demo-start]: https://imgur.com/TeJZLuE.png
[demo-success]: https://imgur.com/lSOsHCS.png