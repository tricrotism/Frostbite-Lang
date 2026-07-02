# Frostbite-Lang

Message catalogs for the [Frostbite](https://github.com/tricrotism/Frostbite) Discord bot. The bot
**pulls every `<code>.json` file straight from this repo at startup** (via the GitHub Contents
API, `frostbite.lang.remote-contents-url`) — merged translations go live on the bot's next
restart, no deploy needed. A local checkout (`frostbite.lang.dir`) overrides per-key for
development. Users pick a language with `/language set` (or `/lang set`) and servers with
`/language server`. **English is always the default** — a copy of `en.json` is bundled inside the
bot, so this repo only needs to exist to add more languages.

> ⚠️ **Machine-translated content.** Every catalog other than `en.json` is generated with an LLM
> and may contain inaccurate or unnatural translations. Corrections are very welcome — open a pull
> request or an issue against this repo.

## File format

One flat JSON object per language, named by its lowercase code (`en.json`, `es.json`, `fr.json`,
`pt.json`, `nl.json`, `de.json`, …): `"key": "template"`.

- `en.json` is the reference catalog. To add a language, copy it, translate the **values**, and
  never change the keys.
- `{tokens}` (e.g. `{guild}`, `{count}`, `{channel}`) are replaced by the bot at runtime — keep
  them exactly as-is, but move them around freely to fit the language's word order.
- Discord markup must survive translation: markdown (`**bold**`, `` `code` ``, `-#` small text,
  `##` headings), timestamps (`<t:{epoch}:f>`), and any URLs stay as in the English value.
- `language.name` is the language naming itself in that language (`"Español"`, `"Deutsch"`) — it's
  what `/language show` lists.
- Missing keys are fine: anything a catalog doesn't define falls back to English. Partial
  translations are better than none.

## What is (deliberately) not translated

Support-server review reports, owner-only command output, and log lines stay English — they're for
the bot team, not end users. Slash-command names/descriptions are also English-only for now.
