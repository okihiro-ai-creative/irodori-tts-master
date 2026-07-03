# STEP 3: キャラクタープリセットとcaption設計

### ⬅️ 着手前に読む（前工程の成果物）

📖 必読: `outputs/intake.md`（用途と固定方式を引き継ぐため）
📖 必読: `outputs/normalized_text.md`（本文の感情・用途に合わせるため）
📖 必読: `resources/CHARACTER_PRESET_TEMPLATE.md`（固定値テンプレートを使うため）
📖 必読: `resources/CAPTION_GUIDE.md`（VoiceDesign captionの境界条件を確認するため）
📖 必読: `resources/PARAMETER_GUIDE.md`（seedと主要パラメータをセットで固定するため）

---

## この工程でやること

`outputs/character_preset.yaml` を作成する。キャラクター固定は、caption、seed、checkpoint、sampling値、参照条件をセットで保存する。

### 設計手順

1. 用途に合う声の役割を1つ決める
2. captionを2〜4文で作る
3. seedを整数で固定する
4. no_ref / ref_wav / ref_latent / ref_embed を選ぶ
5. 初期sampling値を保存する
6. 避けたい声質を negative_caption に保存する

### ファイル操作の可否（原則8）

| 操作 | 可否 |
|---|---|
| `outputs/character_preset.yaml` を作成 | ✅ |
| 既存presetを上書き | ✗ 禁止（理由: キャラクター再現履歴が消えるため。必要なら別名で作る） |
| 参照音声を加工 | ✗ 禁止（理由: この工程は設計工程であり音声処理工程ではないため） |

### 正例・反例（原則3）

✅ 正例:
```yaml
name: "calm-guide-female"
voice_design:
  caption: "若い女性の声。落ち着いていて、近い距離感で、やわらかく自然に話す。少し明るく、聞き手に寄り添う口調。"
sampling:
  seed: 123456
  num_steps: 40
```

✗ 反例:
```yaml
name: "character-a"
voice_design:
  caption: "いい感じ"
sampling:
  seed: 123456
```

captionが曖昧で再現性の核にならない。

### この工程固有の禁止事項（原則2）

- ✗ seedだけを保存してキャラクタープリセット完了とすることを禁止する。なぜなら同じseedでもcaptionやcheckpointが変われば声が変わるからだ。
- ✗ 「有名人に似せる」captionを作ることを禁止する。なぜなら倫理制限に反するからだ。

---

### 🛑 完了ゲート（全項目✅でなければ次に進めない / 原則4・13・14）

- [ ] `outputs/character_preset.yaml` が保存済み
- [ ] `checkpoint` が1件記録済み
- [ ] `seed` が整数で1件記録済み
- [ ] `caption` が2〜4文で記録済み
- [ ] `reference.mode` が no_ref / ref_wav / ref_latent / ref_embed のいずれか
- [ ] `sampling` に num_steps / cfg_scale_text / cfg_scale_caption / duration_scale がある

判定:
- すべて✅なら → 次に開く: `steps/step4_command_plan.md`
- ❌が1つでもあれば → この工程の該当箇所に戻って修正し、再判定する
