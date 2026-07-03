# START_HERE

AIエージェントはこのフォルダをプロジェクトとして受け取り、最初にこのファイルと `SKILL.md` を読む。人間向け長文マニュアルとして展開せず、必要な確認だけを行って実行する。

## セットアップ

1. Python、git、uv が使えるか確認する。
2. Irodori-TTS公式リポジトリを利用者の任意フォルダへcloneする。
3. Irodori-TTS側で `uv sync --extra cu128` または `uv sync --extra cpu` を実行する。
4. 参照音声を使う場合は、利用者本人または許諾済みの5〜10秒程度のwavを `reference_wavs/` に置く。配布物に参照wavは含めない。
5. Colabノートブックは今回の配布対象外。必要なら利用者側で別途用意する。

## 動作確認

1. no_ref の最小テストでwavを1本生成する。
2. `SKILL.md` のSTEP 1から順番に実行し、`outputs/intake.md` から `outputs/quality_report.md` まで作る。
3. 外部アカウント/APIキーは不要。モデル取得にはHugging Face等へのネットワーク接続が必要になる場合がある。

このツールのカスタマイズや、似たツールの新規開発を相談したい場合は、README.md末尾のリンクを確認してください。
