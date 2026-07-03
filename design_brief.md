# irodori-tts-master 設計書

## 目的・役割

Irodori-TTS v3 / VoiceDesign を使い、台本から日本語TTS生成用のキャラクター設定、VoiceDesign caption、seed固定、絵文字スタイル制御、推論コマンド、検収メモを作る。参照音声なしの疑似キャラ固定から、参照音声・Speaker Inversion を使う強い固定まで拡張できる構成にする。

## I/O Contract（入出力契約）

- 入力: 日本語台本、用途、希望する声質・キャラクター方向、参照音声の有無、生成環境の有無
- 出力: キャラクタープリセット、TTS向け整形テキスト、VoiceDesign caption、絵文字制御案、Irodori-TTS CLIコマンド、検収・再生成ログ
- 前提条件: Irodori-TTS のリポジトリまたは実行環境、uv、対象モデル、必要に応じてGPUまたはCPU実行時間

## ファイル構成案（順次ロード型・原則18）

```text
irodori-tts-master/
├── SKILL.md
├── design_brief.md
├── steps/
│   ├── step1_intake.md
│   ├── step2_text_normalization.md
│   ├── step3_character_preset.md
│   ├── step4_command_plan.md
│   └── step5_quality_loop.md
├── resources/
│   ├── CHARACTER_PRESET_TEMPLATE.md
│   ├── CAPTION_GUIDE.md
│   ├── EMOJI_STYLE_CONTROL.md
│   ├── PARAMETER_GUIDE.md
│   ├── SAFETY_AND_LICENSE.md
│   └── KNOWN_MISTAKES.md
└── outputs/
```

## 上流スキル / 下流スキル

- 上流: tts-generator、video-production-mode-f、short-production-master、YouTube_Script_Director_v1
- 下流: video-production-mode-f、video-render-master、short-production-master、audio-slide-rescue-master

## 適用する原則（重点）

- 原則1: 各工程で必要ファイルを再読し、Irodori-TTSのパラメータを記憶で扱わない
- 原則8: キャラクター固定値はプリセットファイルで受け渡す
- 原則11: 入力・出力・前提条件を毎回確定してから生成へ進む
- 原則13: 検収条件を具体化し、再生成時の変更点を記録する
- 原則18: SKILL.mdは工程表、詳細はstepsへ分離する

## 配布時の注意

- 絶対パス: なし
- クライアント固有情報: なし
- APIキー: なし
