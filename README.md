# XDroid

**XDroid** is a potentially good IRC bot. He uses
[feedparser](http://code.google.com/p/feedparser/).

Licensed under the terms of MIT license.

## Usage

```bash
$ ./XDroid.py
```

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to kill bot.

## Commands

Commands start with `+` to avoid conflicts with other IRC bots and services.

* **+hi** — say *Hi!*
* **+time** — display current time
* **+channel** — display name of channel
* **+pi** — display pi value
* **+note** — display notice
* **+tux** — draw Tux
* **+feed** — display Atom or RSS feed items
* **+quit** — kill bot and exit from Python session
* **+rcn** — reconnect bot

## Customization

Variables you should change in `XDroid.py`:

* `server` (L15)
* `channel` (L16)
* `nick` (L17)
* `url` (L63)

To change range of feed items for parse, edit `n` in `range(1, n)` at L64.

Don't change L35 and L36 because of they are for ping replies.

## Author

**Zlatan Vasović**

* <https://twitter.com/zdr0id>
* <https://github.com/ZDroid>