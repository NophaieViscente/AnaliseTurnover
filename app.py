import streamlit as st
from joblib import load
import numpy as np
import os


# streamlit_app = nome do app

st.header('Aplicativo para a Predição de Turnover de Colaboradores.')
#st.subheader('Construído em Python')
st.markdown('Insira as informações para efetuar as previsões.')

# Seleção de Empresas
listaEmpresas = ['101 - Industria de Compensados Guararapes','103 - Industria de Compensados Guararapes',
'201 - PalmasPlac','701 - Guararapes Painéis',
'702 - Guararapes Painéis','703 - Guararapes Painéis'] 
empresa = st.radio('Informe a Empresa onde o trabalhador é lotado:',options=listaEmpresas)
if empresa in listaEmpresas :
       empresa = listaEmpresas.index(empresa)
       if empresa == 0 :
              cidadeEmpresa = 0
       elif empresa == 1 :
              cidadeEmpresa = 1
       elif empresa == 2 :
              cidadeEmpresa = 0
       elif empresa == 3 :
              cidadeEmpresa = 2
       elif empresa == 4 :
              cidadeEmpresa = 3
       else :
              cidadeEmpresa = 4


# Faixa Salarial
#listaFaixaSalarial = ['Até 01 Salário Mínimo','De  01 Até 02 Salários Mínimos','De  02 Até 03 Salários Mínimos',
 #'De  03 Até 04 Salários Mínimos','De  04 Até 05 Salários Mínimos','De  05 Até 06 Salários Mínimos',
 #'De  06 Até 07 Salários Mínimos','De  07 Até 08 Salários Mínimos','De  08 Até 09 Salários Mínimos',
 #'De  09 Até 10 Salários Mínimos','De  10 Até 11 Salários Mínimos', 'De  11 Até 12 Salários Mínimos',
 #'De  12 Até 13 Salários Mínimos', 'De  13 Até 14 Salários Mínimos','De  14 Até 15 Salários Mínimos',
 #'De  15 Até 20 Salários Mínimos',  'Acima  20 Salários Mínimos']
#faixaSalarial = st.selectbox('Escolha a faixa salarial do Funcionário',options = listaFaixaSalarial)
#if faixaSalarial in listaFaixaSalarial :
#       faixaSalarial = listaFaixaSalarial.index(faixaSalarial)

salario = st.number_input('Digite o Salário do Funcionário',min_value=1100.00)


# Dependentes
listaDependentes = ['Nenhum','1','2','3','4','5','6','7','8','9']
dependentes = st.selectbox('Escolha a Quantidade de Dependentes do Funcionário :',options = listaDependentes)
if dependentes in listaDependentes :
       dependentes = listaDependentes.index(dependentes)

# Sexo Funcionário
listaSexo = ['Masculino','Feminino']
sexoFuncionario = st.radio('Escolha o Sexo do Funcionário :',options = listaSexo)
if sexoFuncionario in listaSexo :
       sexoFuncionario = listaSexo.index(sexoFuncionario)

# Estado Civil Funcionário
listaEstadoCivil = ['Casado','Solteiro', 'Viúvo', 'Divorciado',
       'Separado Judicialmente', 'União Estável', 'Desquitado', 'Outros']
estadocivil = st.selectbox('Escolha o estado civil do Funcionário :',options = listaEstadoCivil)
if estadocivil in listaEstadoCivil :
       estadocivil = listaEstadoCivil.index(estadocivil)

# Grau de Instrução Funcionário
listaInstrucao = ['Analfabeto','4ª serie incompleta Ensino Fun','4ª completa Ensino Fundamental','5ª/8ª Ensino Fundamental',
        'Ensino Fundamental Completo','Ensino Medio Incompleto','Ensino Medio Completo', 'Técnico','Superior Incompleto', 
         'Superior Completo','Superior Completo - Pós Gradua']     
instrucao = st.selectbox('Escolha o Grau de Escolaridade do Funcionário :',options=listaInstrucao)
if instrucao in listaInstrucao :
       instrucao = listaInstrucao.index(instrucao)


# Funcionário Sindicalizado ou não
listaFuncionarioSindicalizado = ['Sim','Não']
sindicalizado = st.radio('Funcionário Sindicalizado ?',options=listaFuncionarioSindicalizado)
if sindicalizado in listaFuncionarioSindicalizado :
       sindicalizado = listaFuncionarioSindicalizado.index(sindicalizado)

# Se recebe insalubridade ou não
listaRecebeInsalubridade = ['Não Recebe','Recebe']
insalubridade = st.radio('Funcionário Recebe Insalubridade ?',options=listaRecebeInsalubridade)
if insalubridade in listaRecebeInsalubridade :
       insalubridade = listaRecebeInsalubridade.index(insalubridade)

# Se recebe periculosidade ou não
listaRecebePericulosidade = ['Não Recebe','Recebe']
periculosidade = st.radio('Funcionário Recebe Periculosidade ?',options=listaRecebePericulosidade)
if periculosidade in listaRecebePericulosidade :
       periculosidade = listaRecebePericulosidade.index(periculosidade)

# Carga Horária do Funcionário
listaCargaHoraria = ['220','200','180','100','60','30']
cargaHoraria = st.selectbox('Escolha a Carga Horária do Funcionário :',options=listaCargaHoraria)
if cargaHoraria in listaCargaHoraria :
       cargaHoraria = listaCargaHoraria.index(cargaHoraria)

# Efetuando as predições
if (os.path.exists('modeloXGB_binary.pkl')):
    modelo = load('modeloXGB_binary.pkl')
    botao = st.button('Efetuar previsão')
    if(botao):
        listaValores = np.array([[empresa,cidadeEmpresa,salario,sexoFuncionario,dependentes,estadocivil,
        instrucao,sindicalizado,insalubridade,periculosidade,cargaHoraria]])
        resultado = modelo.predict(listaValores)
        if(resultado[0] == 0):
              st.write('Há baixa probabilidade de saída no período de 1 ano.')
        else :
              st.write('Há probabilidade de desligamento no período de 1 ano.')
else:
	st.error('Erro ao carregar o modelo preditivo. Contate o administrador do sistema')
