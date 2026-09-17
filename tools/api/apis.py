# -*- coding: utf-8 -*-
"""
DDABONG external API helpers. Reads keys from .env (repo root). Never prints key values.
  python tools/api/apis.py selftest              # naver + proxy + elevenlabs voices (no TTS spend)
  python tools/api/apis.py encyc "천마총" [n]      # Naver encyclopedia search (terms.naver.com entries)
  python tools/api/apis.py news "경주 천마총" [n]
  python tools/api/apis.py tts "text" out.mp3 [voice_name] [model]   # ElevenLabs TTS (costs characters)
  python tools/api/apis.py emuseum "천마총" [n]    # data.go.kr / e-museum relic list (needs registered key)
  python tools/api/apis.py khs 11 37 [n]          # 국가유산청 (no key) kind code, sido code
"""
import os, sys, json, io, urllib.parse
import requests

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def env():
    d = {}
    p = os.path.join(ROOT, ".env")
    if os.path.exists(p):
        for line in io.open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1); d[k.strip()] = v.strip()
    return d
E = env()

def mask(s):
    for v in E.values():
        if v and len(v) > 6: s = s.replace(v, "<KEY>")
    return s

# ---------- Naver Search (Client ID/Secret) ----------
def naver(kind, query, n=5, start=1, sort=None):
    """kind: encyc | news | blog | webkr | image | book | doc"""
    h = {"X-Naver-Client-Id": E["NAVER_CLIENT_ID"], "X-Naver-Client-Secret": E["NAVER_CLIENT_SECRET"]}
    p = {"query": query, "display": n, "start": start}
    if sort: p["sort"] = sort
    r = requests.get(f"https://openapi.naver.com/v1/search/{kind}.json", headers=h, params=p, timeout=20)
    r.raise_for_status(); return r.json()

# ---------- ElevenLabs ----------
def el_voices():
    r = requests.get("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key": E["ELEVENLABS_API_KEY"]}, timeout=20)
    r.raise_for_status(); return r.json()["voices"]

def el_tts(text, out_path, voice_name="George", model_id="eleven_multilingual_v2", stability=0.5, similarity=0.75, style=0.0):
    """Returns (bytes, chars). Cost = len(text) characters against the ElevenLabs plan. Record in COST file."""
    vid = [v["voice_id"] for v in el_voices() if v["name"].split(" - ")[0] == voice_name]
    if not vid: raise SystemExit(f"voice not found: {voice_name}")
    r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{vid[0]}?output_format=mp3_44100_128",
                      headers={"xi-api-key": E["ELEVENLABS_API_KEY"], "Content-Type": "application/json"},
                      json={"text": text, "model_id": model_id, "voice_settings": {"stability": stability, "similarity_boost": similarity, "style": style}}, timeout=120)
    r.raise_for_status(); open(out_path, "wb").write(r.content); return len(r.content), len(text)

# ---------- Webshare proxy ----------
def proxy_session(default=False):
    u = E["WEBSHARE_USERNAME_DEFAULT" if default else "WEBSHARE_USERNAME"]; p = E["WEBSHARE_PASSWORD_DEFAULT" if default else "WEBSHARE_PASSWORD"]
    s = requests.Session(); s.proxies = {"http": f"http://{u}:{p}@p.webshare.io:80", "https": f"http://{u}:{p}@p.webshare.io:80"}; return s

# ---------- data.go.kr / e-museum ----------
def emuseum(keyword, n=10, key_name="KOREA_DATA_API_KEY"):
    r = requests.get("http://www.emuseum.go.kr/openapi/relic/list", params={"serviceKey": E[key_name], "keyword": keyword, "numOfRows": n, "pageNo": 1}, timeout=25)
    return r.text

# ---------- 국가유산청 (no key) ----------
def khs(kind_code="11", sido="37", n=20):
    r = requests.get("https://www.khs.go.kr/cha/SearchKindOpenapiList.do", params={"pageUnit": n, "ccbaCncl": "N", "ccbaKdcd": kind_code, "ccbaCtcd": sido}, timeout=25, allow_redirects=True)
    return r.text

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a or a[0] == "selftest":
        out = {}
        try: j = naver("encyc", "천마총", 1); out["naver_encyc"] = f"OK total={j['total']} first={j['items'][0]['link']}"
        except Exception as e: out["naver_encyc"] = f"FAIL {e}"
        try: out["elevenlabs"] = f"OK {len(el_voices())} voices"
        except Exception as e: out["elevenlabs"] = f"FAIL {e}"
        try: ip = proxy_session().get("https://ipinfo.io/json", timeout=25).json(); out["webshare"] = f"OK exit {ip.get('country')} {ip.get('city')}"
        except Exception as e: out["webshare"] = f"FAIL {e}"
        try: t = emuseum("천마총", 1); out["emuseum(KOREA_DATA_API_KEY)"] = "OK" if "<resultCode>00" in t else "PENDING " + t[t.find("<resultMsg>"):][:60]
        except Exception as e: out["emuseum"] = f"FAIL {e}"
        try: t = khs(); out["khs"] = "OK" if "<totalCnt>" in t else "FAIL"
        except Exception as e: out["khs"] = f"FAIL {e}"
        print(mask(json.dumps(out, ensure_ascii=False, indent=1)))
    elif a[0] in ("encyc", "news", "blog", "webkr", "image", "book"):
        j = naver(a[0], a[1], int(a[2]) if len(a) > 2 else 5)
        for it in j["items"]: print("-", it.get("title", "").replace("<b>", "").replace("</b>", ""), "|", it.get("link") or it.get("originallink"), "|", it.get("description", "")[:120].replace("<b>", "").replace("</b>", ""))
    elif a[0] == "tts":
        b, c = el_tts(a[1], a[2], a[3] if len(a) > 3 else "George", a[4] if len(a) > 4 else "eleven_multilingual_v2"); print(f"wrote {a[2]} {b} bytes, {c} chars billed")
    elif a[0] == "emuseum": print(mask(emuseum(a[1], int(a[2]) if len(a) > 2 else 10)[:1500]))
    elif a[0] == "khs": print(khs(a[1], a[2], int(a[3]) if len(a) > 3 else 20)[:1500])
