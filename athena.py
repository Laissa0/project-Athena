import google.generativeai as genai
import re

genai.configure(api_key="sua-api-key")

# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)

# system_instruction = "Voce é uma assiste social competente e preparada para dar suporte e instruções para vitimas de violência domestica ou abuso psicologico ou sexual"
generation_config = {
    "candidate_count": 1,
    "temperature": 1,
}

safety_settings = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

system_instruction = "Você é um assistente social competente e preparada para oferecer apoio e orientação a vítimas de violência doméstica, abuso psicológico ou sexual."

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", 
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                               system_instruction=system_instruction
                              )

chat = model.start_chat(history=[])

bem_vinda = "- Olá, eu sou Athena e estou aqui para te dar suporte -"
print(len(bem_vinda) * "-")
print(bem_vinda)
print(len(bem_vinda) * "-")
print("***   Digite '1' para encerrar    ***")
print("")


# [EMERGÊNCIAS]
def detectar_emergencia(mensagem):
    palavras_chave = ["socorro", "scrr", "soco" , "sco", "ajuda", "aju", "ajd", "estou em perigo", "preciso de ajuda", "me sinto ameaçada", "medo"]

    padrao = "|".join(palavras_chave)
    regex = re.compile(padrao, re.IGNORECASE)

    if regex.search(mensagem):
        return True
    else:
        return False


# [INICIO PADRÃO]
while True:
    texto = input("posso te ajudar em algo hoje? ")

    if detectar_emergencia(texto):
        print("Detectamos uma situação de emergência. Por favor, entre em contato com as autoridades imediatamente.")
        resposta_autoridades = input("Ligar para as autoridades? [1] SIM [2] NÃO: ")
        if resposta_autoridades == "1":
            print("Ligando...")
        elif resposta_autoridades == "2":
            print("Estou aqui para ajudar. Por favor, me avise se precisar de mais alguma coisa.")
        else:
            print("Desculpe, não entendi. Por favor, responda com '1' para SIM ou '2' para NÃO.")
        break

    if texto == "1":
        break

    response = chat.send_message(texto)
    # resposta_athena = processar_resposta(response.text)
    # print("Athena:", resposta_athena, "\n","\n")
    print("Athena:", response.text, "\n","\n")


print("Encerrando Chat")
