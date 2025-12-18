import pathlib
import re
import time
import html

import feedparser


def clean_summary(text):
    """
    清洗摘要文本：去除 HTML 标签、转义字符和换行符
    """
    if not text:
        return ""
    # 1. 去除 HTML 标签
    text = re.sub(r'<[^>]+>', '', text)
    # 2. 将 HTML 实体转回普通字符 (如 &gt; -> >)
    text = html.unescape(text)
    # 3. 去除换行符，避免破坏 Markdown 列表结构
    text = text.replace('\n', ' ').replace('\r', '')
    # 4. 移除多余的空格
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def replace_writing(content, marker, chunk, inline=False):
    """
    根据标记替换 README 中的内容
    """
    # 使用 re.DOTALL 让 . 匹配换行符
    pattern = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    
    # 检查标记是否存在
    if not pattern.search(content):
        print(f"Warning: Marker '' not found in README. No changes made.")
        return content

    if not inline:
        chunk = "\n{}\n".format(chunk)
    
    replacement = "{}".format(marker, chunk, marker)
    return pattern.sub(replacement, content)


def fetch_writing():
    """
    获取 RSS 并解析为结构化数据
    """
    rss_url = "https://rss.csdn.net/P_LarT/rss/map"
    
    try:
        # feedparser 内部处理了很多网络异常，但最好还是包裹一下
        rss_info = feedparser.parse(rss_url)
    except Exception as e:
        print(f"Error fetching RSS: {e}")
        return []

    # 检查是否成功获取到了 entries
    if not rss_info.get("entries"):
        print("No entries found in RSS feed.")
        return []

    entries = rss_info["entries"]
    recent_entries = entries[:10]
    
    processed_entries = []

    for entry in recent_entries:
        # --- 修复核心 Bug: 稳健的日期处理 ---
        # 优先使用 feedparser 解析好的 struct_time
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            date_str = time.strftime("%Y-%m-%d", entry.published_parsed)
        else:
            # Fallback: 如果解析失败，尝试直接获取字符串，或者给一个默认值
            date_str = entry.get("published", "")[:10] 

        # --- 修复排版 Bug: 清洗 Summary ---
        summary_text = clean_summary(entry.get("summary", ""))

        processed_entries.append({
            "title": entry.get("title", "No Title").strip(),
            "url": entry.get("link", "#"),
            "published": date_str,
            "summary": summary_text,
        })

    return processed_entries


if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.resolve()
    readme_path = root / "README.md"
    
    # 检查 README 是否存在
    if not readme_path.exists():
        print("Error: README.md not found.")
        exit(1)

    readme = readme_path.open(encoding="utf-8", mode="r").read()

    entries = fetch_writing()
    
    if not entries:
        print("No blog entries fetched. Exiting.")
        exit(0)

    # 生成新的 Markdown 内容
    entries_md = "\n".join(
        [
            "* [{title}]({url}) - {published}: <small>*{summary}*</small>".format(
                **entry
            )
            for entry in entries
        ]
    )
    
    print("Fetched info sample:", entries[0]['title'])

    # 执行替换
    new_readme = replace_writing(readme, "writing", entries_md)

    # 仅当内容有变化时才写入文件
    if new_readme != readme:
        readme_path.open(encoding="utf-8", mode="w").write(new_readme)
        print("README.md updated successfully.")
    else:
        print("No changes detected. README.md is up to date.")
