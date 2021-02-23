from __future__ import print_function
import pandas as pd
import numpy as np
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

import sys
sys.path.append('../')

pd.options.display.float_format = '{:,.2f}'.format

def pivot_data(df, df_type):
    # df_type possible values: 
    # 0 - salary on date
    # 1 - worker status on date
    # 2 - jobs on date        
    st0, st1, st2, st3, st4, st5 = 0, 0, 0, 0, 0, 0
    if df_type == 0:
        st0 = df.columns[0]
        st1 = df.columns[1]
        st2 = df.columns[2]
    if df_type == 1:
        st0 = df.columns[0]
        st1 = df.columns[1]
        st2 = df.columns[2]
        st3 = df.columns[5]
        st4 = df.columns[7]
    if df_type == 2:
        st0 = df.columns[0]
        st1 = df.columns[1]
        st2 = df.columns[2]
        st3 = df.columns[3]
        st4 = df.columns[35]
        st5 = df.columns[43]        
    index_dict = {0 : [st0, st1],
                  1 : [st0, st1, st2, st4],
                  2 : [st0, st1, st2, st3, st4]}
    values_dict = {0 : [st2],
                   1 : [st3],
                   2 : [st5]}
    df_pivot = pd.pivot_table(df, index = index_dict[df_type], values = values_dict[df_type], fill_value=0)
    return df_pivot

def build_template(df_salary, df_status, worker, df_jobs, filename):
    t_df_salary = pivot_data(df_salary, 0)
    t_df_salary['Salario Total'] = t_df_salary['Salario Total'].map('${:,.2f}'.format)
    
    t_df_status = pivot_data(df_status, 1)
    t_df_status['Salario'] = t_df_status['Salario'].map('${:,.2f}'.format)

    df_jobs_html = []
    for df in df_jobs:
        t_df = pivot_data(df,2)
        t_df['Importe por Programa'] = t_df['Importe por Programa'].map('${:,.2f}'.format)        
        df_jobs_html.append(t_df.to_html())

    env = Environment(loader=FileSystemLoader('template'))
    template = env.get_template("report_structure.html")
    template_vars = {"title" : "Reporte de Salarios Mensuales",
                     "total_salary" : t_df_salary.to_html(),
                     "year" : df_status.iloc[0]["Año"],
                     "month" : df_status.iloc[0]["Mes"],
                     "worker_status" : t_df_status.to_html(),
                     "jobs_done" : df_jobs_html,
                     "worker" : worker}
    jinja2_html_out = template.render(template_vars)
    HTML(string=jinja2_html_out).write_pdf('report/%s.pdf'%filename,stylesheets=["template/style.css"])
    