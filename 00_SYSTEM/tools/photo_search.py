"""photo_search.py - Pipeline A step A2: find licensed photo candidates (Wikimedia Commons).

Usage:
  python 00_SYSTEM/tools/photo_search.py "Daereungwon" "Cheonmachong" --min-width 1920 --limit 15
  python 00_SYSTEM/tools/photo_search.py --shot EP01_S02_SH001 "Daereungwon tumuli"   (tags the table with a shot id)
  ... --out 02_SEASONS/S01/EP01/15_QA/PHOTO_AI_CANDIDATES_20260914.md   (append markdown table + JSON sidecar)

Rules (PHOTO_AI_STANDARD v0.1, D-033):
  GREEN  = CC0 / Public domain / PDM / PD-* (not PD-US*) / KOGL Type 1 -> may be used as AI reference (Pipeline A)
  PD-US* = YELLOW (US-only public domain; manual check before use)
  YELLOW = CC BY, CC BY-SA (any version)                    -> composition numbers only, never as AI reference
  RED    = NC / ND / unknown / all rights reserved          -> never
This script only LISTS candidates. It never downloads originals, never writes rights.json.
No paid call. Network: Wikimedia Commons public API only.
"""
import argparse, json, re, sys, datetime, pathlib, urllib.parse
import requests

API = "https://commons.wikimedia.org/w/api.php"
UA = {"User-Agent": "ddabong-korea-hq/0.1 (photo_search; research only)"}

GREEN_PAT = re.compile(r"^(cc0|public domain|pdm\b|pd\b|pd-(?!us)|kogl type 1|공공누리 제?1유형)", re.I)  # PD-US* -> YELLOW (US-only PD, manual check)
YELLOW_PAT = re.compile(r"^cc[- ]by(-sa)?([-\s]|$)", re.I)


def tier(license_short: str) -> str:
    s = (license_short or "").strip()
    if not s:
        return "RED"
    if re.match(r"^pd-us", s, re.I):  # US-only public domain: manual check (YELLOW)
        return "YELLOW"
    if GREEN_PAT.search(s):
        return "GREEN"
    if re.search(r"\b(nc|nd)\b", s, re.I):
        return "RED"
    if YELLOW_PAT.search(s):
        return "YELLOW"
    return "RED"


def strip_html(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s or "").strip()


def search(query: str, limit: int, min_width: int):
    params = {
        "action": "query", "format": "json", "generator": "search",
        "gsrsearch": f"{query} filetype:bitmap", "gsrnamespace": 6, "gsrlimit": min(limit, 50),
        "prop": "imageinfo", "iiprop": "url|size|extmetadata|mime",
    }
    r = requests.get(API, params=params, headers=UA, timeout=40)
    r.raise_for_status()
    j = r.json()
    if "error" in j:
        raise RuntimeError(f"Commons API error: {j['error']}")
    pages = j.get("query", {}).get("pages", {})
    out = []
    for p in pages.values():
        ii = (p.get("imageinfo") or [{}])[0]
        em = ii.get("extmetadata", {})
        w, h = ii.get("width", 0), ii.get("height", 0)
        lic = strip_html(em.get("LicenseShortName", {}).get("value", ""))
        item = {
            "query": query,
            "title": p["title"],
            "page_url": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(p["title"].replace(" ", "_")),
            "width": w, "height": h,
            "min_1080p": w >= 1920 and h >= 1080,
            "min_4k": w >= 3840 and h >= 2160,
            "license": lic,
            "tier": tier(lic),
            "artist": strip_html(em.get("Artist", {}).get("value", ""))[:60],
            "date": strip_html(em.get("DateTimeOriginal", {}).get("value", ""))[:10],
            "size_source": "API (not downloaded)",
        }
        if w >= min_width:
            out.append(item)
    order = {"GREEN": 0, "YELLOW": 1, "RED": 2}
    out.sort(key=lambda x: (order[x["tier"]], -x["width"]))
    return out


def md_table(items, shot=None):
    head = f"### 후보 — {items[0]['query'] if items else ''}" + (f" · 샷 `{shot}`" if shot else "")
    lines = [head, "", "| 등급 | 파일 | 크기 (API) | 1080p | 4K | 라이선스 | 작가 | 촬영일 | AI 참고 가능 |", "|---|---|---|---|---|---|---|---|---|"]
    for it in items:
        ok = "예" if it["tier"] == "GREEN" else ("수치만" if it["tier"] == "YELLOW" else "아니오")
        lines.append(f"| **{it['tier']}** | [{it['title'].replace('File:', '')}]({it['page_url']}) | {it['width']}×{it['height']} | "
                     f"{'✔' if it['min_1080p'] else '✘'} | {'✔' if it['min_4k'] else '✘'} | {it['license']} | {it['artist']} | {it['date']} | {ok} |")
    g = sum(1 for i in items if i["tier"] == "GREEN")
    lines.append(f"\nGREEN {g} · YELLOW {sum(1 for i in items if i['tier']=='YELLOW')} · RED {sum(1 for i in items if i['tier']=='RED')} · 크기는 API 값(내려받지 않음), 실측은 권리 기록 단계에서.")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("queries", nargs="+")
    ap.add_argument("--shot", default=None)
    ap.add_argument("--limit", type=int, default=15)
    ap.add_argument("--min-width", type=int, default=1920)
    ap.add_argument("--out", default=None, help="markdown file to append to (JSON sidecar written next to it)")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    all_items, blocks = [], []
    for q in a.queries:
        try:
            items = search(q, a.limit, a.min_width)
        except Exception as e:
            print(f"### 후보 — {q}\n\n(검색 실패: {e})\n"); continue
        all_items += items
        blocks.append(md_table(items, a.shot) if items else f"### 후보 — {q}\n\n(폭 {a.min_width}px 이상 후보 없음)")
    body = "\n\n".join(blocks)
    print(body)
    if a.out:
        out = pathlib.Path(a.out)
        stamp = datetime.date.today().isoformat()
        header = "" if out.exists() else f"# Pipeline A · 사진 후보 (photo_search.py · {stamp})\n\n> 조사만. 원본 내려받기·권리 기록·생성 없음. GREEN 만 AI 참고 가능 (D-033). 크기는 Commons API 값.\n\n"
        with out.open("a", encoding="utf-8") as f:
            f.write(header + body + "\n\n")
        side = out.with_suffix(".json")
        prev = json.loads(side.read_text(encoding="utf-8")) if side.exists() else []
        side.write_text(json.dumps(prev + [dict(i, shot=a.shot, searched_at=stamp) for i in all_items], ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\n-> appended to {out} (+ {side.name})")


if __name__ == "__main__":
    main()
