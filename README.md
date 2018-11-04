# Clustering of TrySail

TrySailが好きすぎて気付いたら3人を分類するプログラムを作ってた。

あとナンスが可愛い。

## 手順

1. スクレイピングして画像を収集

scraping.py

2. OpenCVで顔領域を切り出してラベルを付与して保存

face_recog.py

resize.py

3. CNNで顔画像を学習

## 参考

Scraping: https://qiita.com/tsuro/items/fa7bb3015feca1212732