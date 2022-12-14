# Utilizar requisição abaixo para testar a API
# http://127.0.0.1:8000/sudoko?numeros=010600300027000060083004107001005926040720801250801403032409000508160000060008009
# Teste de API para o Sudoko

from fastapi import FastAPI, Query
from Resolve_Sudoko import resolve

app = FastAPI()


@app.get('/sudoko')
async def resultado(numeros: str = Query(default=None, min_length=81, max_length=81)):
    resolvido = resolve(numeros)

    return {'resultado': resolvido}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0",  port=8000, reload=True)
