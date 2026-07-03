# SETUP

Generic Skill Package

この手順は、Irodori-TTS公式リポジトリをクローンして、`irodori-tts-master` スキルから生成したコマンドを実行できる状態にするためのものです。

## 前提

- Pythonが使えること
- `git` が使えること
- `uv` が使えること
- GPUを使う場合はCUDA環境があること

`uv` がない場合は、先に公式のuv導入手順に従ってインストールしてください。

## 1. Irodori-TTSをクローンする

任意の作業フォルダで実行します。

```bash
git clone https://github.com/Aratako/Irodori-TTS.git
cd Irodori-TTS
```

## 2. 依存関係を入れる

CUDA 12.8系GPUを使う場合:

```bash
uv sync --extra cu128
```

CPUで試す場合:

```bash
uv sync --extra cpu
```

## 3. 動作確認する

参照音声なしで最小テストを行います。初回はモデルがダウンロードされるため時間がかかります。

```bash
uv run --no-sync python infer.py \
  --hf-checkpoint Aratako/Irodori-TTS-500M-v3 \
  --text "こんにちは。これは音声合成のテストです。" \
  --no-ref \
  --output-wav outputs/test.wav
```

VoiceDesignモデルを使う場合:

```bash
uv run --no-sync python infer.py \
  --hf-checkpoint Aratako/Irodori-TTS-600M-v3-VoiceDesign \
  --text "こんにちは。これは音声合成のテストです。" \
  --caption "若い女性の声。落ち着いていて、近い距離感で、やわらかく自然に話す。" \
  --no-ref \
  --seed 123456 \
  --num-steps 40 \
  --cfg-scale-text 3.0 \
  --cfg-scale-caption 4.0 \
  --duration-scale 1.0 \
  --output-wav outputs/test_voice_design.wav
```

## 4. このスキルを使う

AIエージェントに `SKILL.md` を読ませ、工程表の順番で進めます。

```text
irodori-tts-master/SKILL.md を使って、台本からIrodori-TTS用のキャラクタープリセットと推論コマンドを作ってください。
```

成果物はスキル内の指定に従い、以下のように作ります。

```text
outputs/intake.md
outputs/normalized_text.md
outputs/character_preset.yaml
outputs/inference_plan.md
outputs/quality_report.md
```

## 5. キャラクターを固定したい場合

`resources/CHARACTER_PRESET_TEMPLATE.md` を使い、最低限この値を固定します。

```yaml
checkpoint: "Aratako/Irodori-TTS-600M-v3-VoiceDesign"
caption: "若い女性の声。落ち着いていて、近い距離感で、やわらかく自然に話す。"
seed: 123456
num_steps: 40
cfg_scale_text: 3.0
cfg_scale_caption: 4.0
duration_scale: 1.0
reference:
  mode: "no_ref"
```

seedだけを変えずに保存しても、captionやcheckpointが変わると同じキャラクターにはなりません。

## 6. 参照音声を使う場合

参照音声を使う前に、音声提供者の同意と利用範囲を確認してください。配布物には参照音声を同梱していません。あなた自身の声、または利用許可を得た5〜10秒程度のwavを `reference_wavs/` に置いてください。

`ref_wav` を使う場合は、`--no-ref` を外し、推論コマンドに参照音声を指定します。

```bash
uv run --no-sync python infer.py \
  --hf-checkpoint Aratako/Irodori-TTS-600M-v3-VoiceDesign \
  --text "こんにちは。これはテストです。" \
  --caption "参照音声の自然な声質を保ったまま、穏やかで丁寧に話す。" \
  --ref-wav path/to/reference.wav \
  --seed 123456 \
  --output-wav outputs/test_ref.wav
```

## トラブル時

- 読み間違いがある: 本文をひらがな・カタカナへ直す
- 声質がぶれる: captionを短くし、seedと主要パラメータを固定する
- 音が破綻する: 絵文字を減らす、captionの矛盾を消す
- 参照音声から離れる: `cfg_scale_speaker` を調整する
- 初回が遅い: モデルダウンロード中の可能性がある

## 7. 音を少しクリアにしたい場合

`ffmpeg` が入っていれば、同梱の軽量後処理ツールを使える。

```bash
python scripts/enhance_audio_ffmpeg.py \
  --input path/to/full_script.wav \
  --preset voice_clear_light
```

出力は既定で `*_enhanced.wav`。まずは `voice_clear_light` を使い、強すぎる場合だけ `voice_clear_soft` を試す。
