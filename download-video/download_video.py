#!/usr/bin/env python3
"""CLI для скачивания видео из социальных сетей по ссылке."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

import click


BROWSERS = ("chrome", "firefox", "edge", "brave", "opera", "safari", "vivaldi")


def video_url(_ctx: click.Context, _param: click.Parameter, value: str) -> str:
    """Проверяет URL, оставляя определение площадки yt-dlp."""
    value = value.strip()
    try:
        parsed = urlparse(value)
        valid = (
            parsed.scheme in {"http", "https"}
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
            and not any(char.isspace() for char in value)
        )
        parsed.port  # Проверить корректность номера порта.
    except ValueError:
        valid = False
    if not valid:
        raise click.BadParameter("укажите полную ссылку на видео: https://...")
    return value


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("url", callback=video_url)
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(path_type=Path, file_okay=False, writable=True),
    default=Path("downloads"),
    show_default=True,
    help="Каталог, в который будет сохранено видео.",
)
@click.option(
    "--cookies-from-browser",
    type=click.Choice(BROWSERS, case_sensitive=False),
    help="Взять cookies из браузера для контента, доступного вашему аккаунту.",
)
@click.option("--quiet", is_flag=True, help="Не выводить ход загрузки yt-dlp.")
@click.version_option(version="0.1.0")
def main(url: str, output_dir: Path, cookies_from_browser: str | None, quiet: bool) -> None:
    """Скачать видео по URL; социальная сеть определяется автоматически.

    Видео сохраняется в OUTPUT_DIR. Используйте только для материалов,
    к которым у вас есть законный доступ.
    """
    try:
        from yt_dlp import DownloadError, YoutubeDL
    except ModuleNotFoundError:
        raise click.ClickException(
            "Не найдена библиотека yt-dlp. Установите зависимости: "
            "python -m pip install -r requirements.txt"
        )

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise click.ClickException(f"Не удалось создать каталог: {exc}") from exc

    options: dict = {
        "outtmpl": str(output_dir / "%(extractor)s - %(title).150B [%(id)s].%(ext)s"),
        "format": "bv*+ba/b",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "playlist_items": "1",  # Для публикаций с несколькими видео.
        "ignoreerrors": False,
        "js_runtimes": {"deno": {}, "node": {}},
        "restrictfilenames": True,
        "windowsfilenames": True,
        "quiet": quiet,
    }
    if cookies_from_browser:
        options["cookiesfrombrowser"] = (cookies_from_browser,)

    try:
        with YoutubeDL(options) as ydl:
            status = ydl.download([url])
            if status:
                raise click.ClickException("Загрузка завершилась с ошибкой.")
    except (DownloadError, OSError) as exc:
        raise click.ClickException(
            f"Не удалось скачать видео: {exc}\n"
            "Проверьте ссылку, доступность видео и обновите yt-dlp. Для доступного вам "
            "контента можно попробовать --cookies-from-browser chrome."
        )

    click.echo(f"Готово. Файл сохранён в: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
