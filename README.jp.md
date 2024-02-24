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
- [Dart(Danbooru Tags Transformer)](https://huggingface.co/p1atdev/dart-v1-sft) によりプロンプトを生成します。
- promptの構文は以下のURLを参照ください。
  - https://huggingface.co/p1atdev/dart-v1-sft#prompt-guidde

### Dart Compose Prompt
- Dart Generateノードの入力であるpromptを生成します。

### Dart Generation Config
- Dart Generateノードの入力であるconfigを生成します。
