(() => {
    let index = 0;
    const FilePickers = document.querySelectorAll(".file-picker");

    window.fmanager = function (element, callback) {
        if (!element) return;
        window.open('/filemanager/picker', 'File Picker',
            'height=400,width=1200,toolbar=no,directories=no,status=no, linemenubar=no,scrollbars=no,resizable=no ,modal=yes');

        if (!window.SetUrl) {
            window.SetUrl = function (url) {
                callback(url, element);
            }
        }
    }

    const SelectorTemplate = `
        <span class="picker">
          Select File
        </span>
      `;

    const PreviewTemplate = `
        <span class="preview">
          <img src="IMAGE_URL">
        </span>
        <span class="close">x</span>
      `;

    const SetPreview = (file) => {
        if (FilePickers[index].classList.contains('has-preview')) {
            const close = FilePickers[index].querySelector('.close')
            if (close) close.remove()
            const preview = FilePickers[index].querySelector('.preview')
            if (preview) preview.remove()
            const PreviewElement = PreviewTemplate.replace("IMAGE_URL", file)
            FilePickers[index].insertAdjacentHTML("beforeend", PreviewElement);
        }
    }

    const PickFile = () => {
        fmanager(FilePickers[index], function (file, target) {
            FilePickers[index].querySelector('input').value = file;
            SetPreview(file);
        });
    }

    FilePickers.forEach(function (fp, i) {
        fp.insertAdjacentHTML("beforeend", SelectorTemplate)
        fp.addEventListener('click', function (e) {
            index = i;
            if (e.target.classList.contains('close')) {
                FilePickers[index].querySelector('.close').remove()
                FilePickers[index].querySelector('.preview').remove()
                FilePickers[index].querySelector('input').value = '';
            } else {
                PickFile(FilePickers[index])
            }
        })
    })
})();