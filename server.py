from starlette.applications import Starlette
from starlette.responses import JSONResponse
import uvicorn    
import nltk.data

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

app = Starlette(debug=True)

@app.route('/sent-tok', methods=['POST'])
async def sent_tok(req):
    params = await req.json()
    text = params["text"]
    sents = sent_detector.tokenize(text.strip())
    return JSONResponse({"sentences": sents})
