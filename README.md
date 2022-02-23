# filemanager

<p align="center">
    <img src="https://banners.beyondco.de/filemanager.png?theme=light&packageManager=pip+install&packageName=masonite-filemanager&pattern=topography&style=style_1&description=File management solution for Masonite&md=1&showWatermark=1&fontSize=100px&images=https%3A%2F%2Fgblobscdn.gitbook.com%2Fspaces%2F-L9uc-9XAlqhXkBwrLMA%2Favatar.png">
</p>

<p align="center">
  
  <img alt="GitHub Workflow Status" src="https://github.com/yubarajshrestha/masonite-filemanager/actions/workflows/python-package.yml/badge.svg">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-filemanager">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/yubarajshrestha/masonite-filemanager">
  <img alt="License" src="https://img.shields.io/github/license/yubarajshrestha/masonite-filemanager">
  <a href="https://github.com/yubarajshrestha/masonite-filemanager/stargazers"><img alt="star" src="https://img.shields.io/github/stars/yubarajshrestha/masonite-filemanager" /></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Introduction

A simple yet powerful file management solution for your masonite application.

## Features

- [x] Manager Server Files (Currently only supports local files)
- [x] Upload Files
- [x] Preview Files
- [x] Rename Files/Folders
- [x] Delete Files
- [x] Download Files
- [ ] Move Files
- [ ] Protect Routes
- [ ] FileManager FormField
- [ ] Image Editing
- [ ] Third Party Driver Support (S3, DigitalOcean Space, etc)

## Installation

```bash
pip install masonite-filemanager
```

## Configuration

Add FileManagerProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from filemanager.providers import FileManagerProvider

# ...
PROVIDERS = [
    # ...
    # Third Party Providers
    FileManagerProvider,
    # ...
]
```

Then you can publish the package resources (if needed) by doing:

```bash
python craft package:publish filemanager
```

Finally add following to `STATICFILES` section in `config/filesystem.py`:

```python
# config/filesystem.py

STATICFILES = {
    # ...
    # FileManager resources
    'resources/vendor/filemanager': 'filemanager-assets/',
    "storage/framework/filesystem/filemanager": "filemanager-uploads/",
}
```

## Usage

Once finishing configurations, you can access the file manager by using the following route:

`http://localhost:8000/filemanager`

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## Maintainers

- [Yubaraj Shrestha](https://www.github.com/yubarajshrestha)

## License

masonite-filemanager is open-sourced software licensed under the [MIT license](LICENSE).
