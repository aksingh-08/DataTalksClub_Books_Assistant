from evaluation.evaluator import evaluate
from evaluation.report import generate_report

results = evaluate()

df = generate_report(results)

print(df)