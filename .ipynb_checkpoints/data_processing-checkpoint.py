import pandas as pd
import numpy as np
import os
import xlrd

# global switcher
switcher_months ={  1 : '1 - enero',
                    2 : '2 - febrero',
                    3 : '3 - marzo',
                    4 : '4 - abril',
                    5 : '5 - mayo',
                    6 : '6 - junio',
                    7 : '7 - julio',
                    8 : '8 - agosto',
                    9 : '9 - septiembre',
                    10: '10 - octubre',
                    11: '11 - noviembre',
                    12: '12 - diciembre',
                    'Enero' : 1,
                    'Febrero' : 2,
                    'Marzo' : 3,
                    'Abril' : 4,
                    'Mayo' : 5,
                    'Junio' : 6,
                    'Julio' : 7,
                    'Agosto' : 8,
                    'Septiembre' : 9,
                    'Octubre' : 10,
                    'Noviembre' : 11,
                    'Diciembre' : 12}

# global data frame files dictionary
january_month_files = []
february_month_files = []
march_month_files = []
april_month_files = []
may_month_files = []
june_month_files = []
july_month_files = []
august_month_files = []
september_month_files = []
october_month_files = []
november_month_files = []
december_month_files = []
record_dict = { '1 - enero': january_month_files,
                '2 - febrero': february_month_files,
                '3 - marzo': march_month_files,
                '4 - abril': april_month_files,
                '5 - mayo': may_month_files,
                '6 - junio': june_month_files,
                '7 - julio': july_month_files,
                '8 - agosto': august_month_files,
                '9 - septiembre': september_month_files,
                '10 - octubre': october_month_files,
                '11 - noviembre': november_month_files,
                '12 - diciembre': december_month_files}

# global valid workers status dictionary
worker_name_column = []
id_value_column = []
position_name_column = []
evaluation_value_column = []
salary_scale_number_column = []
salary_number_colunmn = []
area_name_column = []
human_value_column = []
year_number_column = []
month_number_column = []
worked = []
status = {  'Nombre del Trabajador': worker_name_column,
            'C.I': id_value_column,
            'Nombre del Cargo': position_name_column,
            'Nivel de Evaluación': evaluation_value_column,
            'Salario Escala': salary_scale_number_column,
            'Salario': salary_number_colunmn,
            'ÁREA': area_name_column,
            'R.H': human_value_column,
            'Año': year_number_column,
            'Mes': month_number_column,
            'Trabajado': worked}

# global non valid workers status dictionary 
non_worker_name_column = []
non_id_value_column = []
non_position_name_column = []
non_evaluation_value_column = []
non_salary_scale_number_column = []
non_salary_number_colunmn = []
non_area_name_column = []
non_human_value_column = []
non_year_number_column = []
non_month_number_column = []
non_worked = []
non_status = {  'Nombre del Trabajador': non_worker_name_column,
                'C.I': non_id_value_column,
                'Nombre del Cargo': non_position_name_column,
                'Nivel de Evaluación': non_evaluation_value_column,
                'Salario Escala': non_salary_scale_number_column,
                'Salario': non_salary_number_colunmn,
                'ÁREA': non_area_name_column,
                'R.H': non_human_value_column,
                'Año': non_year_number_column,
                'Mes': non_month_number_column,
                'Trabajado': non_worked}

# list all .xlsx file with the model
def traverse_dir():
    for root, dirs, files in os.walk(os.path.dirname(__file__)):                
        if os.path.basename(root) in record_dict.keys():
            for f in files:                
                if f.lower().endswith('.xlsx'):
                    try:                        
                        f_path = os.path.join(os.path.realpath(root),f)
                        df = pd.read_excel(f_path, sheet_name='Trabajo')
                        record_dict.get(os.path.basename(root)).append(df)
                    except (FileNotFoundError, ValueError, xlrd.biffh.XLRDError):
                        pass

# get month per number
def search_per_month_folder(month_number):
    return record_dict.get(switcher_months.get(month_number), "Error")

# store all workers data
def worker_status(df):
    # valid data
    vdata = True
    # Worker
    #word_worker = df.iloc[:,0][2]
    worker_name = df.iloc[:,2][2]
    # Worker ID
    #word_id = df.iloc[:,13][2]
    id_value = df.iloc[:,15][2]
    # Position
    #word_position = df.iloc[:,0][3]
    position_name = df.iloc[:,1][3]
    # Evaluation
    #word_evaluation = df.iloc[:,22][3]
    evaluation_value = df.iloc[:,28][3]    
    # Scale
    #word_salary_scale = df.iloc[:,36][3]
    salary_scale_number = df.iloc[:,38][3]
    # Area 
    #word_area = df.iloc[:,28][2]
    area_name = df.iloc[:,30][2]
    # Human Resources
    #word_human = df.iloc[:,40][2]
    human_value = df.iloc[:,41][2]
    # Year
    #word_year = df.iloc[:,38][1]
    year_number = df.iloc[:,39][1] 
    # Month
    #word_month = df.iloc[:,38][0]
    month_name = df.iloc[:,39][0] 
    month_dict = {'enero': 1,
                  'febrero': 2,
                  'marzo': 3,
                  'abril': 4,
                  'mayo': 5,
                  'junio': 6,
                  'julio': 7,
                  'agosto': 8,
                  'septiembre': 9,
                  'octubre': 10,
                  'noviembre': 11,
                  'diciembre':12}
    month_number = month_dict.get(str(month_name).lower())       
    
    if worker_name == np.nan:
        worker_name = "Error"
        vdata = False

    if id_value == np.nan:
        id_value = "Error"
        vdata = False

    if position_name == np.nan:
        position_name = "Sin cargo"
    
    if evaluation_value == np.nan:
        evaluation_value = "Sin evaluación"

    if salary_scale_number == np.nan:
        salary_scale_number = "Sin escala"
    
    if area_name == np.nan:
        area_name = "Sin Área"

    if human_value == np.nan:
        human_value = "Error"
        vdata = False

    if year_number == np.nan:
        year_number = "Error"
        vdata = False

    if month_number == np.nan:
        month_number = "Error"
        vdata = False

    if vdata:
        worker_name_column.append(worker_name)
        id_value_column.append(id_value)
        position_name_column.append(position_name)
        evaluation_value_column.append(evaluation_value)
        salary_scale_number_column.append(salary_scale_number)
        area_name_column.append(area_name)
        human_value_column.append(human_value)
        year_number_column.append(year_number)
        month_number_column.append(month_number)
    else:
        non_worker_name_column.append(worker_name)
        non_id_value_column.append(id_value)
        non_position_name_column.append(position_name)
        non_evaluation_value_column.append(evaluation_value)
        non_salary_scale_number_column.append(salary_scale_number)
        non_area_name_column.append(area_name)
        non_human_value_column.append(human_value)
        non_year_number_column.append(year_number)
        non_month_number_column.append(month_number)
    return vdata

# change all NaN for 0
def fill_NaN_where_numbers(df):
    df['Unnamed: 2'] = df['Unnamed: 2'].fillna(0)           # Air time
    df['Unnamed: 3'] = df['Unnamed: 3'].fillna(0)           # Realization Time
    df['Unnamed: 4'] = df['Unnamed: 4'].fillna(0)           # Day 1
    df['Unnamed: 5'] = df['Unnamed: 5'].fillna(0)
    df['Unnamed: 6'] = df['Unnamed: 6'].fillna(0)
    df['Unnamed: 7'] = df['Unnamed: 7'].fillna(0)
    df['Unnamed: 8'] = df['Unnamed: 8'].fillna(0)
    df['Unnamed: 9'] = df['Unnamed: 9'].fillna(0)
    df['Unnamed: 10'] = df['Unnamed: 10'].fillna(0)
    df['Unnamed: 11'] = df['Unnamed: 11'].fillna(0)
    df['Unnamed: 12'] = df['Unnamed: 12'].fillna(0)
    df['Unnamed: 13'] = df['Unnamed: 13'].fillna(0)
    df['Unnamed: 14'] = df['Unnamed: 14'].fillna(0)
    df['Unnamed: 15'] = df['Unnamed: 15'].fillna(0)
    df['Unnamed: 16'] = df['Unnamed: 16'].fillna(0)
    df['Unnamed: 17'] = df['Unnamed: 17'].fillna(0)
    df['Unnamed: 18'] = df['Unnamed: 18'].fillna(0)
    df['Unnamed: 19'] = df['Unnamed: 19'].fillna(0)
    df['Unnamed: 20'] = df['Unnamed: 20'].fillna(0)
    df['Unnamed: 21'] = df['Unnamed: 21'].fillna(0)
    df['Unnamed: 22'] = df['Unnamed: 22'].fillna(0)
    df['Unnamed: 23'] = df['Unnamed: 23'].fillna(0)
    df['Unnamed: 24'] = df['Unnamed: 24'].fillna(0)
    df['Unnamed: 25'] = df['Unnamed: 25'].fillna(0)
    df['Unnamed: 26'] = df['Unnamed: 26'].fillna(0)
    df['Unnamed: 27'] = df['Unnamed: 27'].fillna(0)
    df['Unnamed: 28'] = df['Unnamed: 28'].fillna(0)
    df['Unnamed: 29'] = df['Unnamed: 29'].fillna(0)
    df['Unnamed: 30'] = df['Unnamed: 30'].fillna(0)
    df['Unnamed: 31'] = df['Unnamed: 31'].fillna(0)
    df['Unnamed: 32'] = df['Unnamed: 32'].fillna(0)
    df['Unnamed: 33'] = df['Unnamed: 33'].fillna(0)
    df['Unnamed: 34'] = df['Unnamed: 34'].fillna(0)         # Day 31
    df['Unnamed: 36'] = df['Unnamed: 36'].fillna(0)         # Salary per Program
    df['Unnamed: 38'] = df['Unnamed: 38'].fillna(0)         # Remote
    df['Unnamed: 39'] = df['Unnamed: 39'].fillna(0)         # Interrupt
    df['Unnamed: 40'] = df['Unnamed: 40'].fillna(0)         # Multiple
    df['Unnamed: 41'] = df['Unnamed: 41'].fillna(0)         # Night
    df['Unnamed: 42'] = df['Unnamed: 42'].fillna(0)         # Discount

# make all the calculations and fill the daily labor data
def jobs_done(df):
    fill_NaN_where_numbers(df)

    # Program
    word_program = df.iloc[:,0][5]
    program_values = [  df.iloc[:,0][9],
                        df.iloc[:,0][10],
                        df.iloc[:,0][11],
                        df.iloc[:,0][12],
                        df.iloc[:,0][13],
                        df.iloc[:,0][14],
                        df.iloc[:,0][15],
                        df.iloc[:,0][16],
                        df.iloc[:,0][17],
                        df.iloc[:,0][18]]
    # Complexity
    word_complexity = df.iloc[:,1][5]
    complexity_values = [   df.iloc[:,1][9],
                            df.iloc[:,1][10],
                            df.iloc[:,1][11],
                            df.iloc[:,1][12],
                            df.iloc[:,1][13],
                            df.iloc[:,1][14],
                            df.iloc[:,1][15],
                            df.iloc[:,1][16],
                            df.iloc[:,1][17],
                            df.iloc[:,1][18]]
    # Air Time in mins
    word_air = df.iloc[:,2][5]
    air_values = [  df.iloc[:,2][9],
                    df.iloc[:,2][10],
                    df.iloc[:,2][11],
                    df.iloc[:,2][12],
                    df.iloc[:,2][13],
                    df.iloc[:,2][14],
                    df.iloc[:,2][15],
                    df.iloc[:,2][16],
                    df.iloc[:,2][17],
                    df.iloc[:,2][18]]
    # Realization Time in hours
    word_realization = df.iloc[:,3][5]
    realization_values = [  df.iloc[:,3][9],
                            df.iloc[:,3][10],
                            df.iloc[:,3][11],
                            df.iloc[:,3][12],
                            df.iloc[:,3][13],
                            df.iloc[:,3][14],
                            df.iloc[:,3][15],
                            df.iloc[:,3][16],
                            df.iloc[:,3][17],
                            df.iloc[:,3][18]]
    # Worked Days
    word_days = df.iloc[:,4][6]
    # Day 1
    word_day1 = df.iloc[:,4][8]
    # Emisions
    day1_values = [ df.iloc[:,4][9],
                    df.iloc[:,4][10],
                    df.iloc[:,4][11],
                    df.iloc[:,4][12],
                    df.iloc[:,4][13],
                    df.iloc[:,4][14],
                    df.iloc[:,4][15],
                    df.iloc[:,4][16],
                    df.iloc[:,4][17],
                    df.iloc[:,4][18]]
    # Day 2
    word_day2 = df.iloc[:,5][8]
    # Emisions
    day2_values = [ df.iloc[:,5][9],
                    df.iloc[:,5][10],
                    df.iloc[:,5][11],
                    df.iloc[:,5][12],
                    df.iloc[:,5][13],
                    df.iloc[:,5][14],
                    df.iloc[:,5][15],
                    df.iloc[:,5][16],
                    df.iloc[:,5][17],
                    df.iloc[:,5][18]]
    # Day 3
    word_day3 = df.iloc[:,6][8]
    # Emisions
    day3_values = [ df.iloc[:,6][9],
                    df.iloc[:,6][10],
                    df.iloc[:,6][11],
                    df.iloc[:,6][12],
                    df.iloc[:,6][13],
                    df.iloc[:,6][14],
                    df.iloc[:,6][15],
                    df.iloc[:,6][16],
                    df.iloc[:,6][17],
                    df.iloc[:,6][18]]
    # Day 4
    word_day4 = df.iloc[:,7][8]
    # Emisions
    day4_values = [ df.iloc[:,7][9],
                    df.iloc[:,7][10],
                    df.iloc[:,7][11],
                    df.iloc[:,7][12],
                    df.iloc[:,7][13],
                    df.iloc[:,7][14],
                    df.iloc[:,7][15],
                    df.iloc[:,7][16],
                    df.iloc[:,7][17],
                    df.iloc[:,7][18]]
    # Day 5
    word_day5 = df.iloc[:,8][8]
    # Emisions
    day5_values = [ df.iloc[:,8][9],
                    df.iloc[:,8][10],
                    df.iloc[:,8][11],
                    df.iloc[:,8][12],
                    df.iloc[:,8][13],
                    df.iloc[:,8][14],
                    df.iloc[:,8][15],
                    df.iloc[:,8][16],
                    df.iloc[:,8][17],
                    df.iloc[:,8][18]]
    # Day 6
    word_day6 = df.iloc[:,9][8]
    # Emisions
    day6_values = [ df.iloc[:,9][9],
                    df.iloc[:,9][10],
                    df.iloc[:,9][11],
                    df.iloc[:,9][12],
                    df.iloc[:,9][13],
                    df.iloc[:,9][14],
                    df.iloc[:,9][15],
                    df.iloc[:,9][16],
                    df.iloc[:,9][17],
                    df.iloc[:,9][18]]
    # Day 7
    word_day7 = df.iloc[:,10][8]
    # Emisions
    day7_values = [ df.iloc[:,10][9],
                    df.iloc[:,10][10],
                    df.iloc[:,10][11],
                    df.iloc[:,10][12],
                    df.iloc[:,10][13],
                    df.iloc[:,10][14],
                    df.iloc[:,10][15],
                    df.iloc[:,10][16],
                    df.iloc[:,10][17],
                    df.iloc[:,10][18]]
    # Day 8
    word_day8 = df.iloc[:,11][8]
    # Emisions
    day8_values = [ df.iloc[:,11][9],
                    df.iloc[:,11][10],
                    df.iloc[:,11][11],
                    df.iloc[:,11][12],
                    df.iloc[:,11][13],
                    df.iloc[:,11][14],
                    df.iloc[:,11][15],
                    df.iloc[:,11][16],
                    df.iloc[:,11][17],
                    df.iloc[:,11][18]]
    # Day 7
    word_day7 = df.iloc[:,10][8]
    # Emisions
    day7_values = [ df.iloc[:,10][9],
                    df.iloc[:,10][10],
                    df.iloc[:,10][11],
                    df.iloc[:,10][12],
                    df.iloc[:,10][13],
                    df.iloc[:,10][14],
                    df.iloc[:,10][15],
                    df.iloc[:,10][16],
                    df.iloc[:,10][17],
                    df.iloc[:,10][18]]
    # Day 8
    word_day8 = df.iloc[:,11][8]
    # Emisions
    day8_values = [ df.iloc[:,11][9],
                    df.iloc[:,11][10],
                    df.iloc[:,11][11],
                    df.iloc[:,11][12],
                    df.iloc[:,11][13],
                    df.iloc[:,11][14],
                    df.iloc[:,11][15],
                    df.iloc[:,11][16],
                    df.iloc[:,11][17],
                    df.iloc[:,11][18]]
    # Day 9
    word_day9 = df.iloc[:,12][8]
    # Emisions
    day9_values = [ df.iloc[:,12][9],
                    df.iloc[:,12][10],
                    df.iloc[:,12][11],
                    df.iloc[:,12][12],
                    df.iloc[:,12][13],
                    df.iloc[:,12][14],
                    df.iloc[:,12][15],
                    df.iloc[:,12][16],
                    df.iloc[:,12][17],
                    df.iloc[:,12][18]]
    # Day 10
    word_day10 = df.iloc[:,13][8]
    # Emisions
    day10_values = [ df.iloc[:,13][9],
                    df.iloc[:,13][10],
                    df.iloc[:,13][11],
                    df.iloc[:,13][12],
                    df.iloc[:,13][13],
                    df.iloc[:,13][14],
                    df.iloc[:,13][15],
                    df.iloc[:,13][16],
                    df.iloc[:,13][17],
                    df.iloc[:,13][18]]
    # Day 11
    word_day11 = df.iloc[:,14][8]
    # Emisions
    day11_values = [ df.iloc[:,14][9],
                    df.iloc[:,14][10],
                    df.iloc[:,14][11],
                    df.iloc[:,14][12],
                    df.iloc[:,14][13],
                    df.iloc[:,14][14],
                    df.iloc[:,14][15],
                    df.iloc[:,14][16],
                    df.iloc[:,14][17],
                    df.iloc[:,14][18]]
    # Day 12
    word_day12 = df.iloc[:,15][8]
    # Emisions
    day12_values = [ df.iloc[:,15][9],
                    df.iloc[:,15][10],
                    df.iloc[:,15][11],
                    df.iloc[:,15][12],
                    df.iloc[:,15][13],
                    df.iloc[:,15][14],
                    df.iloc[:,15][15],
                    df.iloc[:,15][16],
                    df.iloc[:,15][17],
                    df.iloc[:,15][18]]
    # Day 13
    word_day13 = df.iloc[:,16][8]
    # Emisions
    day13_values = [ df.iloc[:,16][9],
                    df.iloc[:,16][10],
                    df.iloc[:,16][11],
                    df.iloc[:,16][12],
                    df.iloc[:,16][13],
                    df.iloc[:,16][14],
                    df.iloc[:,16][15],
                    df.iloc[:,16][16],
                    df.iloc[:,16][17],
                    df.iloc[:,16][18]]
    # Day 14
    word_day14 = df.iloc[:,17][8]
    # Emisions
    day14_values = [ df.iloc[:,17][9],
                    df.iloc[:,17][10],
                    df.iloc[:,17][11],
                    df.iloc[:,17][12],
                    df.iloc[:,17][13],
                    df.iloc[:,17][14],
                    df.iloc[:,17][15],
                    df.iloc[:,17][16],
                    df.iloc[:,17][17],
                    df.iloc[:,17][18]]
    # Day 15
    word_day15 = df.iloc[:,18][8]
    # Emisions
    day15_values = [ df.iloc[:,18][9],
                    df.iloc[:,18][10],
                    df.iloc[:,18][11],
                    df.iloc[:,18][12],
                    df.iloc[:,18][13],
                    df.iloc[:,18][14],
                    df.iloc[:,18][15],
                    df.iloc[:,18][16],
                    df.iloc[:,18][17],
                    df.iloc[:,18][18]]
    # Day 16
    word_day16 = df.iloc[:,19][8]
    # Emisions
    day16_values = [ df.iloc[:,19][9],
                    df.iloc[:,19][10],
                    df.iloc[:,19][11],
                    df.iloc[:,19][12],
                    df.iloc[:,19][13],
                    df.iloc[:,19][14],
                    df.iloc[:,19][15],
                    df.iloc[:,19][16],
                    df.iloc[:,19][17],
                    df.iloc[:,19][18]]
    # Day 17
    word_day17 = df.iloc[:,20][8]
    # Emisions
    day17_values = [ df.iloc[:,20][9],
                    df.iloc[:,20][10],
                    df.iloc[:,20][11],
                    df.iloc[:,20][12],
                    df.iloc[:,20][13],
                    df.iloc[:,20][14],
                    df.iloc[:,20][15],
                    df.iloc[:,20][16],
                    df.iloc[:,20][17],
                    df.iloc[:,20][18]]
    # Day 18
    word_day18 = df.iloc[:,21][8]
    # Emisions
    day18_values = [ df.iloc[:,21][9],
                    df.iloc[:,21][10],
                    df.iloc[:,21][11],
                    df.iloc[:,21][12],
                    df.iloc[:,21][13],
                    df.iloc[:,21][14],
                    df.iloc[:,21][15],
                    df.iloc[:,21][16],
                    df.iloc[:,21][17],
                    df.iloc[:,21][18]]
    # Day 19
    word_day19 = df.iloc[:,22][8]
    # Emisions
    day19_values = [ df.iloc[:,22][9],
                    df.iloc[:,22][10],
                    df.iloc[:,22][11],
                    df.iloc[:,22][12],
                    df.iloc[:,22][13],
                    df.iloc[:,22][14],
                    df.iloc[:,22][15],
                    df.iloc[:,22][16],
                    df.iloc[:,22][17],
                    df.iloc[:,22][18]]
    # Day 20
    word_day20 = df.iloc[:,23][8]
    # Emisions
    day20_values = [ df.iloc[:,23][9],
                    df.iloc[:,23][10],
                    df.iloc[:,23][11],
                    df.iloc[:,23][12],
                    df.iloc[:,23][13],
                    df.iloc[:,23][14],
                    df.iloc[:,23][15],
                    df.iloc[:,23][16],
                    df.iloc[:,23][17],
                    df.iloc[:,23][18]]
    # Day 21
    word_day21 = df.iloc[:,24][8]
    # Emisions
    day21_values = [ df.iloc[:,24][9],
                    df.iloc[:,24][10],
                    df.iloc[:,24][11],
                    df.iloc[:,24][12],
                    df.iloc[:,24][13],
                    df.iloc[:,24][14],
                    df.iloc[:,24][15],
                    df.iloc[:,24][16],
                    df.iloc[:,24][17],
                    df.iloc[:,24][18]]
    # Day 22
    word_day22 = df.iloc[:,25][8]
    # Emisions
    day22_values = [ df.iloc[:,25][9],
                    df.iloc[:,25][10],
                    df.iloc[:,25][11],
                    df.iloc[:,25][12],
                    df.iloc[:,25][13],
                    df.iloc[:,25][14],
                    df.iloc[:,25][15],
                    df.iloc[:,25][16],
                    df.iloc[:,25][17],
                    df.iloc[:,25][18]]
    # Day 23
    word_day23 = df.iloc[:,26][8]
    # Emisions
    day23_values = [ df.iloc[:,26][9],
                    df.iloc[:,26][10],
                    df.iloc[:,26][11],
                    df.iloc[:,26][12],
                    df.iloc[:,26][13],
                    df.iloc[:,26][14],
                    df.iloc[:,26][15],
                    df.iloc[:,26][16],
                    df.iloc[:,26][17],
                    df.iloc[:,26][18]]
    # Day 24
    word_day24 = df.iloc[:,27][8]
    # Emisions
    day24_values = [ df.iloc[:,27][9],
                    df.iloc[:,27][10],
                    df.iloc[:,27][11],
                    df.iloc[:,27][12],
                    df.iloc[:,27][13],
                    df.iloc[:,27][14],
                    df.iloc[:,27][15],
                    df.iloc[:,27][16],
                    df.iloc[:,27][17],
                    df.iloc[:,27][18]]
    # Day 25
    word_day25 = df.iloc[:,28][8]
    # Emisions
    day25_values = [ df.iloc[:,28][9],
                    df.iloc[:,28][10],
                    df.iloc[:,28][11],
                    df.iloc[:,28][12],
                    df.iloc[:,28][13],
                    df.iloc[:,28][14],
                    df.iloc[:,28][15],
                    df.iloc[:,28][16],
                    df.iloc[:,28][17],
                    df.iloc[:,28][18]]
    # Day 26
    word_day26 = df.iloc[:,29][8]
    # Emisions
    day26_values = [ df.iloc[:,29][9],
                    df.iloc[:,29][10],
                    df.iloc[:,29][11],
                    df.iloc[:,29][12],
                    df.iloc[:,29][13],
                    df.iloc[:,29][14],
                    df.iloc[:,29][15],
                    df.iloc[:,29][16],
                    df.iloc[:,29][17],
                    df.iloc[:,29][18]]
    # Day 27
    word_day27 = df.iloc[:,30][8]
    # Emisions
    day27_values = [ df.iloc[:,30][9],
                    df.iloc[:,30][10],
                    df.iloc[:,30][11],
                    df.iloc[:,30][12],
                    df.iloc[:,30][13],
                    df.iloc[:,30][14],
                    df.iloc[:,30][15],
                    df.iloc[:,30][16],
                    df.iloc[:,30][17],
                    df.iloc[:,30][18]]
    # Day 28
    word_day28 = df.iloc[:,31][8]
    # Emisions
    day28_values = [ df.iloc[:,31][9],
                    df.iloc[:,31][10],
                    df.iloc[:,31][11],
                    df.iloc[:,31][12],
                    df.iloc[:,31][13],
                    df.iloc[:,31][14],
                    df.iloc[:,31][15],
                    df.iloc[:,31][16],
                    df.iloc[:,31][17],
                    df.iloc[:,31][18]]
    # Day 29
    word_day29 = df.iloc[:,32][8]
    # Emisions
    day29_values = [ df.iloc[:,32][9],
                    df.iloc[:,32][10],
                    df.iloc[:,32][11],
                    df.iloc[:,32][12],
                    df.iloc[:,32][13],
                    df.iloc[:,32][14],
                    df.iloc[:,32][15],
                    df.iloc[:,32][16],
                    df.iloc[:,32][17],
                    df.iloc[:,32][18]]
    # Day 30
    word_day30 = df.iloc[:,33][8]
    # Emisions
    day30_values = [ df.iloc[:,33][9],
                    df.iloc[:,33][10],
                    df.iloc[:,33][11],
                    df.iloc[:,33][12],
                    df.iloc[:,33][13],
                    df.iloc[:,33][14],
                    df.iloc[:,33][15],
                    df.iloc[:,33][16],
                    df.iloc[:,33][17],
                    df.iloc[:,33][18]]
    # Day 31
    word_day31 = df.iloc[:,34][8]
    # Emisions
    day31_values = [ df.iloc[:,34][9],
                    df.iloc[:,34][10],
                    df.iloc[:,34][11],
                    df.iloc[:,34][12],
                    df.iloc[:,34][13],
                    df.iloc[:,34][14],
                    df.iloc[:,34][15],
                    df.iloc[:,34][16],
                    df.iloc[:,34][17],
                    df.iloc[:,34][18]]
    # Top Salary per Program
    word_salary_per_program = df.iloc[:,36][5]
    # Top values
    salary_per_program_values = [   df.iloc[:,36][9],
                                    df.iloc[:,36][10],
                                    df.iloc[:,36][11],
                                    df.iloc[:,36][12],
                                    df.iloc[:,36][13],
                                    df.iloc[:,36][14],
                                    df.iloc[:,36][15],
                                    df.iloc[:,36][16],
                                    df.iloc[:,36][17],
                                    df.iloc[:,36][18]]
    # Remote Import
    word_remote = df.iloc[:,38][5]
    # remote values
    remote_values = [   df.iloc[:,38][9],
                        df.iloc[:,38][10],
                        df.iloc[:,38][11],
                        df.iloc[:,38][12],
                        df.iloc[:,38][13],
                        df.iloc[:,38][14],
                        df.iloc[:,38][15],
                        df.iloc[:,38][16],
                        df.iloc[:,38][17],
                        df.iloc[:,38][18]]
    # Interrupt Import
    word_interrupt = df.iloc[:,39][5]
    # interrupt values
    interrupt_values = [df.iloc[:,39][9],
                        df.iloc[:,39][10],
                        df.iloc[:,39][11],
                        df.iloc[:,39][12],
                        df.iloc[:,39][13],
                        df.iloc[:,39][14],
                        df.iloc[:,39][15],
                        df.iloc[:,39][16],
                        df.iloc[:,39][17],
                        df.iloc[:,39][18]]
    # Multiple Import
    word_multiple = df.iloc[:,40][5]
    # multiple values
    multiple_values = [ df.iloc[:,40][9],
                        df.iloc[:,40][10],
                        df.iloc[:,40][11],
                        df.iloc[:,40][12],
                        df.iloc[:,40][13],
                        df.iloc[:,40][14],
                        df.iloc[:,40][15],
                        df.iloc[:,40][16],
                        df.iloc[:,40][17],
                        df.iloc[:,40][18]]
    # Night
    word_night = df.iloc[:,41][5]
    # night values
    night_values = [df.iloc[:,41][9],
                    df.iloc[:,41][10],
                    df.iloc[:,41][11],
                    df.iloc[:,41][12],
                    df.iloc[:,41][13],
                    df.iloc[:,41][14],
                    df.iloc[:,41][15],
                    df.iloc[:,41][16],
                    df.iloc[:,41][17],
                    df.iloc[:,41][18]]
    # Discount
    word_discount = df.iloc[:,42][5]
    # discolunt values
    discount_values = [ df.iloc[:,42][9],
                        df.iloc[:,42][10],
                        df.iloc[:,42][11],
                        df.iloc[:,42][12],
                        df.iloc[:,42][13],
                        df.iloc[:,42][14],
                        df.iloc[:,42][15],
                        df.iloc[:,42][16],
                        df.iloc[:,42][17],
                        df.iloc[:,42][18]]
    # Total program execution times
    word_total_execution = df.iloc[:,35][5]
    # execution values
    execution_values = [    day1_values[0] + 
                            day2_values[0] + 
                            day3_values[0] + 
                            day4_values[0] + 
                            day5_values[0] + 
                            day6_values[0] + 
                            day7_values[0] + 
                            day8_values[0] +
                            day9_values[0] + 
                            day10_values[0] + 
                            day11_values[0] + 
                            day12_values[0] + 
                            day13_values[0] + 
                            day14_values[0] + 
                            day15_values[0] +
                            day16_values[0] + 
                            day17_values[0] + 
                            day18_values[0] + 
                            day19_values[0] + 
                            day20_values[0] + 
                            day21_values[0] + 
                            day22_values[0] + 
                            day23_values[0] +
                            day24_values[0] + 
                            day25_values[0] + 
                            day26_values[0] + 
                            day27_values[0] + 
                            day28_values[0] + 
                            day29_values[0] + 
                            day30_values[0] +
                            day31_values[0],
                            day1_values[1] + 
                            day2_values[1] + 
                            day3_values[1] + 
                            day4_values[1] + 
                            day5_values[1] + 
                            day6_values[1] + 
                            day7_values[1] + 
                            day8_values[1] +
                            day9_values[1] + 
                            day10_values[1] + 
                            day11_values[1] + 
                            day12_values[1] + 
                            day13_values[1] + 
                            day14_values[1] + 
                            day15_values[1] +
                            day16_values[1] + 
                            day17_values[1] + 
                            day18_values[1] + 
                            day19_values[1] + 
                            day20_values[1] + 
                            day21_values[1] + 
                            day22_values[1] + 
                            day23_values[1] +
                            day24_values[1] + 
                            day25_values[1] + 
                            day26_values[1] + 
                            day27_values[1] + 
                            day28_values[1] + 
                            day29_values[1] + 
                            day30_values[1] +
                            day31_values[1],
                            day1_values[2] + 
                            day2_values[2] + 
                            day3_values[2] + 
                            day4_values[2] + 
                            day5_values[2] + 
                            day6_values[2] + 
                            day7_values[2] + 
                            day8_values[2] +
                            day9_values[2] + 
                            day10_values[2] + 
                            day11_values[2] + 
                            day12_values[2] + 
                            day13_values[2] + 
                            day14_values[2] + 
                            day15_values[2] +
                            day16_values[2] + 
                            day17_values[2] + 
                            day18_values[2] + 
                            day19_values[2] + 
                            day20_values[2] + 
                            day21_values[2] + 
                            day22_values[2] + 
                            day23_values[2] +
                            day24_values[2] + 
                            day25_values[2] + 
                            day26_values[2] + 
                            day27_values[2] + 
                            day28_values[2] + 
                            day29_values[2] + 
                            day30_values[2] +
                            day31_values[2],
                            day1_values[3] + 
                            day2_values[3] + 
                            day3_values[3] + 
                            day4_values[3] + 
                            day5_values[3] + 
                            day6_values[3] + 
                            day7_values[3] + 
                            day8_values[3] +
                            day9_values[3] + 
                            day10_values[3] + 
                            day11_values[3] + 
                            day12_values[3] + 
                            day13_values[3] + 
                            day14_values[3] + 
                            day15_values[3] +
                            day16_values[3] + 
                            day17_values[3] + 
                            day18_values[3] + 
                            day19_values[3] + 
                            day20_values[3] + 
                            day21_values[3] + 
                            day22_values[3] + 
                            day23_values[3] +
                            day24_values[3] + 
                            day25_values[3] + 
                            day26_values[3] + 
                            day27_values[3] + 
                            day28_values[3] + 
                            day29_values[3] + 
                            day30_values[3] +
                            day31_values[3],
                            day1_values[4] + 
                            day2_values[4] + 
                            day3_values[4] + 
                            day4_values[4] + 
                            day5_values[4] + 
                            day6_values[4] + 
                            day7_values[4] + 
                            day8_values[4] +
                            day9_values[4] + 
                            day10_values[4] + 
                            day11_values[4] + 
                            day12_values[4] + 
                            day13_values[4] + 
                            day14_values[4] + 
                            day15_values[4] +
                            day16_values[4] + 
                            day17_values[4] + 
                            day18_values[4] + 
                            day19_values[4] + 
                            day20_values[4] + 
                            day21_values[4] + 
                            day22_values[4] + 
                            day23_values[4] +
                            day24_values[4] + 
                            day25_values[4] + 
                            day26_values[4] + 
                            day27_values[4] + 
                            day28_values[4] + 
                            day29_values[4] + 
                            day30_values[4] +
                            day31_values[4],
                            day1_values[5] + 
                            day2_values[5] + 
                            day3_values[5] + 
                            day4_values[5] + 
                            day5_values[5] + 
                            day6_values[5] + 
                            day7_values[5] + 
                            day8_values[5] +
                            day9_values[5] + 
                            day10_values[5] + 
                            day11_values[5] + 
                            day12_values[5] + 
                            day13_values[5] + 
                            day14_values[5] + 
                            day15_values[5] +
                            day16_values[5] + 
                            day17_values[5] + 
                            day18_values[5] + 
                            day19_values[5] + 
                            day20_values[5] + 
                            day21_values[5] + 
                            day22_values[5] + 
                            day23_values[5] +
                            day24_values[5] + 
                            day25_values[5] + 
                            day26_values[5] + 
                            day27_values[5] + 
                            day28_values[5] + 
                            day29_values[5] + 
                            day30_values[5] +
                            day31_values[5],
                            day1_values[6] + 
                            day2_values[6] + 
                            day3_values[6] + 
                            day4_values[6] + 
                            day5_values[6] + 
                            day6_values[6] + 
                            day7_values[6] + 
                            day8_values[6] +
                            day9_values[6] + 
                            day10_values[6] + 
                            day11_values[6] + 
                            day12_values[6] + 
                            day13_values[6] + 
                            day14_values[6] + 
                            day15_values[6] +
                            day16_values[6] + 
                            day17_values[6] + 
                            day18_values[6] + 
                            day19_values[6] + 
                            day20_values[6] + 
                            day21_values[6] + 
                            day22_values[6] + 
                            day23_values[6] +
                            day24_values[6] + 
                            day25_values[6] + 
                            day26_values[6] + 
                            day27_values[6] + 
                            day28_values[6] + 
                            day29_values[6] + 
                            day30_values[6] +
                            day31_values[6],
                            day1_values[7] + 
                            day2_values[7] + 
                            day3_values[7] + 
                            day4_values[7] + 
                            day5_values[7] + 
                            day6_values[7] + 
                            day7_values[7] + 
                            day8_values[7] +
                            day9_values[7] + 
                            day10_values[7] + 
                            day11_values[7] + 
                            day12_values[7] + 
                            day13_values[7] + 
                            day14_values[7] + 
                            day15_values[7] +
                            day16_values[7] + 
                            day17_values[7] + 
                            day18_values[7] + 
                            day19_values[7] + 
                            day20_values[7] + 
                            day21_values[7] + 
                            day22_values[7] + 
                            day23_values[7] +
                            day24_values[7] + 
                            day25_values[7] + 
                            day26_values[7] + 
                            day27_values[7] + 
                            day28_values[7] + 
                            day29_values[7] + 
                            day30_values[7] +
                            day31_values[7],
                            day1_values[8] + 
                            day2_values[8] + 
                            day3_values[8] + 
                            day4_values[8] + 
                            day5_values[8] + 
                            day6_values[8] + 
                            day7_values[8] + 
                            day8_values[8] +
                            day9_values[8] + 
                            day10_values[8] + 
                            day11_values[8] + 
                            day12_values[8] + 
                            day13_values[8] + 
                            day14_values[8] + 
                            day15_values[8] +
                            day16_values[8] + 
                            day17_values[8] + 
                            day18_values[8] + 
                            day19_values[8] + 
                            day20_values[8] + 
                            day21_values[8] + 
                            day22_values[8] + 
                            day23_values[8] +
                            day24_values[8] + 
                            day25_values[8] + 
                            day26_values[8] + 
                            day27_values[8] + 
                            day28_values[8] + 
                            day29_values[8] + 
                            day30_values[8] +
                            day31_values[8],
                            day1_values[9] + 
                            day2_values[9] + 
                            day3_values[9] + 
                            day4_values[9] + 
                            day5_values[9] + 
                            day6_values[9] + 
                            day7_values[9] + 
                            day8_values[9] +
                            day9_values[9] + 
                            day10_values[9] + 
                            day11_values[9] + 
                            day12_values[9] + 
                            day13_values[9] + 
                            day14_values[9] + 
                            day15_values[9] +
                            day16_values[9] + 
                            day17_values[9] + 
                            day18_values[9] + 
                            day19_values[9] + 
                            day20_values[9] + 
                            day21_values[9] + 
                            day22_values[9] + 
                            day23_values[9] +
                            day24_values[9] + 
                            day25_values[9] + 
                            day26_values[9] + 
                            day27_values[9] + 
                            day28_values[9] + 
                            day29_values[9] + 
                            day30_values[9] +
                            day31_values[9]]
    # Salary per Hour
    word_salary_per_hour = df.iloc[:,37][5]
    # salary per hour values
    salary_per_hour_values = [      salary_per_program_values[0]/190.6,
                                    salary_per_program_values[1]/190.6,
                                    salary_per_program_values[2]/190.6,
                                    salary_per_program_values[3]/190.6,
                                    salary_per_program_values[4]/190.6,
                                    salary_per_program_values[5]/190.6,
                                    salary_per_program_values[6]/190.6,
                                    salary_per_program_values[7]/190.6,
                                    salary_per_program_values[8]/190.6,
                                    salary_per_program_values[9]/190.6]
    # Import per Program
    word_import_per_program = df.iloc[:,43][5]
    # import per program values
    import_per_program_values = [   execution_values[0] * salary_per_hour_values[0] * realization_values[0] + remote_values[0] + interrupt_values[0] + multiple_values[0] + night_values[0] - discount_values[0],
                                    execution_values[1] * salary_per_hour_values[1] * realization_values[1] + remote_values[1] + interrupt_values[1] + multiple_values[1] + night_values[1] - discount_values[1],
                                    execution_values[2] * salary_per_hour_values[2] * realization_values[2] + remote_values[2] + interrupt_values[2] + multiple_values[2] + night_values[2] - discount_values[2],
                                    execution_values[3] * salary_per_hour_values[3] * realization_values[3] + remote_values[3] + interrupt_values[3] + multiple_values[3] + night_values[3] - discount_values[3],
                                    execution_values[4] * salary_per_hour_values[4] * realization_values[4] + remote_values[4] + interrupt_values[4] + multiple_values[4] + night_values[4] - discount_values[4],
                                    execution_values[5] * salary_per_hour_values[5] * realization_values[5] + remote_values[5] + interrupt_values[5] + multiple_values[5] + night_values[5] - discount_values[5],
                                    execution_values[6] * salary_per_hour_values[6] * realization_values[6] + remote_values[6] + interrupt_values[6] + multiple_values[6] + night_values[6] - discount_values[6],
                                    execution_values[7] * salary_per_hour_values[7] * realization_values[7] + remote_values[7] + interrupt_values[7] + multiple_values[7] + night_values[7] - discount_values[7],
                                    execution_values[8] * salary_per_hour_values[8] * realization_values[8] + remote_values[8] + interrupt_values[8] + multiple_values[8] + night_values[8] - discount_values[8],
                                    execution_values[9] * salary_per_hour_values[9] * realization_values[9] + remote_values[9] + interrupt_values[9] + multiple_values[9] + night_values[9] - discount_values[9]]
    # Jobs Data Frame
    jobs = {word_program: program_values,
            word_complexity: complexity_values,
            word_air: air_values,
            word_realization: realization_values,
            word_day1: day1_values,
            word_day2: day2_values,
            word_day3: day3_values,
            word_day4: day4_values,
            word_day5: day5_values,
            word_day6: day6_values,
            word_day7: day7_values,
            word_day8: day8_values,
            word_day9: day9_values,
            word_day10: day10_values,
            word_day11: day11_values,
            word_day12: day12_values,
            word_day13: day13_values,
            word_day14: day14_values,
            word_day15: day15_values,
            word_day16: day16_values,
            word_day17: day17_values,
            word_day18: day18_values,
            word_day19: day19_values,
            word_day20: day20_values,
            word_day21: day21_values,
            word_day22: day22_values,
            word_day23: day23_values,
            word_day24: day24_values,
            word_day25: day25_values,
            word_day26: day26_values,
            word_day27: day27_values,
            word_day28: day28_values,
            word_day29: day29_values,
            word_day30: day30_values,
            word_day31: day31_values,
            word_total_execution: execution_values,
            word_salary_per_program: salary_per_program_values,
            word_salary_per_hour: salary_per_hour_values,
            word_remote: remote_values,
            word_interrupt: interrupt_values,
            word_multiple: multiple_values,
            word_night: night_values,
            word_discount: discount_values,
            word_import_per_program: import_per_program_values}

    return jobs

# status dict contains info about a worker
# jobs dict contains info about the work done by the same worker
def asociate_status_wit_jobs():
    try:
        for lvalue in record_dict.values():
            for df in lvalue:
                tmp_jobs = jobs_done(df)
                salary = 0
                for tmp_salary in tmp_jobs.get("Importe por Programa"):
                    salary += tmp_salary
                if worker_status(df):                                
                    worked.append(tmp_jobs)                    
                    salary_number_colunmn.append(salary)
                else:                
                    non_worked.append(tmp_jobs)
                    non_salary_number_colunmn.append(salary)
    except AttributeError:
        pass

# calculate all the worker's salaries on a specific date
# no matter the Human Resorce in which participates
def total_salary_per_worker_date(year, month):
    t_worker_name = []
    t_worker_ci = []
    t_worker_salary = []
    salary_dict = { 'Nombre' : t_worker_name,
                    'C.I' : t_worker_ci,
                    'Salario Total' : t_worker_salary}
    
    year_index_list = [i for i, e in enumerate(status['Año']) if e == year]        
    
    for year_index in year_index_list:
        if status['Mes'][year_index] == month:            
            if status['C.I'][year_index] in salary_dict['C.I']:            
                ci_index = salary_dict['C.I'].index(status['C.I'][year_index])
                salary_dict['Salario Total'][ci_index] += status['Salario'][year_index]
            else:
                salary_dict['Nombre'].append(status['Nombre del Trabajador'][year_index])
                salary_dict['C.I'].append(status['C.I'][year_index])
                salary_dict['Salario Total'].append(status['Salario'][year_index])
    return salary_dict

# compile all the status of the workers on a specific date
# no matter the Human Resorce in which participates
def status_per_worker_date(year, month):
    t_worker_name_column = []
    t_id_value_column = []
    t_position_name_column = []
    t_evaluation_value_column = []
    t_salary_scale_number_column = []
    t_salary_number_colunmn = []
    t_area_name_column = []
    t_human_value_column = []
    t_year_number_column = []
    t_month_number_column = []
    t_status = {  'Nombre del Trabajador': t_worker_name_column,
            'C.I': t_id_value_column,
            'Nombre del Cargo': t_position_name_column,
            'Nivel de Evaluación': t_evaluation_value_column,
            'Salario Escala': t_salary_scale_number_column,
            'Salario': t_salary_number_colunmn,
            'ÁREA': t_area_name_column,
            'R.H': t_human_value_column,
            'Año': t_year_number_column,
            'Mes': t_month_number_column}

    year_index_list = [i for i, e in enumerate(status['Año']) if e == year]        
    
    for year_index in year_index_list:
        if status['Mes'][year_index] == month:            
            t_status['Nombre del Trabajador'].append(status['Nombre del Trabajador'][year_index])
            t_status['C.I'].append(status['C.I'][year_index])
            t_status['Nombre del Cargo'].append(status['Nombre del Cargo'][year_index])
            t_status['Nivel de Evaluación'].append(status['Nivel de Evaluación'][year_index])
            t_status['Salario Escala'].append(status['Salario Escala'][year_index])
            t_status['Salario'].append(status['Salario'][year_index])
            t_status['ÁREA'].append(status['ÁREA'][year_index])
            t_status['R.H'].append(status['R.H'][year_index])
            t_status['Año'].append(status['Año'][year_index])
            t_status['Mes'].append(status['Mes'][year_index])
    return t_status

# compile all the jobs maked for the workers on a specific date
# no matter the Human Resorce in which participates
def job_done_per_worker_date(year, month):        
    t_data = []
    
    year_index_list = [i for i, e in enumerate(status['Año']) if e == year]        
    
    for year_index in year_index_list:
        if status['Mes'][year_index] == month:            
            t_data.append((status['Nombre del Trabajador'][year_index],
                           status['C.I'][year_index],
                           status['R.H'][year_index],
                           status['Trabajado'][year_index]))
    return t_data


#traverse_dir()
#asociate_status_wit_jobs()
#print(status)
#print(non_status)
#print(total_salary_per_worker_date(2021,1))
#print(job_done_per_worker_date(2021,1))


 #jobs_df = pd.DataFrame(jobs)
 #   jobs_df = jobs_df.dropna(axis='index')
 #   
 #   # 'Styler' object has no attributes
 #   jobs_df = jobs_df.style.format({word_salary_per_hour:'{:.2f}',
 #                                   word_import_per_program:'{:.2f}',
 #                                   word_realization:'{:.2f}',
 #                                 word_remote:'{:.2f}',
 #                                 word_interrupt:'{:.2f}',
 #                                 word_multiple:'{:.2f}',
 #                                 word_night:'{:.2f}',
 #                                 word_discount:'{:.2f}'})


 