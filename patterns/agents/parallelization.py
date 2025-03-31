from concurrent.futures import ThreadPoolExecutor
from typing import List
from util import llm_call

def parallel(prompt: str, inputs: List[str], n_workers: int = 3) -> List[str]:
    """
    Parallelization パターン
    同じプロンプトを使用して複数の入力を並列に処理する関数。

    Args:
        prompt: すべての入力に適用する共通のプロンプト
        inputs: 処理する入力のリスト
        n_workers: 並列処理に使用するワーカーの最大数

    Returns:
        各入力に対する処理結果のリスト
    """
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(llm_call, f"{prompt}\n入力: {x}") for x in inputs]
        return [f.result() for f in futures]

def main():
    """メイン実行関数"""
    # 例: ステークホルダーごとの影響分析を並列処理
    stakeholders = [
        """顧客:
        - 価格に敏感
        - より良い技術を求めている
        - 環境への関心が高い""",

        """従業員:
        - 雇用安定性への不安
        - 新しいスキルが必要
        - 明確な方向性を望んでいる""",

        """投資家:
        - 成長を期待
        - コスト管理を求めている
        - リスクに関する懸念""",

        """サプライヤー:
        - 供給能力の制約
        - 価格圧力
        - 技術移行の課題"""
    ]

    print("ステークホルダー影響分析の並列処理を開始します...\n")
    impact_results = parallel(
        """このステークホルダーグループに対する市場変化の影響を分析してください。
        具体的な影響と推奨される対応策を提供してください。
        明確なセクションと優先順位で情報を整理してください。""",
        stakeholders
    )

    # 結果の表示
    stakeholder_names = ["顧客", "従業員", "投資家", "サプライヤー"]
    for i, result in enumerate(impact_results):
        print(f"\n\n{stakeholder_names[i]}への影響分析:")
        print("=" * 40)
        print(result)

if __name__ == "__main__":
    main()
