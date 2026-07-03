# Irodori-TTS 動作確認テンプレート

この配布物には検証済みwav、参照wav、ローカルGPU固有の検証ログ、Colabノートブックを含めない。利用者の環境で以下を確認する。

## 確認項目

- Irodori-TTS公式リポジトリを任意の作業フォルダへcloneした
- `uv sync --extra cu128` または `uv sync --extra cpu` が成功した
- no_ref の最小テストwavが生成できた
- ref_wav を使う場合、利用許可済みの5〜10秒程度のwavを `reference_wavs/` に置いた
- 生成音声を公開・配布する前に `resources/SAFETY_AND_LICENSE.md` を確認した
