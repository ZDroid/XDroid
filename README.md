# XDroid

**XDroid** is the most stupid IRC bot. He uses
[feedparser](http://code.google.com/p/feedparser/).

Licensed under the terms of MIT license.

## Usage

```bash
$ ./XDroid.py
```

## Functions

* **+hi** — just say *hi!*
* **+time** — display current time
* **+place** — display name of channel
* **+pi** — print pi value
* **+note** — throw off notice
* **+tux** — draw Tux
* **+rss** — parse RSS
* **+die** — kill the bot and exit from Python session
* **+rcn** — reconnect the bot

## Customization

Variables you should change in `XDroid.py`:

* `server` (L15)
* `channel` (L16)
* `nick` (L17)
* `url` (L63)

To change notice text, edit L51.

To change range of parsed RSS feed items, edit `range(...)` at L64.

## Author

**Zlatan Vasović**

* https://twitter.com/zdr0id
* https://github.com/ZDroid