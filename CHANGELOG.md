# Changelog

All notable changes to this ontology are documented in this file.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer adapted for ontologies (see CONTRIBUTING).

## [Unreleased]

### Added
- The context generator emits domain-electrochemistry's `formerLabel` values (retired prefLabel spellings, introduced there in 0.38.0) as extra JSON-LD terms for the same IRI, so data written against `InititalThermodynamicTemperature` and the five other corrected spellings keeps expanding (#81).
- `tests/test_context_terms.py`: the six retired electrochemistry spellings and their corrected forms resolve, the SI-accepted unit terms are present, and no `nsN` prefix is published (#81).

### Changed
- Electrochemistry import updated from 0.37.2 to 0.38.0 in the four importing modules and all four catalogs (#81). The closure gains the 198 SI-accepted unit terms (`AmpereHour`, `MilliAmpereHour`, `WattHour`, `MolePerLitre`, `MilliAmpereHourPerGram`, ...) that 0.38.0 imports, the six corrected spellings, `ElectrodeToSeparatorGapWidth` and `formerLabel`; `context/context.json` grows by 206 terms with nothing removed or changed. None of the 28 electrochemistry anchor quantities deprecated in 0.38.0 is referenced by this domain's own modules.
- The JSON-LD context publishes the canonical prefixes `emmo`, `battery`, `electrochemistry`, `chemsub` and `chameo`, never an auto-generated `nsN` prefix (#78).

### Fixed
- `battery-products` moved from `subdomains/` to `modules/`, where its ontology IRI and the import in `battery-dependencies.ttl` say it is, so online resolution of `.../modules/battery-products` no longer returns 404; the `modules/` and `reference/` catalogs had also mapped it to a `./subdomains/` path that did not exist relative to them (#79, #82).

### Removed
- `subdomains/battery-model-lithium-ion.ttl` and its `config.yml` entries. It declared 23 terms in a namespace that returns 404, each reusing the UUID of a domain-electrochemistry term, was imported by nothing and listed in no catalog, and appeared in neither the inferred ontology nor the docs. The concepts live in domain-electrochemistry, where the polarity-qualified ones are deprecated with defining axioms as of 0.38.0 (#80, #83).

## [0.20.2] - 2026-08-10

### Changed
- The eight chemistry battery classes (`LithiumIonIronPhosphateBattery` and siblings) are un-deprecated and kept as defined classes: a reasoner infers the chemistry from the asserted electrode composition, so they are query vocabulary, not denormalised data. `LithiumIonBattery` documents the policy: the set is closed and curated, stoichiometry variants live at the material level, and the subclasses are inferred rather than asserted (#74, #77).
- `hasMeasurementUnit` is vocab-valued in the generated context, so a bare `Volt` expands to the unit term (#75, #77).
- The context generator carries a canonical-label table resolving the 17 duplicate prefLabels in the import closure and fails loudly on new ones (#76, #77).
- Electrochemistry import updated to 0.37.1 and then 0.37.2 (imports + all catalogs), bringing in the electrode-side half of #74 (#77).

### Deprecated
- The hyphen-named `PrismaticBattery` original, replaced by an underscore-named class with `isReplacedBy` (#73, #77).

## [0.20.1] - 2026-08-04

### Added
- `battery-cell-geometry` imported by the dependencies module (was documented but outside the release closure).
- Subdomains (products, lithium-ion extensions) added to documentation coverage.
- CONTRIBUTING guide; `bump-version` replaced by the shared config-driven tool (adds `--check` and date handling) with tests.
- Scheduled (weekly + post-release) CI check that the public w3id.org IRIs resolve, shared with domain-electrochemistry and domain-chemical-substance.
- The docs workflow now also redeploys automatically after each successful release (`workflow_run`), so the `versions/` archive picks up the new inferred release asset without a manual dispatch.

### Changed
- The inferred ontology (`battery-inferred.ttl`) is no longer tracked in git — it is a generated build artifact. CI regenerates it and publishes it to gh-pages (`/inferred`, latest) and attaches a freshly reasoned copy to each GitHub Release (per version); the docs workflow backfills the per-version `versions/` archive from Release assets. You no longer generate or commit it by hand.
- Updated the electrochemistry import to 0.36.0 and, matching its closure, the chemical-substance import to 0.15.0 and the CHAMEO import to 1.0.2 (imports + all catalogs). The full dependency stack now imports EMMO 1.0.2 consistently.

### Deprecated
- The specific commercial product classes in battery-products: `INR18650MJ1` (LG), `INR1865025R` and `INR1865035E` (Samsung), `INR18650P28A` and `INR18650P28B` (Molicel), `NaCR32140MP10` (HiNa), `G20M7` (Google). Manufacturer-specific products are out of scope for the reference ontology and will be removed in a future release; product-level terms belong in application resources or a dedicated registry. The IEC-designation classes (`INR18650`, `INR21700`, `INR46800`, `IFp18650`, `IFp21700`, `IFp46800`, `ICP66575`) are unaffected.

### Fixed
- Diamond dependency: catalogs pinned chemical-substance 0.13.2 while the electrochemistry import chain required 0.14.x — all catalogs now pin 0.14.1; electrochemistry pinned to 0.35.1.
- CHAMEO catalog entries pinned to the 1.0.0 tag (was a moving branch URL).
- `chemsub:` prefix namespace corrected (chemicalsubstance# → chemical-substance#; unused prefix, no term IRIs affected).
- Stale `dcterms:issued`/`modified` dates refreshed; `dcterms:license` now an IRI.
- emmocheck: exempted the external `schema:Product` interoperability stub from the description check (EMMOntoPy's built-in schema.org skip is broken by a typo upstream). This was the first CI run over the full file set; the failure predated the dependency updates.
- subdomains catalog: the `battery-products` entry resolved to a doubled path (`subdomains/subdomains/...`), which broke ontology loading for every file in that directory.

[Unreleased]: https://github.com/emmo-repo/domain-battery/compare/0.20.2...HEAD
[0.20.2]: https://github.com/emmo-repo/domain-battery/compare/0.20.1...0.20.2
[0.20.1]: https://github.com/emmo-repo/domain-battery/compare/0.20.0...0.20.1
