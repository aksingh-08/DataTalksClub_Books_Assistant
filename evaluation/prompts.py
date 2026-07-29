JUDGE_PROMPT = """
You are evaluating the answer produced by a RAG system.

Question:
{question}

Reference Answer:
{reference_answer}

Generated Answer:
{generated_answer}

Instructions:

1. Ignore wording differences.
2. Ignore formatting differences.
3. Focus on factual correctness.
4. If the generated answer conveys the same meaning as the reference answer,
   mark it Correct.
5. If it is partially correct but missing important information,
   mark it Partially Correct.
6. If it is wrong,
   mark it Incorrect.

Respond with ONLY ONE WORD:

Correct

or

Partially Correct

or

Incorrect
"""