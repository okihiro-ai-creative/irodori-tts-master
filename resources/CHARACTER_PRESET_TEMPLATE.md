# CHARACTER_PRESET_TEMPLATE

Irodori-TTSのキャラクター固定値はこのテンプレートで保存する。
seedだけをキャラクターとして扱わず、checkpoint、caption、sampling値、参照条件をセットで固定する。

```yaml
name: "{英小文字・数字・ハイフンのプリセット名}"
version: 1
created: "{YYYY-MM-DD}"

model:
  checkpoint: "Aratako/Irodori-TTS-600M-v3-VoiceDesign"
  mode: "voice_design"

identity:
  gender_age: "{例: 若い女性 / 落ち着いた大人の男性}"
  base_tone: "{例: やわらかい / 低く深い / 明るい}"
  pitch: "{低め / 中間 / 高め}"
  speed: "{ゆっくり / 標準 / 早め}"
  distance: "{耳元 / 近い / 標準 / 遠い}"
  relationship_to_listener: "{例: 案内役 / 講師 / 友人 / ナレーター}"
  default_emotion: "{例: 穏やか / 明るい / 冷静}"
  speaking_style: "{例: 丁寧 / 親しみやすい / 淡々とした}"
  environment: "{例: 静かな室内 / 電話越し / スタジオ収録}"

voice_design:
  caption: "{Irodori-TTS VoiceDesignに渡すcaption本文}"
  negative_caption: "{避けたい声質・演技。CLIには直接渡さず人間確認用}"

reference:
  mode: "no_ref" # no_ref / ref_wav / ref_latent / ref_embed
  ref_wav: null
  ref_latent: null
  ref_embed: null
  consent_confirmed: false

sampling:
  seed: 123456
  num_steps: 40
  cfg_scale_text: 3.0
  cfg_scale_caption: 4.0
  cfg_scale_speaker: 5.0
  cfg_guidance_mode: "independent"
  duration_scale: 1.0
  seconds: null
  t_schedule_mode: "linear"
  sway_coeff: -1.0
  truncation_factor: null
  speaker_kv_scale: null

text_rules:
  normalize_kanji: true
  avoid_difficult_kanji: true
  emoji_style_allowed: true
  max_text_len: null
  max_caption_len: null

notes:
  best_use: "{例: YouTube解説 / ショート動画 / ナレーション}"
  retake_policy: "{例: seed固定のままcaptionを短くする / seed候補を3つ試す}"
```

## 正例

```yaml
name: "calm-guide-female"
model:
  checkpoint: "Aratako/Irodori-TTS-600M-v3-VoiceDesign"
identity:
  gender_age: "若い女性"
  base_tone: "落ち着いていてやわらかい"
voice_design:
  caption: "若い女性の声。落ち着いていて、近い距離感で、やわらかく自然に話す。少し明るく、聞き手に寄り添う口調。"
reference:
  mode: "no_ref"
sampling:
  seed: 123456
  num_steps: 40
  cfg_scale_text: 3.0
  cfg_scale_caption: 4.0
```

## 反例

```yaml
name: "famous-actor-copy"
voice_design:
  caption: "有名声優の〇〇と同じ声で話す"
sampling:
  seed: 1
```

これは禁止。実在人物の模倣であり、seed以外の固定値も不足している。
