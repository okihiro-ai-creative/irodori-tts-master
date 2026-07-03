# STEP 4: 推論コマンドと生成計画

### ⬅️ 着手前に読む（前工程の成果物）

📖 必読: `outputs/intake.md`（実行環境と出力先を引き継ぐため）
📖 必読: `outputs/normalized_text.md`（CLIに渡す本文を確認するため）
📖 必読: `outputs/character_preset.yaml`（固定値をCLIへ反映するため）
📖 必読: `resources/PARAMETER_GUIDE.md`（引数の意味と調整順を確認するため）

---

## この工程でやること

`outputs/inference_plan.md` を作成する。Irodori-TTS CLIコマンド、出力wav名、固定パラメータ、再生成時に変えてよい値・変えてはいけない値を記録する。

### コマンド雛形

```bash
uv run --no-sync python infer.py \
  --hf-checkpoint Aratako/Irodori-TTS-600M-v3-VoiceDesign \
  --text "{outputs/normalized_text.md の本文}" \
  --caption "{outputs/character_preset.yaml の caption}" \
  --no-ref \
  --seed {seed} \
  --num-steps {num_steps} \
  --cfg-scale-text {cfg_scale_text} \
  --cfg-scale-caption {cfg_scale_caption} \
  --duration-scale {duration_scale} \
  --output-wav "{output_wav}"
```

### ref_wav使用時の追加

```bash
  --ref-wav "{reference.ref_wav}" \
  --cfg-scale-speaker {cfg_scale_speaker}
```

`--no-ref` と `--ref-wav` は同時に使わない。

### ファイル操作の可否（原則8）

| 操作 | 可否 |
|---|---|
| `outputs/inference_plan.md` を作成 | ✅ |
| wavを生成する | ユーザーが実行を明示した場合のみ✅ |
| 既存wavを上書き | ✗ 禁止（理由: 比較検収ができなくなるため） |

### 正例・反例（原則3）

✅ 正例:
```markdown
固定する値:
- checkpoint
- caption
- seed
- num_steps
- cfg_scale_text
- cfg_scale_caption

変えてよい値:
- output_wav
- text（別セリフ生成時のみ）
```

✗ 反例:
```markdown
うまくいかなければ適当にseedやcaptionを変える。
```

変更点が記録されず、キャラクター再現性が失われる。

### 実行環境の選択

#### ローカル実行（通常時）
```bash
cd "<Irodori-TTS repo>"
uv run --no-sync python infer.py ...
```

#### Google Colab実行

今回の無料配布物にはColabノートブックを含めない。Colab運用はこの配布物の対象外として扱い、必要な場合は利用者側で別途ノートブックと実行手順を用意する。

---

### この工程固有の禁止事項（原則2）

- ✗ `--no-ref` と `--ref-wav` を同時に指定することを禁止する。なぜならIrodori-TTSの参照条件が排他的だからだ。
- ✗ 出力wav名を毎回同じにすることを禁止する。なぜなら検収前の音声を上書きするからだ。

---

### 🛑 完了ゲート（全項目✅でなければ次に進めない / 原則4・13・14）

- [ ] `outputs/inference_plan.md` が保存済み
- [ ] CLIコマンドが1本以上ある
- [ ] `--seed` がコマンドに含まれている
- [ ] no_ref / ref_wav / ref_latent / ref_embed の排他条件が守られている
- [ ] 出力wavパスが既存ファイルを上書きしない名前になっている

判定:
- すべて✅なら → 次に開く: `steps/step5_quality_loop.md`
- ❌が1つでもあれば → この工程の該当箇所に戻って修正し、再判定する
