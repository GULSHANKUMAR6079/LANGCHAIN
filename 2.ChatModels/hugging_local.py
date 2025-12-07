from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline

llm=HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation",pipeline_kwargs=dict(temperature=0.5,max_new_tokens=200))
model=ChatHuggingFace(llm=llm)
result=model.invoke("What is the capital of INDIA?")
r2=model.invoke("explain me about langchain in detail ?")
print(r2)
print("="*100)
print(r2.content)
print("="*100)
print(result.content)