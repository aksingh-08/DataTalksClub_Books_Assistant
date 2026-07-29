from rag.llm import generate_answer

from evaluation.prompts import JUDGE_PROMPT


class LLMJudge:

    def judge(
        self,
        question: str,
        reference_answer: str,
        generated_answer: str,
    ) -> str:

        prompt = JUDGE_PROMPT.format(
            question=question,
            reference_answer=reference_answer,
            generated_answer=generated_answer,
        )

        verdict, _ = generate_answer(prompt)

        verdict = verdict.strip()

        if verdict == "Correct":
            return "Correct"

        if verdict == "Partially Correct":
            return "Partially Correct"

        return "Incorrect"