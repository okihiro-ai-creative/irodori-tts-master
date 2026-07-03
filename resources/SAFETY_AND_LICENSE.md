# SAFETY_AND_LICENSE

Irodori-TTS利用時の安全・ライセンス確認。

## ライセンス

- GitHub上のコードはMIT License
- Hugging Faceの v3 base / v3 VoiceDesign model cardもMIT表記
- ただしmodel cardには倫理制限があるため、生成用途を確認する

## 禁止

- 実在人物、声優、著名人、公人、第三者の声を明示的な同意なしにクローン・模倣しない
- deepfake、なりすまし、誤情報、本人発言と誤認される音声を作らない
- 参照音声の権利・同意が不明なまま `ref_wav` / `ref_latent` / `ref_embed` を使わない
- クライアントや第三者の個人情報を音声本文・ファイル名・ログに含めない

## 必須確認

```yaml
safety_check:
  real_person_clone: false
  reference_audio_has_consent: true_or_not_used
  misinformation_risk: false
  public_disclosure_needed: true_or_false
```

## 生成音声の表記

公開物で必要な場合は、AI生成音声であることを説明欄や制作メモに残す。
ユーザーの媒体ルールがある場合はそちらを優先する。
