import os
import time
import pandas as pd 
from InquirerPy import inquirer
from InquirerPy.validator import NumberValidator

pasta_destino = os.path.join(os.getcwd(), 'baixa_do_estoque.xlsx')

try:
    df = pd.read_excel(pasta_destino)
    np = df.to_dict('records')
except:
    np = []
while True:
    
    def options():
        op = inquirer.select(
            message='Cadastro',
            choices=[
            {'name': '📉 Dar baixa em alimentos', 'value': 'baixa'},
            {'name': '➕ Registrar entrada de estoque', 'value': 'entrada'},
            {'name': '📋 Ver Relatório de consumo', 'value': 'relatorio'},
            {'name': '📋 Buscar Alimento', 'value': 'busca'},
            {'name': '❌ Excluir Registros', 'value': 'excluir'},
            {'name': '🚪 Sair do programa', 'value': 'sair'},
            ]
        ).execute()
        return op

    def operations(op, np, pasta_destino):
        if op == 'baixa':
          addn = inquirer.text(message = 'Digite o Nome do Alimento: ').execute()
          addt = inquirer.text(message = 'Digite o dia que foi usado: ').execute()
          addq = inquirer.text(message = 'Digite quantos foram  usados: ',
          validate = NumberValidator(message='Por favor, digite um número válido.')).execute()
          addi = len(np) + 1
          np.append({
              'ID': addi,
              'Alimento':addn,
              'Data de consumo':addt,
              'Quantidade':int(addq)
              })
          print(f'✅Baixa de {addn} aplicada com sucesso')
          
          df_local = pd.DataFrame(np)
          df_local.to_excel(pasta_destino, index=False)
        
        if op == 'entrada':
            addn = inquirer.text(message = 'Digite o Nome do Alimento: ').execute()
            addte = inquirer.text(message = 'Digite o dia da Entrada: ').execute()
            addq = inquirer.text(message = 'Digite a quantidade: ',
            validate = NumberValidator(message='Por favor, digite um número válido.')).execute()
            addi = len(np) + 1
            np.append({
                'ID': addi,
                'Alimento':addn,
                'Data de entrada':addte,
                'Quantidade':int(addq)
                })
            print(f'✅{addn} registrado no estoque')
            
            df_local = pd.DataFrame(np)
            df_local.to_excel(pasta_destino, index=False)
            
        if op == 'relatorio':
            if not np:
                print('\n⚠️ O estoque está vazio no momento.\n')
                time.sleep(2)
                return np
            
            df = pd.DataFrame(np)
            print(df)
            time.sleep(2)
            ver = input('Quer abrir o arquivo XLSX? (s/n): ').lower().strip() 
            if ver == 's':
                df.to_excel(pasta_destino, index=False)
                print('🔄 Abrindo o arquivo no Excel...')
                os.startfile(pasta_destino) 
            elif ver == 'n':
                print('Voltando para o cadastro...')
                pass
            else:
                print('Não corresponde')
        
        if op == 'busca':
            bu = inquirer.text(message='Qual é o nome do alimento pretende buscar: ').execute()
            encon = False
            for alimento in np[:]:
                if alimento['Alimento'].lower() == bu.lower():
                    id_alim = alimento.get('ID', '-')
                    nome_alim = alimento.get('Alimento', '-')
                    qtd_alim = alimento.get('Quantidade', '-')
                    if 'Data de entrada' in alimento and pd.notna(alimento['Data de entrada']):
                        data_info = f"Data de Entrada: {alimento['Data de entrada']}"
                    else:
                        data_info = f"Data de Consumo: {alimento.get('Data de consumo', '-')}"
                    
                    print(f"📌 [ID: {id_alim}] {nome_alim} | Qtd: {qtd_alim} | {data_info}")
                    encon = True
            if not encon:
                print('❌ Alimento não encontrado no registro.')
                
        if op == 'excluir':
            re = inquirer.text(message='Qual é o nome do alimento a ser removido: ').execute()
            encon = False
            for alimento in np[:]:
                if alimento['Alimento'].lower() == re.lower():
                    np.remove(alimento)
                    print('❌ Removido com sucesso')
                    encon = True
            if encon:
                df_local = pd.DataFrame(np) 
                df_local.to_excel(pasta_destino, index=False)
                print('💾 Planilha atualizada com sucesso!')
            else:
                print('⚠️ Alimento não encontrado.')
                
        return np
    
    escolha = options()
    
    if escolha == 'sair': # Mudado de 'op' para 'escolha' e corrigida a indentação
        df_final = pd.DataFrame(np)
        df_final.to_excel(pasta_destino, index=False)
        print('💾 Alterações salvas com sucesso! Saindo...')
        break 
        
    np = operations(escolha, np, pasta_destino)
                    
                
          
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
