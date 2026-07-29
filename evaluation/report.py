from pathlib import Path

import pandas as pd


RESULTS_DIR = Path(__file__).parent / "results"
RESULTS_DIR.mkdir(exist_ok=True)


def generate_report(results):

    df = pd.DataFrame(results)

    output_file = RESULTS_DIR / "evaluation_results.csv"

    df.to_csv(
        output_file,
        index=False,
    )

    print("=" * 70)
    print("Evaluation Summary")
    print("=" * 70)

    print(f"Questions             : {len(df)}")
    print(f"Average Precision     : {df['precision'].mean():.2f}")
    print(f"Average Recall        : {df['recall'].mean():.2f}")
    print(f"Average F1            : {df['f1'].mean():.2f}")
    print(f"Exact Match           : {df['exact_match'].mean():.2f}")
    print(f"Average Response Time : {df['response_time'].mean():.2f} sec")
    print(f"Average Prompt Tokens : {df['prompt_tokens'].mean():.0f}")
    print(f"Average Completion    : {df['completion_tokens'].mean():.0f}")
    print(f"Average Total Tokens  : {df['total_tokens'].mean():.0f}")

    print("=" * 70)

    print("\nLLM Judge Results")
    print("-" * 70)

    counts = df["judge"].value_counts()

    for label, count in counts.items():
        print(f"{label:<20}: {count}")

    print("-" * 70)

    print(f"\nDetailed report saved to:\n{output_file}")

    return df