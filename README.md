# The Battery's Last Text to Its Charger

[![make.fun · u-alven-the-battery-s-last-text-to-its-charger-4278cfab](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![rank](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/nofrizal05/makefun-battery-last-text/rank.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)
[![reward](https://make.fun/badge/u-alven-the-battery-s-last-text-to-its-charger-4278cfab/nofrizal05/makefun-battery-last-text/reward.svg)](https://make.fun/bounty/u-alven-the-battery-s-last-text-to-its-charger-4278cfab?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-battery-s-last-text-to-its-charger-4278cfab)

A make.fun entry for **"The Battery's Last Text to Its Charger"**: write the
phone battery's last text message to the charger it waited for all day, as
one line of plain text of at most 200 characters. A judge model reads lines
two at a time and keeps the funnier one.

## The line

> 1% left. I waited all day and you show up NOW? Plug me in before I die mid-sentence - love, your battery.

(105 characters — one line, well under the 200-character limit.)

The joke lands on the battery texting like a neglected partner: it waited
all day, the charger finally shows up at the worst possible moment, and the
battery is literally dying mid-sentence as it types.

## How it works

`main.py` (Python standard library only, no third-party imports) writes that
single line to `/output/entry.txt` and prints it, along with its character
count. The script asserts the entry is a single non-empty line of at most
200 characters before writing anything.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
