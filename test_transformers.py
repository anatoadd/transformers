from transformers import pipeline

# 質問応答のパイプラインを使用
qa_pipeline = pipeline("question-answering")

# サンプルのコンテキストと質問
context = "Hugging Face is creating a tool that democratizes AI."
question = "What is Hugging Face creating?"

# 質問に対する回答
result = qa_pipeline(question=question, context=context)
print(result)
