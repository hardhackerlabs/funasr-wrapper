from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn
from funasr import AutoModel

# 初始化 FastAPI 应用
app = FastAPI()
# 加载模型
model = AutoModel(model="ct-punc", device="cpu", ncpu=4)

def process_sentence(model, text):
    print(f"Processing sentence: {text}")
    res = model.generate(input=text)
    if len(res) > 0:
        return res[0]["text"]
    return text

# 定义请求数据模型
class InputData(BaseModel):
    texts: List[str]

@app.post("/restore_punct")
async def process_text(input_data: InputData):
    try:
        # 获取输入列表
        input_texts = input_data.texts
        if not isinstance(input_texts, list):
            raise HTTPException(status_code=400, detail="Input must be a list of strings")

        # 处理输入的每个字符串
        results = [process_sentence(model, text) for text in input_texts]
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7777)
