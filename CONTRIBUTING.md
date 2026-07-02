# Contributing translations

Thanks for helping make Frostbite speak your language properly. The non-English catalogs here are
LLM-generated, so native-speaker fixes — even single-word ones — are genuinely useful.

## Fixing an existing translation

1. Edit the value in the language's `<code>.json`. **Never change a key** — keys are the bot's
   lookup ids and must match `en.json` exactly.
2. Run `python validate.py` (needs any Python 3; no dependencies).
3. Open a pull request. Mention what was wrong if it isn't obvious (grammar, register, a term
   Discord's own UI translates differently, …).

## Adding a new language

1. Copy `en.json` to `<code>.json`, where `<code>` is the lowercase two-letter code (`it`, `pl`,
   `tr`, …). The filename is the language code the bot registers.
2. Set `language.name` to the language naming itself (`"Italiano"`), then translate the values.
3. A partial catalog is fine — untranslated keys fall back to English. Prioritize the user-facing
   blocks: `dm.compromised`, `setup.*`, `honeypot.warning`, `language.*`, `report.*`.
4. Validate and open a PR. Once merged, the language appears on the bot's next restart.

## Translation rules

- **`{placeholders}`** (`{guild}`, `{count}`, `{epoch}`, …) are replaced by the bot at runtime.
  Keep their spelling exactly as-is, but move them freely to fit your language's word order. Every
  placeholder in the English value must appear in yours — `validate.py` enforces this.
- **Markdown and Discord syntax must survive**: `**bold**`, `` `code` ``, ``` fences, the `-#`
  small-text prefix, `#`/`##` headings, `•` bullets, `[label](url)` links, `<t:{epoch}:f>`
  timestamps, emoji.
- **Don't translate**: URLs; backticked commands and options (`/filter status`, `enabled:true` —
  Discord registers these in English); the name "Frostbite"; placeholder-only code spans like
  `{hash}…`.
- **Register**: informal second person, matching Discord's own UI in your language (tú/tu/você/je/
  du). The bot speaks in first person ("I removed…").
- **Discord terms**: prefer the wording Discord's official client uses in your language,
  especially for permission names (e.g. German "Nachrichten verwalten" for Manage Messages).
- English can hedge plurals ("image(s)"); if your language can't, pick the natural construction
  ("{count} vez/veces") rather than forcing the parenthesis.

## What's deliberately not translatable

Support-server review reports, owner-only command output, and log lines stay English — they're
for the bot team, not end users. Slash-command names/descriptions are also English-only for now.
