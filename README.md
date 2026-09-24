# Snippets

Небольшие полезные скрипты и утилиты для повседневных задач.

## Что внутри

| Скрипт | Описание |
| --- | --- |
| [download-video](./download-video/) | Скачивание вертикальных видео из соцсетей с автоматическим определением источника по ссылке. |

## `short-video-download`

Общая CLI-утилита для Instagram Reels, YouTube Shorts, TikTok, VK Клипов
и других площадок, поддерживаемых yt-dlp. Заменяет отдельные сниппеты Instagram и YouTube.

```bash
cd download-video
pipx install .
short-video-download "https://www.youtube.com/shorts/Zga3CdIRGrw"
```

Требования, параметры и примеры — в [README скрипта](./download-video/README.md).

## Структура

Каждая утилита живёт в собственной папке вместе с кодом и зависимостями.
