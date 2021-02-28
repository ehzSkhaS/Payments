import numpy as np
import matplotlib.pyplot as plt

# Make a graph from total salary data frame
# and return the matplotlib fig
def plot_data(df_salary):        
    # converting data frames to numpy arrays
    array_name = df_salary.loc[:, 'Nombre del Trabajador'].values
    array_ci = df_salary.loc[:, 'C.I'].values
    array_ci = array_ci.astype(str)
    array_salary = df_salary.loc[:, 'Salario Total'].values
    np.around(array_salary, 2, array_salary)         
    
    n_rows = len(array_ci)           
    values = np.arange(0,30000, 5000)        
    values_minor = np.arange(0, 30000, 1000)
    index = np.arange(n_rows)        
    bar_width = 0.7

    fig = plt.figure(figsize = (15,n_rows), 
                     facecolor = 'white', 
                     edgecolor = "#eaeaf2")   
    # configure axes                     
    ax = plt.axes(frameon = False)    
    ax.set_xticks(values_minor, minor=True)
    plt.grid(which='both', axis='x')
    plt.grid(which='major', axis='y')

    # label structure of: C.I + name
    array_yticks_labels = []
    for e, i in zip(array_ci, array_name):
        array_yticks_labels.append(e + "\n" + i)    
    
    for row in range(n_rows):
        # bars configuration and personalization
        plt.barh(y = index,
                 width = array_salary, 
                 height = bar_width,           
                 linewidth = 5,
                 edgecolor = '#80d4d5',
                 color = '#ceebf8')
        # text with the value of the salary,
        #  at the end of every barh
        plt.text(x = array_salary[row] + 2000,
                 y = index[row],
                 s = "$ " + str(array_salary[row]),
                 horizontalalignment = 'center',
                 verticalalignment = 'center',                 
                 bbox=dict(facecolor = '#c3d9ff', alpha = 0.9))            
    
    # x axis labels distribution and personalization
    xticks_label = plt.xticks(ticks = values, 
                              labels = ['$ %d' % val for val in values])
    for label in xticks_label[1]:
        label.set_bbox(dict(facecolor = '#c3d9ff', 
                            alpha = 0.9))       

    # y axis labels distribution and personalization
    yticks_label = plt.yticks(ticks = index,                              
                              labels = array_yticks_labels)
    for label in yticks_label[1]:
        label.set_bbox(dict(facecolor = '#c3d9ff', 
                            alpha = 0.9))
        label.set_ha('right')
        label.set_va('center')    

    return fig
    
    