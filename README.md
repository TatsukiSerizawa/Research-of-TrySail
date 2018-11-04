# Clustering of TrySail

TrySailが好きすぎて気付いたら3人を分類するプログラムを作ってた。

あとナンスが可愛い。

## 手順

1. スクレイピングして画像を収集

scraping.py

2. 顔領域を切り出し

face_recog.py

3. 画像サイズを64✕64にリサイズ

resize.py

4. 画像を水増し

padded.py

X. CNNで顔画像を学習

## 参考

Scraping: https://qiita.com/tsuro/items/fa7bb3015feca1212732