#!/usr/bin/env python3
"""CLI для скачивания публичных Instagram Reels по ссылке."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import urlparse

import click


BROWSERS = ("chrome", "firefox", "edge", "brave", "opera", "safari", "vivaldi")


def reel_url(_ctx: click.Context, _param: click.Parameter, value: str) -> str:
    """Проверяет, что передана ссылка Instagram Reel."""
    parsed = urlparse(value)
    host = (parsed.hostname or "").lower()
    is_instagram = host == "instagram.com" or host.endswith(".instagram.com")
    is_reel = parsed.path.lower().startswith("/reel/")
    if parsed.scheme not in {"http", "https"} or not is_instagram or not is_reel:
        raise click.BadParameter("укажите ссылку вида https://www.instagram.com/reel/<id>/")
    return value


@click.command(context_settings={"help_option_names": ["-h", "--help"]})
@click.argument("url", callback=reel_url)
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
@click.version_option()
def main(url: str, output_dir: Path, cookies_from_browser: str | None, quiet: bool) -> None:
    """Скачать публичный Instagram REEL по URL.

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

    output_dir.mkdir(parents=True, exist_ok=True)

    options: dict = {
        "outtmpl": str(output_dir / "%(uploader)s - %(title)s [%(id)s].%(ext)s"),
        "format": "bv*+ba/b",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "restrictfilenames": True,
        "windowsfilenames": True,
        "quiet": quiet,
    }
    if cookies_from_browser:
        options["cookiesfrombrowser"] = (cookies_from_browser,)

    try:
        with YoutubeDL(options) as ydl:
            ydl.download([url])
    except DownloadError as exc:
        raise click.ClickException(
            f"Не удалось скачать Reel: {exc}\n"
            "Проверьте ссылку и доступность публикации. Для доступного вам "
            "контента можно попробовать --cookies-from-browser chrome."
        )

    click.echo(f"Готово. Файл сохранён в: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
