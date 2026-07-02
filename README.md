# Frostbite-Lang

Message catalogs (translations) for the [Frostbite Bot](https://tricrotism.com/frostbite)
Discord bot.

> ⚠️ **Machine-translated content.** Every catalog other than `en.json` was generated with an LLM
> and may contain inaccurate or unnatural translations. Corrections are very welcome — see
> [CONTRIBUTING.md](CONTRIBUTING.md).

## Languages

| Code | Language   | Source                  |
|------|------------|-------------------------|
| `en` | English    | Reference (hand-written)|
| `de` | Deutsch    | LLM-generated           |
| `es` | Español    | LLM-generated           |
| `fr` | Français   | LLM-generated           |
| `nl` | Nederlands | LLM-generated           |
| `pt` | Português  | LLM-generated           |

## How the bot uses this repo

- On startup, Frostbite lists this repo through the GitHub Contents API and downloads **every
  `<code>.json` file it finds** — the filename *is* the language code, so `it.json` landing here
  makes Italian exist, with no bot code changes. Merged changes go live on the bot's next restart.
- Each catalog names itself via its `language.name` key (e.g. `"Español"`); that's the name shown
  by `/language show`.
- Any key a catalog doesn't define falls back to English, so partial translations are safe.
- English is always the default: a copy of `en.json` is bundled inside the bot, and users/servers
  only get another language by opting in with `/language set` (per-user) or `/language server`
  (per-server, Manage Server). `/lang` is an alias. Public posts also carry a 🌐 button that shows
  a private copy in the clicker's language.

## Validating

```sh
python validate.py
```

Checks every catalog against `en.json`: valid JSON, no unknown keys, `{placeholders}` preserved.
