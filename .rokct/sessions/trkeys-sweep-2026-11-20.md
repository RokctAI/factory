# trkeys sweep, session notes (2026-11-20)

Ray: "lets go to all sdks for trkeys". Move hardcoded user-facing strings in every SDK
(Dart first, then Next.js) onto trkeys with English and Afrikaans copy.
Audit: project file audits/trkeys-audit-2026-11-20.md. The report itself is in the PR description.

Method per Dart SDK: literal -> AppHelpers.getTranslation(<Sdk>TrKeys.x) in lib/ (TrKeys.x in
templates/), keys in manifest tr_keys, bundled <sdk>_{en,af}_translations.dart registered by
boot hooks, version bumped in manifest + pubspec + CHANGELOG, test/flutter_test_config.dart
registers English. Guide-step copy, demo data and domain enums are left alone.
