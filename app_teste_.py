import streamlit as st
from joblib import load
import numpy as np
import os
from datetime import date
from dateutil.relativedelta import relativedelta


# streamlit_app = nome do app

st.header('Aplicativo para a Predição de Turnover de Colaboradores.')
#st.subheader('Construído em Python')
st.markdown('Insira as informações para efetuar as previsões.')

# Seleção de Empresas
listaEmpresas = ['101 - Industria de Compensados Guararapes - PR','103 - Industria de Compensados Guararapes - SC',
'201 - PalmasPlac - PR','701 - Guararapes Painéis - SC',
'702 - Guararapes Painéis - PR','703 - Guararapes Painéis - PE','705 - Guararapes Painéis - SP'] 
empresa = st.radio('Informe a Empresa onde o trabalhador é lotado:',options=listaEmpresas)
if empresa in listaEmpresas :
       empresa = listaEmpresas.index(empresa)

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

#Idade Funcionário
#idadeFuncionario = st.number_input('Insira a idade do Funcionário em Anos :',min_value=15)
dataNascFuncionario = st.date_input('Insira a Data de Nascimento do Funcionário :',min_value=date(1950,1,1),max_value=date.today())
hoje = date.today()
idadeRelativa = relativedelta(hoje, dataNascFuncionario)
idadeFuncionario = idadeRelativa.years

# Data de Admissão Funcionário
dataAdmissao = st.date_input('Insira a Data de Admissão do Funcionário :',min_value=date(1990,1,1),max_value=date.today())
hoje = date.today()
tempoEmpresaRelativo = relativedelta(hoje, dataAdmissao)
tempoEmpresa = tempoEmpresaRelativo.years

# Dependentes
listaDependentes = ['Nenhum','1','2','3','4','5','6','7','8','9']
dependentes = st.selectbox('Escolha a Quantidade de Dependentes do Funcionário :',options = listaDependentes)
if dependentes in listaDependentes :
       dependentes = listaDependentes.index(dependentes)


# Grau de Instrução Funcionário
listaInstrucao = ['Analfabeto','4ª Série Incompleta Ensino Fundamental','4ª Série Completa Ensino Fundamental','5ª/8ª Ensino Fundamental',
        'Ensino Fundamental Completo','Ensino Medio Incompleto','Ensino Medio Completo', 'Técnico','Superior Incompleto', 
         'Superior Completo','Superior Completo - Pós Graduado']     
instrucao = st.selectbox('Escolha o Grau de Escolaridade do Funcionário :',options=listaInstrucao)
if instrucao in listaInstrucao :
       instrucao = listaInstrucao.index(instrucao)

#Salário Funcionário
salario = st.number_input('Digite o Salário do Funcionário',min_value=1100.00)

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

# Se houve Absenteísmo ou não no mês.
listaAbsenteismo = ['Não Houve','Houve']
absenteismo = st.radio('Houve Absenteísmo no mês vigente ?',options=listaAbsenteismo)
if absenteismo in listaAbsenteismo :
       absenteismo = listaAbsenteismo.index(absenteismo)

# Se houve Afastamento ou não no mês.
listaAfastamento = ['Não Houve','Houve']
afastamento = st.radio('Houve Afastamento no mês vigente ?',options=listaAfastamento)
if afastamento in listaAfastamento :
       afastamento = listaAfastamento.index(afastamento)

# Efetuando as predições
if (os.path.exists('modeloXGB_final.pkl')):
    modelo = load('modeloXGB_final.pkl')
    botao = st.button('Efetuar previsão')
    if(botao):
        listaValores = np.array([[empresa,sexoFuncionario,idadeFuncionario,dependentes,estadocivil,
        instrucao,salario,sindicalizado,insalubridade,periculosidade,cargaHoraria,absenteismo,afastamento,tempoEmpresa]])
        resultado = modelo.predict(listaValores)
        prob = modelo.predict_proba(listaValores)
        if(resultado[0] == 0):
              st.write('A probabilidade de permanência é de {:.2f}%'.format([prob][0][0][0]*100))
        else :
              st.write('A probabilidade de desligamento é de {:.2f}%'.format([prob][0][0][1]*100))
else:
	st.error('Erro ao carregar o modelo preditivo. Contate o administrador do sistema')
