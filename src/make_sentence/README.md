# Make sentence from blog

Blogから文章を抽出した上で学習を行い，文章を生成します．

## Directory description
- create_files.pyを実行することでscraping.pyも呼び出されて実行，スクレイピングした文章をファイルに保存する．
- 引数にファイル名を入れてmake_sentence.pyを実行することでmarkov.pyも呼び出されて実行，文章を形態素解析した上でマルコフ連鎖でモデルを作って文章を生成する．
- make_sentence_original.py: ライブラリでエラーが出る

## References
- 麻倉ももについての説明とブログのスクレイピング, http://be-07.hatenablog.com/entry/2016/12/22/000356
- アメブロのブログ記事をスクレイピングで全件取得する方法, http://be-07.hatenablog.com/entry/2016/12/23/012055
- [Python] MeCab とマルコフ連鎖ライブラリ markovify を使い、文章を学習して自動生成する方法, https://qiita.com/shge/items/fbfce6b54d2e0cc1b382#%E3%83%9E%E3%83%AB%E3%82%B3%E3%83%95%E9%80%A3%E9%8E%96%E3%81%A8%E3%81%AF