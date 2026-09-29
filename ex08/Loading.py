import os


def ft_tqdm(lst: range) -> None:
    """Yield the items of lst while printing a progress bar."""
    total = len(lst)
    try:
        width = os.get_terminal_size().columns
    except OSError:
        width = 80
    bar_width = max(width - len(f"100%|[]| {total}/{total}"), 0)
    for i, item in enumerate(lst, 1):
        yield item
        percent = i * 100 // total
        filled = bar_width * i // total
        bar = "=" * (filled - 1) + ">" if filled else ""
        print(f"\r{percent:3d}%|[{bar:<{bar_width}}]| {i}/{total}",
              end="", flush=True)
