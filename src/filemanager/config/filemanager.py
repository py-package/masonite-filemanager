"""filemanager Settings"""

"""
|--------------------------------------------------------------------------
| A Heading of The Setting Being Set
|--------------------------------------------------------------------------
|
| A quick description
|
"""

DRIVER = "local"  # local or s3

PATHS = {
    'files': '/mnt/internal-storage/development_internal_ssd/wyndham/storage/files/',
    'uploads': '/mnt/internal-storage/development_internal_ssd/wyndham/storage/files/filemanager/',
    # Path to generated image previews for non-image files (pdf, mp3, etc..)
    'previews': '/mnt/internal-storage/development_internal_ssd/wyndham/storage/files/previews/',
}

GENERATE_PREVIEWS = False
