# YouTube Shorts downloader

Консольная утилита для скачивания YouTube Shorts по ссылке, аналог `download-reel`.

## Установка

Нужны Python 3.10+, `ffmpeg` для объединения видео со звуком и актуальный
Deno или Node.js для JavaScript-проверок YouTube. Скрипт включает оба runtime;
yt-dlp выбирает доступный. Подробнее: [требования yt-dlp](https://github.com/yt-dlp/yt-dlp/wiki/EJS).

```bash
pipx install .
```

Или установка в виртуальное окружение:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python download_short.py "https://www.youtube.com/shorts/Zga3CdIRGrw"
```

## Использование

```bash
download-short "https://www.youtube.com/shorts/Zga3CdIRGrw"
download-short -o videos "https://www.youtube.com/shorts/Zga3CdIRGrw"
download-short --cookies-from-browser chrome "https://www.youtube.com/shorts/Zga3CdIRGrw"
download-short --quiet "https://www.youtube.com/shorts/Zga3CdIRGrw"
download-short --help
```

По умолчанию видео сохраняется в `downloads` относительно текущего каталога.
Выбирается лучшее доступное качество; отдельные видео и звук объединяются
в MP4. Ссылки с параметрами отслеживания принимаются, параметры удаляются.

Cookies можно передать, если YouTube требует входа и видео доступно вашему аккаунту.

При ошибках из-за изменений YouTube обновите зависимости:

```bash
pipx upgrade youtube-shorts-downloader
```

Для виртуального окружения: `.venv/bin/python -m pip install -U -r requirements.txt`.
