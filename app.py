from transformers import pipeline

class AnalisadorDeSentimentos :def__init__(self) :
  self.modelo = pipeline("sentimentanalysis", model="nlptown/bert-base-multilingual-uncased-sentiment" )
 
def analisar(self.modelo(texto) [0]
return f"sentimento:
{res[` label ` ] } - confiança:
{res[` label ` ] : . 2f}"
ia = AnalisadorDeSentimentos() 
print(ia.analisar("esse projeto ficou muito bom! " ))
