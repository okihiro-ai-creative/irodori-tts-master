# irodori-tts-master

Created by OKIHIRO — AI自動化ワークフローを130個以上開発・運用しています。

`irodori-tts-master` は、Irodori-TTS v3 / VoiceDesign を使って日本語TTS用のキャラクター固定、VoiceDesign caption、seed、絵文字制御、推論コマンドを設計するためのAIスキルです。

このパッケージは Irodori-TTS 本体ではありません。音声生成エンジンは公式リポジトリを別途クローンして使います。

## 何ができるか

- 台本をIrodori-TTS向けに整形する
- VoiceDesign captionを設計する
- seedと主要パラメータを固定してキャラクター再現性を高める
- 参照音声なし、参照音声あり、Speaker Inversion前提の設計を切り替える
- 絵文字スタイル制御を使うか判断する
- Irodori-TTSのCLI推論コマンドを作る
- 生成音声の検収とリテイク方針を記録する
- 生成後の音声に軽い明瞭化後処理をかける

## 最初に読むファイル

1. `SETUP.md`
2. `VERIFICATION.md`
3. `SKILL.md`
4. `steps/step1_intake.md`

## 基本構成

```text
irodori-tts-master/
├── README.md
├── SETUP.md
├── SETUP_AND_USAGE.html
├── VERIFICATION.md
├── SKILL.md
├── steps/
│   ├── step1_intake.md
│   ├── step2_text_normalization.md
│   ├── step3_character_preset.md
│   ├── step4_command_plan.md
│   └── step5_quality_loop.md
└── resources/
    ├── CHARACTER_PRESET_TEMPLATE.md
    ├── CAPTION_GUIDE.md
    ├── EMOJI_STYLE_CONTROL.md
    ├── PARAMETER_GUIDE.md
    ├── SAFETY_AND_LICENSE.md
    └── KNOWN_MISTAKES.md
```

## 注意

- seedだけでキャラクターを固定できるわけではありません。`checkpoint + caption + seed + sampling + reference mode` をセットで固定してください。
- 実在人物や第三者の声を同意なくクローンしないでください。
- Irodori-TTSの導入と実行は `SETUP.md` の順番で進めてください。

---

## このツールを自分の業務に合わせてカスタマイズしたい方へ

このツールをベースに、あなたの環境・業務に合わせたカスタマイズや、
新しい自動化ツールの開発をご相談いただけます。

▶ ご相談はこちら: https://forms.gle/2a2vfn7E3rYGcbex7
