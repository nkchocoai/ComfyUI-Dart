# ComfyUI-Dart
![Dart Preview](workflows/dart_generate_with_config.png)  
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)用のカスタムノードです。
- [Dart(Danbooru Tags Transformer)](https://huggingface.co/p1atdev/dart-v1-sft) によりdanbooruタグを生成するノードを追加します。

## Installation
```
cd <ComfyUI directory>/custom_nodes
git clone https://github.com/nkchocoai/ComfyUI-Dart.git
```

## Nodes
### Dart Generate
- [Dart(Danbooru Tags Transformer)](https://huggingface.co/p1atdev/dart-v1-sft) によりdanbooruタグを生成します。
- promptの構文は以下のURLを参照ください。
  - https://huggingface.co/p1atdev/dart-v1-sft#prompt-guidde
- `remove_tags`で指定したタグは出力されません。

### Dart Compose Prompt
- Dart Generateノードの入力であるpromptを生成します。

### Dart Generation Config
- Dart Generateノードの入力であるconfigを生成します。

### Dart Ban Tags From Regex
- 正規表現にマッチしたDart Generateノードの入力であるban tagsを生成します。
- 複数行に分けることで複数の正規表現で検索することができます。

### Dart Generate(Advanced)
- [Dart(Danbooru Tags Transformer)](https://huggingface.co/p1atdev/dart-v1-sft) により生成されたdanbooruタグのトークンID列を出力します。
- promptの構文は以下のURLを参照ください。
  - https://huggingface.co/p1atdev/dart-v1-sft#prompt-guidde

### Dart Decode
- トークンID列をデコードします。

### Dart Rearranged By Animagine
- トークンID列をAnimagineのプロンプト順にソートします。

### Dart Decode By Splited Parts
- 要素ごとに分割したトークンID列をデコードした文字列を出力します。

### Dart Remove Tag Token
- トークンID列から指定したタグを削除します。
