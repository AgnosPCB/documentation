"""
mkdocs-static-i18n builds every language into the same ``site/`` tree but
shares a single ``search/search_index.json`` across all of them (see
``mkdocs_static_i18n.reconfigure.ExtendedPlugin.reconfigure_search_index``,
which merges every language's entries into one Lunr index and lets
Material's own ``on_post_build`` write it once). Material's search worker
always fetches that one file relative to the site root, so a visitor
searching on, say, the Spanish pages gets English/French/German/Italian
results mixed in.

This hook runs after that combined index is written and splits it back out
into one file per language:

    site/search/search_index.json      -> English (default, no prefix)
    site/<lang>/search/search_index.json -> only that language's docs

Pairing with ``overrides/main.html``, which redirects the browser's request
for the index to the per-language file that matches the current page.
"""

import json
import logging
from pathlib import Path

from mkdocs.plugins import event_priority

log = logging.getLogger("mkdocs.hooks.split_search_index")

# Must match the "languages" list in mkdocs.yml (minus the default one).
TRANSLATED_LANGUAGES = ["es", "fr", "de", "it"]


def _doc_language(location: str) -> str:
    for lang in TRANSLATED_LANGUAGES:
        if location == lang or location.startswith(f"{lang}/"):
            return lang
    return "en"


# mkdocs_static_i18n writes the combined index from its own on_post_build,
# registered with event_priority(-100) so it runs after every other
# plugin's on_post_build. Ours must run after that, so it gets a lower
# priority still.
@event_priority(-200)
def on_post_build(config, **kwargs):
    site_dir = Path(config["site_dir"])
    combined_index = site_dir / "search" / "search_index.json"
    if not combined_index.exists():
        log.warning("split_search_index: no search_index.json found, skipping")
        return

    data = json.loads(combined_index.read_text(encoding="utf-8"))
    base_config = data.get("config", {})
    docs = data.get("docs", [])

    buckets: dict[str, list] = {"en": []}
    for lang in TRANSLATED_LANGUAGES:
        buckets[lang] = []
    for doc in docs:
        buckets[_doc_language(doc.get("location", ""))].append(doc)

    for lang, entries in buckets.items():
        target = (
            combined_index
            if lang == "en"
            else site_dir / lang / "search" / "search_index.json"
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "config": {**base_config, "lang": [lang]},
            "docs": entries,
        }
        target.write_text(
            json.dumps(payload, ensure_ascii=False), encoding="utf-8"
        )
        log.info(
            "split_search_index: wrote %d docs to %s", len(entries), target
        )
