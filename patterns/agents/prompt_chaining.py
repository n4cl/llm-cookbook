from typing import List
from util import llm_call

def chain(input: str, prompts: List[str]) -> str:
    """
    Prompt-Chaining パターン
    複数のLLM呼び出しを順番に実行し、結果を次のステップに渡す関数。

    Args:
        input: 初期入力文字列
        prompts: 実行するプロンプトのリスト

    Returns:
        最終的な結果の文字列
    """
    result = input
    for i, prompt in enumerate(prompts, 1):
        print(f"\nステップ {i}:")
        result = llm_call(f"{prompt}\n入力: {result}")
        print(result)
    return result

def main():
    """メイン実行関数"""
    # 例: データの抽出と整形のためのチェーンワークフロー
    data_processing_steps = [
        """テキストから数値とそれに関連するメトリクスのみを抽出してください。
        各行を「値: メトリクス」の形式で表示してください。
        例:
        92: 顧客満足度
        45%: 収益成長率""",

        """可能な限り全ての数値をパーセンテージに変換してください。
        パーセンテージやポイントでない場合は、小数点表記に変換してください（例: 92ポイント → 92%）。
        各行に1つの数値を表示してください。
        例:
        92%: 顧客満足度
        45%: 収益成長率""",

        """すべての行を数値の降順に並べ替えてください。
        各行の形式は「値: メトリクス」を維持してください。
        例:
        92%: 顧客満足度
        87%: 従業員満足度""",

        """並べ替えたデータをマークダウンテーブルとして整形してください。列は以下の通りです:
        | メトリクス | 値 |
        |:--|--:|
        | 顧客満足度 | 92% |"""
    ]

    report = """
    第3四半期業績サマリー:
    当四半期の顧客満足度スコアは92ポイントに上昇しました。
    収益は前年比45%成長しました。
    主要市場でのマーケットシェアは現在23%です。
    顧客離れは8%から5%に減少しました。
    新規ユーザー獲得コストはユーザーあたり43ドルです。
    製品採用率は78%に増加しました。
    従業員満足度は87ポイントです。
    営業利益率は34%に改善しました。
    """

    print("\n入力テキスト:")
    print(report)
    formatted_result = chain(report, data_processing_steps)
    print("\n最終結果:")
    print(formatted_result)

if __name__ == "__main__":
    main()
