# Instagram Reel downloader

Небольшая консольная утилита для сохранения публичных Instagram Reels, к которым у вас есть законный доступ.

## Установка

```bash
pipx install .
```

## Использование

```bash
download-reel "https://www.instagram.com/reel/ABC123/"
```

Видео сохраняется в каталог `downloads`. Указать другой каталог:

```bash
download-reel -o videos "https://www.instagram.com/reel/ABC123/"
```

Если Instagram требует входа, и публикация доступна вашему аккаунту, можно использовать cookies из локального браузера:

```bash
download-reel --cookies-from-browser chrome "https://www.instagram.com/reel/ABC123/"
```

Справка по всем параметрам:

```bash
download-reel --help
```

Не используйте утилиту для обхода ограничений доступа и соблюдайте права автора и правила Instagram.
