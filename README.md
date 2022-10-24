# filemanager

<p align="center">
<img src="https://banners.beyondco.de/Masonite%20Filemanager.png?theme=light&packageManager=pip+install&packageName=masonite-filemanager&pattern=charlieBrown&style=style_2&description=File+management+solution+for+Masonite&md=1&showWatermark=1&fontSize=100px&images=adjustments&widths=50&heights=50">
</p>

<p align="center">
  
  <img alt="GitHub Workflow Status" src="https://github.com/py-package/masonite-filemanager/actions/workflows/python-package.yml/badge.svg">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-filemanager">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/py-package/masonite-filemanager">
  <img alt="License" src="https://img.shields.io/github/license/py-package/masonite-filemanager">
  <a href="https://github.com/py-package/masonite-filemanager/stargazers"><img alt="star" src="https://img.shields.io/github/stars/py-package/masonite-filemanager" /></a>
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Introduction

A simple yet powerful file management solution for your masonite application.

## Features

- [x] Manager Server Files (Currently only supports local files)
- [x] Upload Files
- [x] Preview Files
- [x] Rename Files/Folders
- [x] Delete Files/Folders
- [x] Download Files
- [x] Search Files
- [ ] Protect Routes
- [ ] Image Editing
- [ ] Third Party Driver Support (S3, DigitalOcean Space, etc)
- [x] File Picker (Form)

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

If you want to use file picker then all you have to do is include then follow the following guidelines:

1. Add style in the header of your base template:
   ```html
   <link href="/filemanager-assets/picker.css" rel="stylesheet" />
   ```
2. Add script before the `</body>` tag of your base template:
   ```html
   <script src="/filemanager-assets/picker.js"></script>
   ```
3. Finally, in your form you can use selector in your form in the following way:
   ```html
   <div class="file-picker">
     <input type="hidden" name="j-sukai" />
   </div>
   ```
   or, if you want file-preview:
   ```html
   <div class="file-picker has-preview">
     <input type="hidden" name="j-sukai" />
   </div>
   ```

The design of the file-picker is very basic so you might want to customize with your own design by modifying the stylesheet which resides in `storage/vendor/filemanager` directory.

## License

masonite-filemanager is open-sourced software licensed under the [MIT license](LICENSE).
