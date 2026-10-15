"""Entry point for SentinelPass."""
from ui.main_window import SentinelPassApp


def main() -> None:
    app = SentinelPassApp()
    app.mainloop()


if __name__ == "__main__":
    main()
