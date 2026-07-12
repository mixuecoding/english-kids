"""生成英语单词MP3 — edge-tts"""
import asyncio, os, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
from edge_tts import Communicate

async def gen(word):
    mp3 = f"audio/{word}.mp3"
    if os.path.exists(mp3):
        print(f"  skip {word}")
        return
    try:
        comm = Communicate(word, "en-US-JennyNeural")
        await comm.save(mp3)
        print(f"  OK {word} ({os.path.getsize(mp3)} bytes)")
    except Exception as e:
        print(f"  ERR {word}: {e}")

async def main():
    words = []
    with open("audio/list.txt", "r", encoding="utf-8") as f:
        words = [l.strip() for l in f if l.strip()]
    print(f"Generating {len(words)} MP3s...")
    for w in words:
        await gen(w)
    print("Done!")

if __name__ == "__main__":
    asyncio.run(main())
