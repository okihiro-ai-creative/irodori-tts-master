# PARAMETER_GUIDE

Irodori-TTSでキャラクター再現性に関わる主要パラメータをまとめる。

## 固定すべき値

| 値 | 役割 | 固定理由 |
|---|---|---|
| checkpoint | 使用モデル | モデルが変わると声質と挙動が変わる |
| text | 読ませる本文 | テキストが変わると長さ・抑揚・声質が変わる |
| caption | VoiceDesign指示 | キャラクターの中核 |
| seed | 初期ノイズ | 同条件での再現性を上げる |
| num_steps | サンプリング品質 | 結果の安定性に影響する |
| cfg_scale_text | テキスト追従 | 読みの強さに影響する |
| cfg_scale_caption | caption追従 | 声質・演技への追従に影響する |
| cfg_scale_speaker | 参照音声追従 | ref_wav/ref_embed使用時の声質維持に影響する |
| duration_scale / seconds | 長さ | 話速・余白・破綻に影響する |
| t_schedule_mode / sway_coeff | サンプリング経路 | 声質・安定性に影響する |
| truncation_factor | ばらつき抑制 | 変化量と表現力に影響する |

## 推奨初期値

```yaml
num_steps: 40
cfg_scale_text: 3.0
cfg_scale_caption: 4.0
cfg_scale_speaker: 5.0
cfg_guidance_mode: "independent"
duration_scale: 1.0
t_schedule_mode: "linear"
sway_coeff: -1.0
truncation_factor: null
```

## seedの扱い

seedはキャラクターIDではなく、初期ノイズ固定値。
同じ checkpoint、text、caption、参照条件、sampling値で再生成したときの再現性を上げる。

## ref modeの使い分け

| mode | 用途 |
|---|---|
| no_ref | 参照音声なし。caption + seedで疑似キャラ固定 |
| ref_wav | 短い参照音声から声質を寄せる |
| ref_latent | 同じ参照音声を何度も使う高速化 |
| ref_embed | Speaker Inversionで学習した話者トークンを使う |

## 調整順

1. 読みが違う: 本文をひらがな・カタカナへ直す
2. 声質が違う: captionを短く具体化する
3. キャラがぶれる: seedを固定し、num_stepsとcfgを戻す
4. 参照音声から離れる: cfg_scale_speakerまたはspeaker_kv_scaleを少し上げる
5. 不自然な音が出る: 絵文字を減らし、truncation_factorを未指定へ戻す
