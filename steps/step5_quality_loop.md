# STEP 5: 音声検収と再生成ループ

### ⬅️ 着手前に読む（前工程の成果物）

📖 必読: `outputs/inference_plan.md`（実行したコマンドと固定値を確認するため）
📖 必読: `outputs/character_preset.yaml`（変えてよい値と固定すべき値を確認するため）
📖 必読: `resources/PARAMETER_GUIDE.md`（問題別の調整順を確認するため）
📖 必読: `resources/SAFETY_AND_LICENSE.md`（公開・利用前の安全確認を行うため）

---

## この工程でやること

生成音声を検収し、`outputs/quality_report.md` にPASS/RETAKEを記録する。RETAKEの場合は、変更したパラメータと理由を記録する。

### 検収項目

| 項目 | 判定 |
|---|---|
| 読み間違い | PASS / RETAKE |
| 無音・途切れ | PASS / RETAKE |
| ノイズ・破綻 | PASS / RETAKE |
| キャラクター一致 | PASS / RETAKE |
| caption追従 | PASS / RETAKE |
| 参照音声追従 | PASS / RETAKE / N/A |
| 尺 | PASS / RETAKE |
| 禁止用途リスク | PASS / STOP |

### RETAKE調整順

1. 読み間違い: `outputs/normalized_text.md` を直す
2. 声質違い: captionを短く具体化する
3. キャラぶれ: seed・num_steps・cfgを固定値へ戻す
4. 参照音声から離れる: `cfg_scale_speaker` を少し上げる
5. ノイズ: 絵文字を減らす、captionの矛盾を消す
6. 尺: `duration_scale` を0.05刻みで調整する

### ファイル操作の可否（原則8）

| 操作 | 可否 |
|---|---|
| `outputs/quality_report.md` を作成 | ✅ |
| RETAKE版の別名wavを作成 | ✅ |
| PASS前のwavを削除 | ✗ 禁止（理由: 比較検収ができなくなるため） |
| character presetを無断上書き | ✗ 禁止（理由: キャラクター固定値が壊れるため） |

### 正例・反例（原則3）

✅ 正例:
```markdown
RETAKE 02:
- 問題: 声が明るすぎる
- 変更: captionから「少し明るく」を削除、seedは固定
- 固定維持: checkpoint, seed, num_steps, cfg_scale_text
```

✗ 反例:
```markdown
なんとなく全部変えて再生成した。
```

比較不能になるため禁止。

### この工程固有の禁止事項（原則2）

- ✗ RETAKE時にseed、caption、cfg、durationを同時に変更することを禁止する。なぜなら原因が特定できなくなるからだ。
- ✗ PASS前の音声を削除することを禁止する。なぜなら比較と復元ができなくなるからだ。

---

### 🛑 完了ゲート（全項目✅でなければ完了できない / 原則4・13・14）

- [ ] `outputs/quality_report.md` が保存済み
- [ ] 検収項目8件が PASS / RETAKE / N/A / STOP のいずれかで判定済み
- [ ] RETAKEした場合、変更値と理由が1件以上記録済み
- [ ] PASS音声のファイル名が記録済み、またはコマンド生成のみであることが記録済み
- [ ] 禁止用途リスクが STOP ではない

判定:
- すべて✅なら → スキル完了報告
- ❌が1つでもあれば → この工程の該当箇所に戻って修正し、再判定する
