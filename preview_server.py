#!/usr/bin/env python3
"""Serve the static resume locally for browser preview."""

from __future__ import annotations

import argparse
import http.server
import threading
import webbrowser
from pathlib import Path


class PreviewHandler(http.server.SimpleHTTPRequestHandler):
    """Static file handler with cache disabled for rapid local edits."""

    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="interface to bind to (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="port to serve on (default: 8000)",
    )
    parser.add_argument(
        "--open",
        action="store_true",
        help="open the preview URL in the default browser",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    root = Path(__file__).resolve().parent
    handler = lambda *handler_args, **handler_kwargs: PreviewHandler(  # noqa: E731
        *handler_args,
        directory=str(root),
        **handler_kwargs,
    )

    with http.server.ThreadingHTTPServer((args.host, args.port), handler) as server:
        host = "localhost" if args.host in {"127.0.0.1", "::1"} else args.host
        url = f"http://{host}:{server.server_port}/"
        print(f"Serving {root}")
        print(f"Preview: {url}")
        print("Press Ctrl+C to stop.")

        if args.open:
            threading.Timer(0.2, webbrowser.open, args=(url,)).start()

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview server stopped.")


if __name__ == "__main__":
    main()
