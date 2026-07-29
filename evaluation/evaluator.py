from evaluation.dataset import load_dataset
from evaluation.metrics import (
    source_precision,
    source_recall,
    source_f1,
    exact_match,
    answer_overlap,
)
from evaluation.llm_judge import LLMJudge

from rag.pipeline import RAGPipeline


def evaluate():

    rag = RAGPipeline()

    judge = LLMJudge()

    dataset = load_dataset()

    results = []

    for sample in dataset:

        response = rag.ask(sample["question"])

        judge_result = judge.judge(
            question=sample["question"],
            reference_answer=sample["expected_answer"],
            generated_answer=response.answer,
        )

        results.append(
            {
                'question_number': len(results) + 1,
                "question": sample["question"],

                "expected_answer": sample["expected_answer"],

                "generated_answer": response.answer,

                "expected_sources": sample["expected_sources"],

                "retrieved_sources": response.sources,

                "precision": source_precision(
                    sample["expected_sources"],
                    response.sources,
                ),

                "recall": source_recall(
                    sample["expected_sources"],
                    response.sources,
                ),

                "f1": source_f1(
                    sample["expected_sources"],
                    response.sources,
                ),

                "exact_match": exact_match(
                    sample["expected_answer"],
                    response.answer,
                ),
                'answer_overlap': answer_overlap(
                    sample['expected_answer'],
                    response.answer,
                ),

                "judge": judge_result,

                "response_time": response.response_time,

                "prompt_tokens": response.prompt_tokens,

                "completion_tokens": response.completion_tokens,

                "total_tokens": response.total_tokens,
            }
        )

    return results