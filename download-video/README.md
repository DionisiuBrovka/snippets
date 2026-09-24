# Social video downloader

Общий сниппет для скачивания вертикальных роликов: Instagram Reels, YouTube
Shorts, TikTok, VK Клипы, Facebook Reels и видео с других площадок,
[поддерживаемых yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).
Источник определяется по ссылке самим yt-dlp, включая поддерживаемые короткие
ссылки и перенаправления. Отдельно выбирать соцсеть не нужно.
Доступность конкретной публикации зависит от площадки, региона и авторизации.

## Установка

Нужны Python 3.10+, `ffmpeg` для объединения видео со звуком и Deno либо
Node.js для YouTube ([требования yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/EJS)).

```bash
cd download-video
pipx install .
```

Или через виртуальное окружение:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python download_video.py "https://www.youtube.com/shorts/Zga3CdIRGrw"
```

## Использование

```bash
short-video-download "https://www.youtube.com/shorts/Zga3CdIRGrw"
short-video-download "https://www.instagram.com/reel/ABC123/"
short-video-download "https://www.tiktok.com/@username/video/1234567890123456789"
short-video-download "https://vk.com/clip-123456_456789012"
short-video-download -o videos "https://youtu.be/Zga3CdIRGrw"
short-video-download --cookies-from-browser firefox "https://www.instagram.com/reel/ABC123/"
short-video-download --quiet "https://www.youtube.com/shorts/Zga3CdIRGrw"
short-video-download --help
```

Ссылки Instagram, TikTok и VK выше иллюстративные — замените их своими.
По умолчанию файлы сохраняются в `downloads` относительно текущего каталога.
Выбирается лучшее доступное качество; раздельные дорожки объединяются в MP4.
Если скачивается готовый файл со звуком, его контейнер сохраняется.
Пропорции остаются исходными: вертикальные видео не обрезаются, горизонтальные
тоже принимаются. Ограничения длительности нет.

Передавайте ссылку на конкретный ролик, а не на профиль или подборку.
Плейлист из ссылки на отдельное видео игнорируется; если сама ссылка возвращает
список (например, публикация с несколькими роликами), берётся только первый элемент.
Параметры URL сохраняются, поскольку могут требоваться для доступа к видео.

Cookies из браузера можно использовать для публикаций, доступных вашему аккаунту.
При ошибках сначала проверьте ссылку в браузере и обновите yt-dlp:

```bash
pipx runpip social-video-downloader install -U 'yt-dlp[default]'
```

Для виртуального окружения: `.venv/bin/python -m pip install -U -r requirements.txt`.

Этот сниппет заменяет `download-video-insta` и `download-video-youtube`.
Если старые команды установлены через pipx, удалить их можно отдельно:

```bash
pipx uninstall instagram-reel-downloader
pipx uninstall youtube-shorts-downloader
```
