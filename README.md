# Snippets

Небольшие полезные скрипты и утилиты для повседневных задач.

## Что внутри

| Скрипт | Описание |
| --- | --- |
| [download-video-insta](./download-video-insta/) | CLI-утилита для скачивания публичных Instagram Reels по ссылке. |

## `download-video-insta`

Скачивает видео из публичного Instagram Reel и сохраняет его в локальную папку.

> Используйте инструмент только для материалов, к которым у вас есть законный доступ, и с соблюдением правил Instagram.

### Требования

- Python 3.10 или новее
- `pip`

### Установка

```bash
cd download-video-insta
python -m pip install -r requirements.txt
```

### Использование

```bash
python download_reel.py https://www.instagram.com/reel/<id>/
```

По умолчанию видео попадёт в каталог `downloads` внутри текущей папки.

#### Полезные опции

```bash
# Сохранить в выбранную папку
python download_reel.py <URL> --output-dir ~/Videos/reels

# Использовать cookies из браузера для доступного вашему аккаунту контента
python download_reel.py <URL> --cookies-from-browser chrome

# Показать все параметры
python download_reel.py --help
```

Поддерживаются браузеры: Chrome, Firefox, Edge, Brave, Opera, Safari и Vivaldi.

## Структура

Каждая утилита живёт в собственной папке вместе с кодом и зависимостями. По мере появления новых скриптов они будут добавляться в таблицу выше.
