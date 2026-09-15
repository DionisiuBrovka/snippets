# Snippets

Небольшие полезные скрипты и утилиты для повседневных задач.

## Что внутри

| Скрипт | Описание |
| --- | --- |
| [download-video-insta](./download-video-insta/) | CLI-утилита для скачивания публичных Instagram Reels по ссылке. |

## `download-video-insta`

Консольная утилита для скачивания публичных Instagram Reels по ссылке. Видео сохраняется локально в `downloads`; для доступных вашему аккаунту публикаций поддерживаются cookies из браузера.

```bash
cd download-video-insta && pipx install .
download-reel "https://www.instagram.com/reel/<id>/"
```

Полный список параметров и примеры — в [README скрипта](./download-video-insta/README.md).

## Структура

Каждая утилита живёт в собственной папке вместе с кодом и зависимостями. По мере появления новых скриптов они будут добавляться в таблицу выше.
