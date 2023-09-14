import streamlit as st
import pandas as pd
import numpy as np
import numpy_financial as npf
from datetime import datetime, timedelta
from PIL import Image


image = Image.open('Suzano.PNG')

suporte = pd.read_excel('Analise_Fim.xlsx')
#st.write(suporte)
st.set_page_config (page_title="Modelagem Financeira Capex", layout='wide')
st.image(image=image)
st.title('Análise de Viabilidade de Projeto - Capex')
# Configuração da página 
#st.set_page_config (page_title="Modelagem Financeira Capex" )
st.title('Cadastro')

st.sidebar.success('Menu de Navegação')


with st.form(key='Cadastrar'):
    nome_projeto = st.text_input('Nome do Projeto')
    col1,col2, col3 = st.columns(3)
    with col1:
        natureza = st.selectbox(label='Natureza', options=['Modernização', 'Expansão'])
    with col2:   
        diretoria = st.selectbox(label='Diretoria', options=['Florestal', 'Celulose', 'Papel'])
    with col3:
        site = st.selectbox(label='Site', options=['ARA', 'MUC', 'TLS', 'LIM'])
    col4, col5, col6 = st.columns(3)
    with col4:
        data_incial = st.date_input('Data Inicial')
    with col5:
        data_final = st.date_input('Data Final')
    with col6:
        vida_util = st.number_input(label='Vida Util do Equipamento', step=1)

    objetivo = st.text_area("Objetivo", height=100)
    escopo = st.text_area("Escopo", height=100)
    risco = st.text_area("Risco", height=100)
    beneficio = st.text_area("Beneficios", height=100)

    add_suporte = st.form_submit_button('Cadastrar')
    if add_suporte:
        #st.write(nome_projeto, natureza)
        new_add_suporte = {'Nome do Projeto': nome_projeto, 'Natureza': natureza}
        suporte = suporte.append(new_add_suporte, ignore_index=True)
        #st.write(suporte)
        suporte.to_excel(r'C:\Users\lpalmeira\Videos\Streamlit\data\Analise_Teste.xlsx', index=False)


    #valor = st.number_input('Valor do Projeto')


st.markdown("""
    # Orçamento - 2023
    """)

col7, col8, col9, col10, col11, col12 = st.columns(6)
with col7:
    jan_23 = st.number_input('Jan-23')
with col8:
    fev_23 = st.number_input('Fev-23')
with col9:
    mar_23 = st.number_input('Mar-23')
with col10:
    abr_23 = st.number_input('Abr-23')
with col11:
    mai_23 = st.number_input('Mai-23')
with col12:
    jun_23 = st.number_input('Jun-23')
col13, col14, col15, col16, col17, col18  = st.columns(6)
with col13:
    jul_23 = st.number_input('Jul-23')
with col14:
    ago_23 = st.number_input('Ago-23')
with col15:
    set_23 = st.number_input('Set-23')
with col16:
    out_23 = st.number_input('Out-23')
with col17:
    nov_23 = st.number_input('Nov-23')
with col18:
    dez_23 = st.number_input('Dez-23')

total_orc_23 = jan_23+fev_23+mar_23+abr_23+mai_23+jun_23+jul_23+ago_23+set_23+out_23+nov_23+dez_23

st.markdown("""
    # Orçamento - 2024
    """)

col19, col20, col21, col22, col23, col24 = st.columns(6)
with col19:
    jan_24 = st.number_input('Jan-24')
with col20:
    fev_24 = st.number_input('Fev-24')
with col21:
    mar_24 = st.number_input('Mar-24')
with col22:
    abr_24 = st.number_input('Abr-24')
with col23:
    mai_24 = st.number_input('Mai-24')
with col24:
    jun_24 = st.number_input('Jun-24')
col25, col26, col27, col28, col29, col30  = st.columns(6)
with col25:
    jul_24 = st.number_input('Jul-24')
with col26:
    ago_24 = st.number_input('Ago-24')
with col27:
    set_24 = st.number_input('Set-24')
with col28:
    out_24 = st.number_input('Out-24')
with col29:
    nov_24 = st.number_input('Nov-24')
with col30:
    dez_24 = st.number_input('Dez-24')

total_orc_24 = jan_24+fev_24+mar_24+abr_24+mai_24+jun_24+jul_24+ago_24+set_24+out_24+nov_24+dez_24

st.markdown("""
    # Orçamento - 2025
    """)

col31, col32, col33, col34, col35, col36 = st.columns(6)
with col31:
    jan_25 = st.number_input('Jan-25')
with col32:
    fev_25 = st.number_input('Fev-25')
with col33:
    mar_25 = st.number_input('Mar-25')
with col34:
    abr_25 = st.number_input('Abr-25')
with col35:
    mai_25 = st.number_input('Mai-25')
with col36:
    jun_25 = st.number_input('Jun-25')
col37, col38, col39, col40, col41, col42  = st.columns(6)
with col37:
    jul_25 = st.number_input('Jul-25')
with col38:
    ago_25 = st.number_input('Ago-25')
with col39:
    set_25 = st.number_input('Set-25')
with col40:
    out_25 = st.number_input('Out-25')
with col41:
    nov_25 = st.number_input('Nov-25')
with col42:
    dez_25 = st.number_input('Dez-25')

total_orc_25 = jan_25+fev_25+mar_25+abr_25+mai_25+jun_25+jul_25+ago_25+set_25+out_25+nov_25+dez_25

st.markdown("""
    # Orçamento - 2026
    """)

col43, col44, col45, col46, col47, col48 = st.columns(6)
with col43:
    jan_26 = st.number_input('Jan-26')
with col44:
    fev_26 = st.number_input('Fev-26')
with col45:
    mar_26 = st.number_input('Mar-26')
with col46:
    abr_26 = st.number_input('Abr-26')
with col47:
    mai_26 = st.number_input('Mai-26')
with col48:
    jun_26 = st.number_input('Jun-26')
col49, col50, col51, col52, col53, col54  = st.columns(6)
with col49:
    jul_26 = st.number_input('Jul-26')
with col50:
    ago_26 = st.number_input('Ago-26')
with col51:
    set_26 = st.number_input('Set-26')
with col52:
    out_26 = st.number_input('Out-26')
with col53:
    nov_26 = st.number_input('Nov-26')
with col54:
    dez_26 = st.number_input('Dez-26')

total_orc_26 = jan_26+fev_26+mar_26+abr_26+mai_26+jun_26+jul_26+ago_26+set_26+out_26+nov_26+dez_26

st.markdown("""
    # Orçamento - 2027
    """)

col55, col56, col57, col58, col59, col60 = st.columns(6)
with col55:
    jan_27 = st.number_input('Jan-27')
with col56:
    fev_27 = st.number_input('Fev-27')
with col57:
    mar_27 = st.number_input('Mar-27')
with col58:
    abr_27 = st.number_input('Abr-27')
with col59:
    mai_27 = st.number_input('Mai-27')
with col60:
    jun_27 = st.number_input('Jun-27')
col61, col62, col63, col64, col65, col66  = st.columns(6)
with col61:
    jul_27 = st.number_input('Jul-27')
with col62:
    ago_27 = st.number_input('Ago-27')
with col63:
    set_27 = st.number_input('Set-27')
with col64:
    out_27 = st.number_input('Out-27')
with col65:
    nov_27 = st.number_input('Nov-27')
with col66:
    dez_27 = st.number_input('Dez-27')

total_orc_27 = jan_27+fev_27+mar_27+abr_27+mai_27+jun_27+jul_27+ago_27+set_27+out_27+nov_27+dez_27

valor = total_orc_23+total_orc_24+total_orc_25+total_orc_26+total_orc_27

df_orc = pd.DataFrame(columns=['Nome do Projeto', 'Total Orçamento-23', 'Total Orçamento-24', 'Total Orçamento-25', 'Total Orçamento-26', 'Total Orçamento-27'])
new_df_orc = {"Nome do Projeto": nome_projeto, "Total Orçamento-23": float(total_orc_23), "Total Orçamento-24": float(total_orc_24), "Total Orçamento-25": float(total_orc_25), "Total Orçamento-26": float(total_orc_26), "Total Orçamento-27": float(total_orc_27)}
df_orc = df_orc.append(new_df_orc, ignore_index=True)

#df_orc

st.markdown("""
    # :red[Custos (-)]
    """)

ct1, ct2, ct3, ct4, ct5 = st.columns(5)
with ct1:
    custo_23 = st.number_input('Custo Anual-23')
with ct2:
    custo_24 = st.number_input('Custo Anual-24')
with ct3:
    custo_25 = st.number_input('Custo Anual-25')
with ct4:
    custo_26 = st.number_input('Custo Anual-26')
with ct5:
    custo_27 = st.number_input('Custo Anual-27')

ct6, ct7, ct8, ct9, ct10 = st.columns(5)
with ct6:
    custo_28 = st.number_input('Custo Anual-28')
with ct7:
    custo_29 = st.number_input('Custo Anual-29')
with ct8:
    custo_30 = st.number_input('Custo Anual-30')
with ct9:
    custo_31 = st.number_input('Custo Anual-31')
with ct10:
    custo_32 = st.number_input('Custo Anual-32')

total_custo = custo_23+custo_24+custo_25+custo_26+custo_27+custo_28+custo_29+custo_30+custo_31+custo_32

df_custos = pd.DataFrame(columns=['Nome do Projeto', 'Custo Anual-23', 'Custo Anual-24', 'Custo Anual-25', 'Custo Anual-26', 'Custo Anual-27', 'Custo Anual-28', 'Custo Anual-29', 'Custo Anual-30', 'Custo Anual-31', 'Custo Anual-32'])
new_df_custos = {"Nome do Projeto": nome_projeto, "Custo Anual-23": float(custo_23), "Custo Anual-24": float(custo_24), "Custo Anual-25": float(custo_25), "Custo Anual-26": float(custo_26), "Custo Anual-27": float(custo_27), "Custo Anual-28": float(custo_28), "Custo Anual-29": float(custo_29), "Custo Anual-30": float(custo_30), "Custo Anual-31": float(custo_31), "Custo Anual-32": float(custo_32)}
df_custos = df_custos.append(new_df_custos, ignore_index=True)

#df_custos

st.markdown("""
    # :green[Ganhos (+)]
    """)

gn1, gn2, gn3, gn4, gn5 = st.columns(5)
with gn1:
    ganhos_23 = st.number_input('Ganhos Anual-23')
with gn2:
    ganhos_24 = st.number_input('Ganhos Anual-24')
with gn3:
    ganhos_25 = st.number_input('Ganhos Anual-25')
with gn4:
    ganhos_26 = st.number_input('Ganhos Anual-26')
with gn5:
    ganhos_27 = st.number_input('Ganhos Anual-27')


gn6, gn7, gn8, gn9, gn10 = st.columns(5)
with gn6:
    ganhos_28 = st.number_input('Ganhos Anual-28')
with gn7:
    ganhos_29 = st.number_input('Ganhos Anual-29')
with gn8:
    ganhos_30 = st.number_input('Ganhos Anual-30')
with gn9:
    ganhos_31 = st.number_input('Ganhos Anual-31')
with gn10:
    ganhos_32 = st.number_input('Ganhos Anual-32')


total_ganhos = ganhos_23+ganhos_24+ganhos_25+ganhos_26+ganhos_27+ganhos_28+ganhos_29+ganhos_30+ganhos_31+ganhos_32

df_ganhos = pd.DataFrame(columns=['Nome do Projeto', 'Ganhos Anual-23', 'Ganhos Anual-24', 'Ganhos Anual-25', 'Ganhos Anual-26', 'Ganhos Anual-27', 'Ganhos Anual-28', 'Ganhos Anual-29', 'Ganhos Anual-30', 'Ganhos Anual-31', 'Ganhos Anual-32'])
new_df_ganhos = {"Nome do Projeto": nome_projeto, "Ganhos Anual-23": float(ganhos_23), "Ganhos Anual-24": float(ganhos_24), "Ganhos Anual-25": float(ganhos_25), "Ganhos Anual-26": float(ganhos_26), "Ganhos Anual-27": float(ganhos_27), "Ganhos Anual-28": float(ganhos_28), "Ganhos Anual-29": float(ganhos_29), "Ganhos Anual-30": float(ganhos_30), "Ganhos Anual-31": float(ganhos_31), "Ganhos Anual-32": float(ganhos_32)}
df_ganhos = df_ganhos.append(new_df_ganhos, ignore_index=True)

#df_ganhos

st.markdown("""
    # :orange[Outros Itens FCL (+)]
    """)

ot1, ot2, ot3, ot4, ot5 = st.columns(5)
with ot1:
    outros_23 = st.number_input('Outros Itens FCL Anual-23')
with ot2:
    outros_24 = st.number_input('Outros Itens FCL Anual-24')
with ot3:
    outros_25 = st.number_input('Outros Itens FCL Anual-25')
with ot4:
    outros_26 = st.number_input('Outros Itens FCL Anual-26')
with ot5:
    outros_27 = st.number_input('Outros Itens FCL Anual-27')

ot6, ot7, ot8, ot9, ot10 = st.columns(5)
with ot6:
    outros_28 = st.number_input('Outros Itens FCL Anual-28')
with ot7:
    outros_29 = st.number_input('Outros Itens FCL Anual-29')
with ot8:
    outros_30 = st.number_input('Outros Itens FCL Anual-30')
with ot9:
    outros_31 = st.number_input('Outros Itens FCL Anual-31')
with ot10:
    outros_32 = st.number_input('Outros Itens FCL Anual-32')



total_outros_itens = outros_23+outros_24+outros_25+outros_26+outros_27+outros_28+outros_29+outros_30+outros_31+outros_32

df_outros_itens = pd.DataFrame(columns=['Nome do Projeto', 'Outros Itens FCL Anual-23', 'Outros Itens FCL Anual-24', 'Outros Itens FCL Anual-25', 'Outros Itens FCL Anual-26', 'Outros Itens FCL Anual-27', 'Outros Itens FCL Anual-28', 'Outros Itens FCL Anual-29', 'Outros Itens FCL Anual-30', 'Outros Itens FCL Anual-31', 'Outros Itens FCL Anual-32'])
new_df_outros_itens = {"Nome do Projeto": nome_projeto, "Outros Itens FCL Anual-23": float(outros_23), "Outros Itens FCL Anual-24": float(outros_24), "Outros Itens FCL Anual-25": float(outros_25), "Outros Itens FCL Anual-26": float(outros_26), "Outros Itens FCL Anual-27": float(outros_27), "Outros Itens FCL Anual-28": float(outros_28), "Outros Itens FCL Anual-29": float(outros_29), "Outros Itens FCL Anual-30": float(outros_30), "Outros Itens FCL Anual-31": float(outros_31), "Outros Itens FCL Anual-32": float(outros_32)}
df_outros_itens = df_outros_itens.append(new_df_outros_itens, ignore_index=True)

#df_outros_itens

def soma():
    s = valor * 0.093
    #st.metric(label='Total Recuperação PIS/Cofins (Anos)', value=s)
    imp = s / 48
    #st.metric(label='Total Recuperação PIS/Cofins (Mensal)', value=imp)
    data_rec_pis_cofins = pd.date_range(data_incial, periods=48, freq='M')
    data_rec_pis_cofins = data_rec_pis_cofins.to_frame(name='Periodo')
    data_rec_pis_cofins['Periodo'] = data_rec_pis_cofins['Periodo'].apply(lambda x: 'PISCOFINS - {}'.format(x.year))
    data_rec_pis_cofins['Valor Rec'] = imp
    data_rec_pis_cofins = data_rec_pis_cofins.groupby('Periodo')['Valor Rec'].sum().reset_index()
    #data_rec_pis_cofins
    df = pd.DataFrame(columns=['Nome do Projeto', 'Valor do Projeto', 'Início do Investimento', 'PISCOFINS - 2023', 'PISCOFINS - 2024', 'PISCOFINS - 2025', 'PISCOFINS - 2026', 'PISCOFINS - 2027'])
    new_data = {"Nome do Projeto": nome_projeto, "Valor do Projeto": float(valor), "Início do Investimento": data_incial}
    df = df.append(new_data, ignore_index=True)
    df = pd.melt(df.reset_index(), id_vars=['Nome do Projeto', 'Valor do Projeto', 'Início do Investimento'], var_name='Periodo', value_name='Valor')
    df = df[df.Periodo.str.contains("index") == False]
    df_imp = pd.merge(df, data_rec_pis_cofins, on= 'Periodo', how='outer')
    df_imp['Valor Rec'].fillna(0.0, inplace=True)

    data_aux_imp = pd.pivot_table(df_imp, values='Valor Rec', index=['Nome do Projeto', 'Valor do Projeto', 'Início do Investimento'], 
                                  columns=['Periodo'], aggfunc=np.sum, margins=False)
        
    data_aux_imp.reset_index()

    data_aux_imp.reset_index(inplace=True)

    #st.dataframe(data_aux_imp)
    

    vida_util_meses = vida_util * 12
    dt_depreciacao = pd.date_range(data_incial, periods=vida_util_meses, freq='M')
    
    df_dep = dt_depreciacao.to_frame(name='Periodo')
    
    df_dep['Periodo'] = df_dep['Periodo'].apply(lambda x: 'DEPRC - {}'.format(x.year))
    df_dep['Valor Depreciação'] = valor / vida_util_meses
    df_dep['Valor Depreciação'].sum()
    df_dep['Nome do Projeto'] = nome_projeto

    df_depreciacao_ano = df_dep.groupby(['Nome do Projeto', 'Periodo'])['Valor Depreciação'].sum().reset_index()
    df_depreciacao_ano = pd.pivot_table(df_depreciacao_ano, values='Valor Depreciação', index=['Nome do Projeto'], 
                                  columns=['Periodo'], aggfunc=np.sum, margins=False)
    #df_depreciacao_ano
    
    dt_depreciacao_n = pd.date_range(data_incial, periods=vida_util_meses, freq='M')
    
    df_dep_n = dt_depreciacao_n.to_frame(name='Periodo')
    
    df_dep_n['Periodo'] = df_dep_n['Periodo'].apply(lambda x: '(-) DEPRC - {}'.format(x.year))
    df_dep_n['Valor Depreciação'] = valor / vida_util_meses
    df_dep_n['Valor Depreciação'].sum()
    df_dep_n['Nome do Projeto'] = nome_projeto
    df_depreciacao_ano_n = df_dep_n.groupby(['Nome do Projeto', 'Periodo'])['Valor Depreciação'].sum().reset_index()
    df_depreciacao_ano_n['Valor Depreciação (-)'] = df_depreciacao_ano_n['Valor Depreciação'].apply(lambda x: x * -1)
    

    df_depreciacao_ano_negativo = df_depreciacao_ano_n[['Nome do Projeto', 'Periodo', 'Valor Depreciação (-)']]
    df_depreciacao_ano_negativo = pd.pivot_table(df_depreciacao_ano_negativo, values='Valor Depreciação (-)', index=['Nome do Projeto'], 
                                  columns=['Periodo'], aggfunc=np.sum, margins=False)
    #df_depreciacao_ano_negativo

    df_fim_aux = pd.merge(df_depreciacao_ano, df_depreciacao_ano_negativo, on='Nome do Projeto', how='outer')
    #df_fim_aux
    df_fim_aux_2 = pd.merge(data_aux_imp, df_fim_aux, on='Nome do Projeto', how='outer')
    #df_fim_aux_2
    df_fim_3 = pd.merge(df_fim_aux_2, df_orc, on='Nome do Projeto', how='outer')
    #df_fim_3

    df_fim_4 = pd.merge(df_fim_3, df_custos, on='Nome do Projeto', how='outer')
    #df_fim_4

    df_fim_5 = pd.merge(df_fim_4, df_ganhos, on='Nome do Projeto', how='outer')
    #df_fim_5

    df_fim_6 = pd.merge(df_fim_5, df_outros_itens, on='Nome do Projeto', how='outer')
    #df_fim_6

    df_fim_6 = pd.melt(df_fim_6.reset_index(), id_vars=['Nome do Projeto', 'Valor do Projeto', 'Início do Investimento'], var_name='Periodo', value_name='Valor')
    #df_fim_6
    # df_fim_6 = df_fim_6[df_fim_6.Periodo.str.contains("index") == False]
    # df_fim_6
    #df_fim_6.to_excel(r'C:\Users\lpalmeira\Videos\Streamlit\data\Analise_Aux.xlsx', index=False)
    # data_fim = pd.merge(data_aux_imp, df_fim_6, on='Periodo', how='outer')
    # data_fim = data_fim[['Nome do Projeto', 'Valor do Projeto', 'Início do Investimento', 'Periodo', 'Valor']]
    # data_fim
    # data_fim = pd.pivot_table(data_fim, values='Valor', index=['Nome do Projeto', 'Valor do Projeto', 'Início do Investimento'], 
    #                               columns=['Periodo'], aggfunc=np.sum, margins=False)
    # data_fim

    orc1, orc2 , orc3 = st.columns(3)
    with orc1:
        st.metric(label='Total Orçamento 2023',  value=total_orc_23)
    with orc2:
        st.metric(label='Total Orçamento 2024', value=total_orc_24)
    with orc3:
        st.metric(label='Total Orçamento 2025', value=total_orc_25)

    # car1, car2 = st.columns(2)
    # with car1:
    #     st.metric(label='Total Recuperação PIS/Cofins (Anos)', value=s)
    # with car2:
    #     st.metric(label='Total Recuperação PIS/Cofins (Mensal)', value=imp)
    

    x = pd.read_excel(r'C:\Users\lpalmeira\Videos\Streamlit\data\Analise_Teste.xlsx')
    #st.write(x)

    x = pd.melt(x.reset_index(), id_vars=['Nome do Projeto', 'Natureza', 'Diretoria', 'Site', 'Vida Util', 'Data Inicial', 'Data Final'], var_name='Periodo', value_name='Valor')
    #x

    y = pd.merge(x, df_fim_6, on='Periodo', how='outer')
    #y
    y['Valor_y'].fillna(0.0, inplace=True)
    y['Valor do Projeto'].fillna(valor, inplace=True)
    y['Diretoria'].fillna(diretoria, inplace=True)
    y['Site'].fillna(site, inplace=True)
    y['Vida Util'].fillna(vida_util, inplace=True)
    y['Data Inicial'].fillna(data_incial, inplace=True)
    y['Data Final'].fillna(data_final, inplace=True)
    y = y[['Nome do Projeto_x', 'Natureza', 'Diretoria', 'Site', 'Vida Util', 'Data Inicial', 'Data Final', 'Valor do Projeto', 'Periodo', 'Valor_y']]
    y = y[y.Periodo.str.contains("index") == False]
    #y

    # y['Valor_z'] = y['Valor_y'].apply(lambda x: str(x).replace(",",""))
    # y

    y = pd.pivot_table(y, values='Valor_y', index=['Nome do Projeto_x', 'Natureza', 'Diretoria', 'Site', 'Vida Util', 'Data Inicial', 'Data Final', 'Valor do Projeto'], 
                                   columns=['Periodo'], aggfunc=np.sum, margins=False).reset_index()
    #y
    # y = pd.merge(x, df_fim_6, on='Nome do Projeto')
    # st.write(y)
    y['EBTIDA - 2023'] = y['Custo Anual-23'] + y['Ganhos Anual-23'] + y['PISCOFINS - 2023']
    y['EBTIDA - 2024'] = y['Custo Anual-24'] + y['Ganhos Anual-24'] + y['PISCOFINS - 2024']
    y['EBTIDA - 2025'] = y['Custo Anual-25'] + y['Ganhos Anual-25'] + y['PISCOFINS - 2025']
    y['EBTIDA - 2026'] = y['Custo Anual-26'] + y['Ganhos Anual-26'] + y['PISCOFINS - 2026']
    y['EBTIDA - 2027'] = y['Custo Anual-27'] + y['Ganhos Anual-27'] + y['PISCOFINS - 2027']
    y['EBTIDA - 2028'] = y['Custo Anual-28'] + y['Ganhos Anual-28'] + y['PISCOFINS - 2028']
    y['EBTIDA - 2029'] = y['Custo Anual-29'] + y['Ganhos Anual-29'] + y['PISCOFINS - 2029']
    y['EBTIDA - 2030'] = y['Custo Anual-30'] + y['Ganhos Anual-30'] + y['PISCOFINS - 2030']
    y['EBTIDA - 2031'] = y['Custo Anual-31'] + y['Ganhos Anual-31'] + y['PISCOFINS - 2031']
    y['EBTIDA - 2032'] = y['Custo Anual-32'] + y['Ganhos Anual-32'] + y['PISCOFINS - 2032']

    y['LUCRO BRUTO - 2023'] = y['EBTIDA - 2023'] + y['(-) DEPRC - 2023']
    y['LUCRO BRUTO - 2024'] = y['EBTIDA - 2024'] + y['(-) DEPRC - 2024']
    y['LUCRO BRUTO - 2025'] = y['EBTIDA - 2025'] + y['(-) DEPRC - 2025']
    y['LUCRO BRUTO - 2026'] = y['EBTIDA - 2026'] + y['(-) DEPRC - 2026']
    y['LUCRO BRUTO - 2027'] = y['EBTIDA - 2027'] + y['(-) DEPRC - 2027']
    y['LUCRO BRUTO - 2028'] = y['EBTIDA - 2028'] + y['(-) DEPRC - 2028']
    y['LUCRO BRUTO - 2029'] = y['EBTIDA - 2029'] + y['(-) DEPRC - 2028']
    y['LUCRO BRUTO - 2030'] = y['EBTIDA - 2030'] + y['(-) DEPRC - 2030']
    y['LUCRO BRUTO - 2031'] = y['EBTIDA - 2031'] + y['(-) DEPRC - 2031']
    y['LUCRO BRUTO - 2032'] = y['EBTIDA - 2032'] + y['(-) DEPRC - 2032']

    y['IR - 2023'] = ((y['LUCRO BRUTO - 2023'] * 0.25) + (y['LUCRO BRUTO - 2023'] * 0.09)) * -1
    y['IR - 2024'] = ((y['LUCRO BRUTO - 2024'] * 0.25) + (y['LUCRO BRUTO - 2024'] * 0.09)) * -1
    y['IR - 2025'] = ((y['LUCRO BRUTO - 2025'] * 0.25) + (y['LUCRO BRUTO - 2025'] * 0.09)) * -1
    y['IR - 2026'] = ((y['LUCRO BRUTO - 2026'] * 0.25) + (y['LUCRO BRUTO - 2026'] * 0.09)) * -1
    y['IR - 2027'] = ((y['LUCRO BRUTO - 2027'] * 0.25) + (y['LUCRO BRUTO - 2027'] * 0.09)) * -1
    y['IR - 2028'] = ((y['LUCRO BRUTO - 2028'] * 0.25) + (y['LUCRO BRUTO - 2028'] * 0.09)) * -1
    y['IR - 2029'] = ((y['LUCRO BRUTO - 2029'] * 0.25) + (y['LUCRO BRUTO - 2029'] * 0.09)) * -1
    y['IR - 2030'] = ((y['LUCRO BRUTO - 2030'] * 0.25) + (y['LUCRO BRUTO - 2030'] * 0.09)) * -1
    y['IR - 2031'] = ((y['LUCRO BRUTO - 2031'] * 0.25) + (y['LUCRO BRUTO - 2031'] * 0.09)) * -1
    y['IR - 2032'] = ((y['LUCRO BRUTO - 2032'] * 0.25) + (y['LUCRO BRUTO - 2032'] * 0.09)) * -1
    
    y['LUCRO LIQUIDO - 2023'] = y['LUCRO BRUTO - 2023'] + y['IR - 2023']
    y['LUCRO LIQUIDO - 2024'] = y['LUCRO BRUTO - 2024'] + y['IR - 2024']
    y['LUCRO LIQUIDO - 2025'] = y['LUCRO BRUTO - 2025'] + y['IR - 2025']
    y['LUCRO LIQUIDO - 2026'] = y['LUCRO BRUTO - 2026'] + y['IR - 2026']
    y['LUCRO LIQUIDO - 2027'] = y['LUCRO BRUTO - 2027'] + y['IR - 2027']
    y['LUCRO LIQUIDO - 2028'] = y['LUCRO BRUTO - 2028'] + y['IR - 2028']
    y['LUCRO LIQUIDO - 2029'] = y['LUCRO BRUTO - 2029'] + y['IR - 2029']
    y['LUCRO LIQUIDO - 2030'] = y['LUCRO BRUTO - 2030'] + y['IR - 2030']
    y['LUCRO LIQUIDO - 2031'] = y['LUCRO BRUTO - 2031'] + y['IR - 2031']
    y['LUCRO LIQUIDO - 2032'] = y['LUCRO BRUTO - 2032'] + y['IR - 2032']

    y['FCL - 2023'] = y['DEPRC - 2023'] + y['LUCRO LIQUIDO - 2023'] - y['Total Orçamento-23']
    y['FCL - 2024'] = y['DEPRC - 2024'] + y['LUCRO LIQUIDO - 2024'] - y['Total Orçamento-24']
    y['FCL - 2025'] = y['DEPRC - 2025'] + y['LUCRO LIQUIDO - 2025'] - y['Total Orçamento-25']
    y['FCL - 2026'] = y['DEPRC - 2026'] + y['LUCRO LIQUIDO - 2026'] - y['Total Orçamento-26']
    y['FCL - 2027'] = y['DEPRC - 2027'] + y['LUCRO LIQUIDO - 2027'] - y['Total Orçamento-27']
    y['FCL - 2028'] = y['DEPRC - 2028'] + y['LUCRO LIQUIDO - 2028'] - y['Total Orçamento-28']
    y['FCL - 2029'] = y['DEPRC - 2029'] + y['LUCRO LIQUIDO - 2029'] - y['Total Orçamento-29']
    y['FCL - 2030'] = y['DEPRC - 2030'] + y['LUCRO LIQUIDO - 2030'] - y['Total Orçamento-30']
    y['FCL - 2031'] = y['DEPRC - 2031'] + y['LUCRO LIQUIDO - 2031'] - y['Total Orçamento-31']
    y['FCL - 2032'] = y['DEPRC - 2032'] + y['LUCRO LIQUIDO - 2032'] - y['Total Orçamento-32']
    
    #y.columns
    y.to_excel(r'C:\Users\lpalmeira\Videos\Streamlit\data\Analise_Teste_Saida.xlsx', index=False)
    grafico_orc = y[['Nome do Projeto_x', 'Total Orçamento-23', 'Total Orçamento-24', 'Total Orçamento-25', 'Total Orçamento-26', 'Total Orçamento-27']]
    grafico_orc_2 = pd.melt(grafico_orc.reset_index(), id_vars=['Nome do Projeto_x'], var_name='Periodo', value_name='Orçamento')
    grafico_orc_2 = grafico_orc_2[grafico_orc_2.Periodo.str.contains("index") == False]
    #grafico_orc_2 = grafico_orc_2[['Orçamento']]
    #grafico_orc_2


    grafico_custo = y[['Nome do Projeto_x', 'Custo Anual-23', 'Custo Anual-24', 'Custo Anual-25', 'Custo Anual-26', 'Custo Anual-27', 'Custo Anual-28', 'Custo Anual-29', 'Custo Anual-30', 'Custo Anual-31', 'Custo Anual-32']]
    grafico_custo_2 = pd.melt(grafico_custo.reset_index(), id_vars=['Nome do Projeto_x'], var_name='Periodo', value_name='Custos')
    grafico_custo_2 = grafico_custo_2[grafico_custo_2.Periodo.str.contains("index") == False]
    #grafico_custo_2 = grafico_custo_2[['Custos']]
    #grafico_custo_2

    grafico_ganhos = y[['Nome do Projeto_x', 'Ganhos Anual-23', 'Ganhos Anual-24', 'Ganhos Anual-25', 'Ganhos Anual-26', 'Ganhos Anual-27', 'Ganhos Anual-28', 'Ganhos Anual-29', 'Ganhos Anual-30', 'Ganhos Anual-31', 'Ganhos Anual-32']]
    grafico_ganhos_2 = pd.melt(grafico_ganhos.reset_index(), id_vars=['Nome do Projeto_x'], var_name='Periodo', value_name='Ganhos')
    grafico_ganhos_2 = grafico_ganhos_2[grafico_ganhos_2.Periodo.str.contains("index") == False]
    #grafico_ganhos_2 = grafico_ganhos_2[['Ganhos']]
    #grafico_ganhos_2

    grafico_aux = grafico_ganhos_2.merge(grafico_custo_2, how='left')
    grafico_aux2 = grafico_aux.merge(grafico_orc_2, how='outer')

    grafico_aux2['Ganhos'].fillna(0.0, inplace=True)
    grafico_aux2['Custos'].fillna(0.0, inplace=True)
    grafico_aux2['Orçamento'].fillna(0.0, inplace=True)
    #grafico_aux2
    grafico_fim = grafico_aux2[['Custos', 'Ganhos']]
    #grafico_fim
    st.line_chart(grafico_fim)

    df_cx = y[['Nome do Projeto_x', 'FCL - 2023', 'FCL - 2024', 'FCL - 2025', 'FCL - 2026', 'FCL - 2027', 'FCL - 2028', 'FCL - 2029', 'FCL - 2030', 'FCL - 2031', 'FCL - 2032']]
    df_cx = pd.melt(df_cx.reset_index(), id_vars=['Nome do Projeto_x'], var_name='Caixa', value_name='Valor')
    df_cx = df_cx[df_cx.Caixa.str.contains("index") == False]
    df_cx = df_cx.groupby(by=['Caixa']).sum()
    #df_cx


    x = np.array(df_cx['Valor'][1:])
    x = np.insert(x,0,0.0,axis=0)

    #x

    cxd = []

    for i, v in enumerate(x):
        cxd.append(v/((1+0.07)**(i+1)))

    #cxd

    vpl = npf.npv(0.07, cxd)
    vpl = vpl.round(2)
    
    mtir = npf.mirr(values=np.array(df_cx['Valor']), finance_rate=0.07, reinvest_rate=0.07)
    mtir = (mtir*100).round(2)


    # def payback_of_investment(investment, cashflows):
                
    #     total, years, cumulative = 0.0, 0, []
        
    #     for cashflow in cashflows:
    #         total += cashflow
    #         if total < investment:
    #             years += 1
    #         cumulative.append(total)
    #         A = years
    #         B = investment - cumulative[years-1]
    #         C = cumulative[years] - cumulative[years-1]
    #         return A + (B/C)

    # def payback(cashflows):
                
    #         investment, cashflows = cashflows[0], cashflows[1:]
    #         if investment < 0 : investment = -investment
    #         return payback_of_investment(investment, cashflows)

    # pay_back = payback(np.array(df_cx['Valor'])).round(1)
    # pay_back


    card1, card2 = st.columns(2)
    with card1:
        st.metric(label='Total VPL', value=vpl)
    with card2:    
        st.metric(label='Total TIR', value=mtir)


st.button('Calcular', on_click=soma)
