# The World Today · 23 November 2026

An illustrated entry for the make.fun bounty **Sum up 23 November's world news in one image** (`news-image-20261123`).

- COP31 ended without an overall deal in Antalya after the EU and about 130 parties rejected a draft that omitted fossil fuels. [The Japan Times](https://www.japantimes.co.jp/environment/2026/11/23/climate-change/climate-diplomacy-cop31-collapse/) · [One Turn](https://oneturn.news/day/2026-11-23/)
- Russian strikes killed at least 15 people in the Kyiv region. [South China Morning Post](https://www.scmp.com/news/world/europe/article/3375401/russian-strikes-kill-6-kyiv-region-ukraine-says)
- Ukraine said its sea drones sank a Russian warship and destroyed a Ka-27 helicopter at the Benghazi naval base in Libya. [Associated Press](https://apnews.com/article/c382f8eb06dca7d87e89bc6c18ba7d61)
- US Democrats secured at least 258 House seats, their biggest majority since 1992. [Associated Press](https://apnews.com/article/721096a4d9ba2cd68683692361798cdb)
- The AI sell-off knocked the Nikkei down 5.06% and the S&P 500 down 3.7% on Friday. Gold subsequently rose 2.72%. [One Turn](https://oneturn.news/day/2026-11-23/)
- The joint European–Japanese BepiColombo mission entered orbit around Mercury. [Associated Press](https://apnews.com/article/0c80bbf2039ed4f6ee4a34426b3594a0)

Run `python3 main.py` to write `/output/entry.png`. Set `ENTRY_OUTPUT` to use a different path.

## Pre-submit review

- Decoded the final PNG and confirmed it is 1024 × 1024 and 659,840 bytes, below the 1 MiB limit.
- Reduced the PNG from 938,565 bytes by quantizing colors only within the illustrations. A pixel comparison confirmed that the text bands and borders retained their exact pixels. The image was visually checked at full size and thumbnail size.
- Ran `main.py` twice with fresh `ENTRY_OUTPUT` paths, once from the repository and once by absolute path from `/tmp`. Both outputs matched `entry.png` byte for byte and had mode `0644`.
