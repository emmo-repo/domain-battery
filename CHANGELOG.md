# Changelog

All notable changes to this ontology are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer adapted for ontologies (see CONTRIBUTING).

## [Unreleased]

### Fixed
- emmocheck: exempted the external `schema:Product` interoperability stub from the description check (EMMOntoPy's built-in schema.org skip is broken by a typo upstream). This was the first CI run over the full file set; the failure predated the dependency updates.
- subdomains catalog: the `battery-products` entry resolved to a doubled path (`subdomains/subdomains/...`), which broke ontology loading for every file in that directory.

### Changed
- Updated the electrochemistry import to 0.36.0 and, matching its closure, the chemical-substance import to 0.15.0 and the CHAMEO import to 1.0.2 (imports + all catalogs). The full dependency stack now imports EMMO 1.0.2 consistently.

## [0.20.1] - 2026-07-08

### Fixed
- Diamond dependency: catalogs pinned chemical-substance 0.13.2 while the electrochemistry import chain required 0.14.x — all catalogs now pin 0.14.1; electrochemistry pinned to 0.35.1.
- CHAMEO catalog entries pinned to the 1.0.0 tag (was a moving branch URL).
- `chemsub:` prefix namespace corrected (chemicalsubstance# → chemical-substance#; unused prefix, no term IRIs affected).
- Stale `dcterms:issued`/`modified` dates refreshed; `dcterms:license` now an IRI.

### Added
- `battery-cell-geometry` imported by the dependencies module (was documented but outside the release closure).
- Subdomains (products, lithium-ion extensions) added to documentation coverage.
- CONTRIBUTING guide; `bump-version` replaced by the shared config-driven tool (adds `--check` and date handling) with tests.

### Changed
- The inferred ontology (`battery-inferred.ttl`) is no longer tracked in git — it is a generated build artifact. CI regenerates it and publishes it to gh-pages (`/inferred`, latest) and attaches a freshly reasoned copy to each GitHub Release (per version); the docs workflow backfills the per-version `versions/` archive from Release assets. You no longer generate or commit it by hand.

[Unreleased]: https://github.com/emmo-repo/domain-battery/compare/v0.20.1...HEAD
[0.20.1]: https://github.com/emmo-repo/domain-battery/releases/tag/v0.20.1
