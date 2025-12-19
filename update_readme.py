import html
import pathlib
import re
import time

import feedparser


def clean_summary(text):
    """
    清洗 RSS 摘要：去除 HTML 标签、修复转义字符、去除换行
    """
    if not text:
        return ""
    # 1. 去除 HTML 标签
    text = re.sub(r"<[^>]+>", "", text)
    # 2. 修复实体字符 (如 &gt; -> >)
    text = html.unescape(text)
    # 3. 去除换行符，防止破坏 Markdown 表格或列表结构
    text = text.replace("\n", " ").replace("\r", "")
    # 4. 移除多余空格
    text = re.sub(r"\s+", " ", text).strip()
    return text


def fetch_rss_data(num_entries=10):
    """
    获取 RSS 数据并返回前 5 条
    """
    rss_url = "https://rss.csdn.net/P_LarT/rss/map"
    print(f"DEBUG: Fetching RSS from {rss_url}...")

    try:
        # feedparser 自带容错，但为了保险起见加 try-except
        feed = feedparser.parse(rss_url)
    except Exception as e:
        print(f"ERROR: Failed to fetch RSS: {e}")
        return []

    if not feed.entries:
        print("WARN: RSS feed is empty.")
        return []

    return feed.entries[:num_entries]


def generate_content(entries):
    """
    将 RSS 条目转换为 Markdown 列表字符串
    """
    lines = []
    for entry in entries:
        # 处理日期：优先使用解析后的结构化时间
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            date_str = time.strftime("%Y-%m-%d", entry.published_parsed)
        else:
            date_str = entry.get("published", "")[:10]

        # 处理摘要
        summary = clean_summary(entry.get("summary", ""))
        if len(summary) > 80:  # 限制摘要长度
            summary = summary[:80] + "..."

        # 格式化行
        line = f"* [{entry.title.strip()}]({entry.link}) - {date_str}: <small>*{summary}*</small>"
        lines.append(line)

    # 返回拼接好的文本，首尾不加换行符，由替换逻辑控制
    return "\n".join(lines)


if __name__ == "__main__":
    # 1. 定位 README 文件
    root = pathlib.Path(__file__).parent.resolve()
    readme_path = root / "README.md"
    readme_content = readme_path.read_text(encoding="utf-8")

    # 2. 定义特定的标记
    start_marker = "<!-- BEGIN_RECENT_WRITING -->"
    end_marker = "<!-- END_RECENT_WRITING -->"

    # 3. 构建正则表达式
    pattern = re.compile(
        r"({})[\s\S]*?({})".format(re.escape(start_marker), re.escape(end_marker))
    )

    # 4. 检查是否能在文档中找到这两个标记
    if not pattern.search(readme_content):
        print("FATAL: Markers not found in README.md.")
        print(f"Please ensure '{start_marker}' and '{end_marker}' are present.")
        exit(1)

    # 5. 获取数据
    entries = fetch_rss_data()
    if not entries:
        print("INFO: No entries fetched. Exiting without update.")
        exit(0)

    # 6. 生成新内容
    new_list_content = generate_content(entries)

    # 构造替换后的中间块：前后加换行符保证美观
    # 最终结构: 标记 -> 换行 -> 内容 -> 换行 -> 标记
    replacement_content = f"\n{new_list_content}\n"

    # 7. 执行替换
    # \1 保留开始标记, \2 替换为新内容, \3 保留结束标记
    # 注意：这里的正则只有两个捕获组 (Start) 和 (End)，中间的内容不需要捕获组，直接用 formatted string 替换即可
    # 修正逻辑：使用 sub 直接重组

    def replacer(match):
        # match.group(1) 是开始标记
        # match.group(2) 是结束标记
        # 我们把新内容插在中间
        return f"{match.group(1)}{replacement_content}{match.group(2)}"

    new_readme = pattern.sub(replacer, readme_content)

    # 8. 写入文件（仅当有变化时）
    if new_readme != readme_content:
        readme_path.write_text(new_readme, encoding="utf-8")
        print("SUCCESS: README.md updated.")
    else:
        print("INFO: No changes detected.")
