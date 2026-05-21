# CSV Error Log Tool


## 概要

このツールは、CSV形式のログファイルから `status` 列が `ERROR` の行だけを抽出し、
`error.log` に書き出すためのスクリプトです。

- 入力: input.csv（id, status, message などの列を持つCSV）
- 出力: error.log（ERROR行のみを1行1レコードで出力）
- 実行すると、全体の行数とERROR行数をターミナルに表示します。



## 学び・振り返り

- csv.DictReader を使って、ヘッダ付きCSVを1行ずつ辞書として扱う方法を学んだ
- ループの中で全行数をカウントしつつ、status が "ERROR" の行だけを別リストに集める処理を書けるようになった
- with open(..., "r"/"w") を使ったファイル入出力の基本的なパターンを復習できた
- CSVの入力 → 条件抽出 → ログファイルへの出力という、シンプルなETL処理の流れを体験できた