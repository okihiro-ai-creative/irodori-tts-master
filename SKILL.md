---
name: irodori-tts-master
description: Irodori-TTS v3 / VoiceDesignで日本語TTS用のキャラクター固定、caption、seed、絵文字制御、推論コマンドを設計する順次ロード型スキル。
version: 1.0
created: 2026-06-18
---

# irodori-tts-master

> [!CAUTION]
> Irodori-TTSの声固定は「caption + seed + 主要パラメータ + 参照条件」の固定で再現性を高める設計であり、seedだけをキャラクターIDとして扱ってはならない。
> このスキルは順次ロード型。下の工程表を上から1ファイルずつ開いて実行する。
> 全工程を先読みするな。今の工程ファイルだけを開き、終わったら次を開く。

---

## 工程表（上から順に1ファイルずつ開いて実行する）

| STEP | 開くファイル | 完了条件（満たすまで次へ進まない） |
|------|-------------|----------------------------------|
| 1 | steps/step1_intake.md | 入力、用途、固定方式、出力先、停止条件が確定済み |
| 2 | steps/step2_text_normalization.md | TTS向け整形テキストと読み注意が保存済み |
| 3 | steps/step3_character_preset.md | character preset と caption が保存済み |
| 4 | steps/step4_command_plan.md | 実行コマンド、パラメータ、生成メモが保存済み |
| 5 | steps/step5_quality_loop.md | 検収結果と再生成方針が判定済み |

> [!IMPORTANT]
> 各 stepN.md は「冒頭=前工程の成果物を読む」「末尾=完了ゲート＋次に開くファイル名」を持つ。
> 完了ゲートが全✅でなければ次のファイルを開いてはならない。

---

## I/O Contract（入出力契約）

| 項目 | 内容 |
|---|---|
| 入力 | 日本語台本、用途、希望声質、キャラクター方向、参照音声の有無、実行環境 |
| 出力 | TTS整形テキスト、キャラクタープリセット、VoiceDesign caption、絵文字制御案、推論コマンド、検収ログ |
| 前提条件 | Irodori-TTS repoまたは実行環境、uv、対象checkpoint、出力wav保存先 |
| 上流スキル | なし。任意の台本・テキスト入力に対応 |
| 下流スキル | なし。生成wavは任意の動画編集・音声編集ワークフローで利用 |

---

## グローバル禁止事項

- ✗ seedだけでキャラクターを固定できると断定することを禁止する。なぜならseedは初期ノイズ固定であり、captionやcheckpointやsampling条件が変わると声も変わるからだ。
- ✗ 実在人物、声優、著名人、第三者の声を同意なしに模倣・クローンする指示を禁止する。なぜならIrodori-TTS model cardの倫理制限に反し、権利侵害や誤認を招くからだ。
- ✗ 難読漢字や固有名詞を未確認のまま最終音声用テキストに残すことを禁止する。なぜならIrodori-TTSは漢字読み精度に制約があるからだ。
- ✗ captionと参照音声の属性を矛盾させることを禁止する。なぜならVoiceDesign model cardが不安定化・ノイズ・条件上書きのリスクを示しているからだ。
- ✗ 工程表を飛ばして先の stepN.md を開くことを禁止する。前工程の完了ゲートが全✅になるまで進まない。
- ✗ ユーザー承認が必要な停止点を越えて次STEPへ進むことを禁止する。
- ✗ 効率化・先回りを理由にした先行生成を禁止する。
- ✗ ターミナル（mv / ren / sed / echo >）によるファイル変更を禁止する。
- ✗ ファイル操作（リネーム・コピー・移動・削除）はエディタ系ツール経由のみ。手段を各stepに明記する。

---

## 完了条件

全項目を✅/❌で宣言してから完了報告すること。

- [ ] `outputs/intake.md` が生成・保存済みである
- [ ] `outputs/normalized_text.md` が生成・保存済みである
- [ ] `outputs/character_preset.yaml` が生成・保存済みである
- [ ] `outputs/inference_plan.md` が生成・保存済みである
- [ ] `outputs/quality_report.md` が生成・保存済みである
- [ ] キャラクター固定値に checkpoint / seed / caption /主要sampling値が含まれている
- [ ] すべての stepN.md の完了ゲートが✅で通過した
- [ ] `resources/KNOWN_MISTAKES.md` が存在する

---

*Updated: 2026-06-18 / v1.0 初版 / OKIHIRO FORGE*
