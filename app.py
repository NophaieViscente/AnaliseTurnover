import streamlit as st
from joblib import dump, load
import numpy as np
import os
import sklearn

# streamlit_app = nome do app

st.header('Predição de Turnover de Colaboradores')
#st.subheader('Construído em Python')
st.markdown('Insira as informações para efetuar as previsões')

# Seleção de Empresas
listaEmpresas = ['101 - Industria de Compensados Guararapes','103 - Industria de Compensados Guararapes',
'201 - PalmasPlac','701 - Guararapes Painéis',
'702 - Guararapes Painéis','703 - Guararapes Painéis'] 
empresa = st.radio('Informe a Empresa onde o trabalhador é lotado:',options=listaEmpresas)
if empresa in listaEmpresas :
       empresa = listaEmpresas.index(empresa)
st.write(empresa)


# Seleção de Cidade
listaCidades = ['Caçador','Curitiba','Palmas','Pernambuco','Sta Cecília']
cidadeEmpresa = st.selectbox('Escolha a cidade onde a empresa é situada', options = listaCidades)
if cidadeEmpresa in listaCidades :
       cidadeEmpresa = listaCidades.index(cidadeEmpresa)
st.write(cidadeEmpresa)

# Salário Atual
salario = st.number_input('Salario: ',min_value=0.00)


# Sexo Funcionário
listaSexo = ['Masculino','Feminino']
sexoFuncionario = st.radio('Escolha o Sexo do Funcionário?',options = listaSexo)
if sexoFuncionario in listaSexo :
       sexoFuncionario = listaSexo.index(sexoFuncionario)
st.write(sexoFuncionario)

listaEstadoCivil = ['Casado', 'Solteiro', 'Viúvo', 'Divorciado',
       'Separado Judicialmente', 'União Estável', 'Desquitado', 'Outros']
estadoCivil= st.selectbox('Escolha o estado civil do Funcionário',options = listaEstadoCivil)
if estadoCivil in listaEstadoCivil :
       estadoCivil = listaEstadoCivil.index(estadoCivil)
st.write(estadoCivil)

listaInstrucao = ['Ensino Medio Completo', '5ª/8ª Ensino Fundamental',
        '4ª completa Ensino Fundamental', 'Superior Completo - Pós Gradua',
        '4ª serie incompleta Ensino Fun', 'Ensino Medio Incompleto',
        'Ensino Fundamental Completo', 'Técnico', 'Superior Incompleto',
        'Analfabeto', 'Superior Completo']
instrucao = st.selectbox('Escolha o grau de escolaridade do funcionário',options=listaInstrucao)
if instrucao in listaInstrucao :
       instrucao = listaInstrucao.index(instrucao)
st.write(instrucao)

listaTempoEmpresa = ['26 a 30 Anos', '21 a 25 Anos', '31 a 35 Anos', '16 a 20 Anos',
        '11 a 15 Anos', '5 a 10 Anos', '5 Anos', '4 Anos', '3 Anos',
        '2 Anos', '1 Ano', 'Menos de 1 Ano']
tempoEmpresa = st.selectbox('Escolha a faixa de tempo de empresa do funcionário', options=listaTempoEmpresa)
if tempoEmpresa in listaTempoEmpresa :
       tempoEmpresa = listaTempoEmpresa.index(tempoEmpresa)
st.write(tempoEmpresa)

listaFuncionarioSindicalizado = ['Sim','Não']
sindicalizado = st.radio('Funcionário Sindicalizado ?',options=listaFuncionarioSindicalizado)
if sindicalizado in listaFuncionarioSindicalizado :
       sindicalizado = listaFuncionarioSindicalizado.index(sindicalizado)
st.write(sindicalizado)

listaRecebeInsalubridade = ['Sim','Não']
insalubridade = st.radio('Funcionário Recebe Insalubridade ?',options=listaFuncionarioSindicalizado)
if insalubridade in listaRecebeInsalubridade :
       insalubridade = listaRecebeInsalubridade.index(insalubridade)
st.write(insalubridade)

listaRecebePericulosidade = ['Sim','Não']
periculosidade = st.radio('Funcionário Recebe Periculosidade ?',options=listaFuncionarioSindicalizado)
if periculosidade in listaRecebePericulosidade :
       periculosidade = listaRecebePericulosidade.index(periculosidade)
st.write(periculosidade)

cargaHoraria = st.number_input('Carga Horária :',min_value=140)


if (os.path.exists('modelo.pkl')):
    modelo = load('modelo.pkl')
    botao = st.button('Efetuar previsão')
    if(botao):
        listaValores = np.array([[empresa,cidadeEmpresa,salario,sexoFuncionario,estadoCivil,
        instrucao,tempoEmpresa,sindicalizado,insalubridade,periculosidade,cargaHoraria]])
        resultado = modelo.predict(listaValores)
        if(resultado[0] == 0):
            st.write('Há baixa probabilidade de saída.')
        else :
            st.write('Há probabilidade de desligamento.')
else:
	st.error('Erro ao carregar o modelo preditivo. Contate o administrador do sistema')
