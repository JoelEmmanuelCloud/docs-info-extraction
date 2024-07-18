def get_system_prompt():
    system_prompt = """
Você é um assistente de um escritório e trabalha analisando o conteúdo de notas fiscais"
"""
    return system_prompt


def get_user_prompt():

    json_response_format = """
<json>
{
    "data_hora_emissao":
    "nome_tomador":
    "cnpj_tomador":
    "valor_liquido":
    "impostos":
    "data_vencimento":
    "numero_documento"
}
</>json
"""
    user_prompt = f"""
Sua tarefa é extrair as seguintes informações do documento que foi enviado:

<info>
    - Data e Hora de Emissão
    - Nome/Razão Social Tomador
    - CNPJ Tomador
    - Valor Líquido da Nota Fiscal 
    - Impostos 
    - Código de pagamento do boleto
    - Data de Vencimento 
    - Número do Documento
</info>

    Respire fundo e revise cuidadosamente sua resposta. Certifique-se de verificar a formatação e as informações do JSON várias vezes para garantir que não haja erros. 
    Sua resposta é crucial para o processo, então preste muita atenção à precisão da formatação do JSON.
    O padrão de resposta deve seguir:
    {json_response_format}
"""
    return user_prompt
