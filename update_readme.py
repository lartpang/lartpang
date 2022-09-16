import pathlib
import re

import feedparser


def replace_writing(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = "\n{}\n".format(chunk)
    chunk = "<!-- {} starts -->{}<!-- {} ends -->".format(marker, chunk, marker)
    return r.sub(chunk, content)


def fetch_writing():
    rss_info = feedparser.parse("https://blog.csdn.net/p_lart/rss/list")
    entries = rss_info["entries"]
    recent_entries = entries[:10]

    return [
        {
            "title": entry["title"],
            "url": entry["link"],
            "published": re.findall(r"(.*?)\s\d{2}:", entry["published"])[0],
            "summary": entry["summary"],
        }
        for entry in recent_entries
    ]


if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.resolve()
    readme_path = root / "README.md"
    readme = readme_path.open(encoding="utf-8", mode="r").read()

    entries = fetch_writing()
    entries_md = "\n".join(
        [
            "* [{title}]({url}) - {published}: <small>*{summary}*</small>".format(
                **entry
            )
            for entry in entries
        ]
    )
    print("Information from RSS:\n", entries_md)

    # Update entries
    readme = replace_writing(readme, "writing", entries_md)
    readme_path.open(encoding="utf-8", mode="w").write(readme)
