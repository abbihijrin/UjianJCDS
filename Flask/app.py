from flask import Flask,render_template
from plots import count_type1,dist_total
from cleaning_data import data_mpg
app = Flask(__name__)

# ROUTE
# RENDER TEMPLATE
# RENDER TEMPLATE WITH VARIABLE

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/data')
def data():
    data = data_mpg().head()
    return render_template('table_data.html' , data=data)


@app.route('/plots')
def plots():
    plot1 = count_type1()
    plot2 = dist_total()
    return render_template('plots.html' , data=[plot1,plot2])

@app.route('/stats')
def stats():
    return render_template('stats.html')









# @app.route('/hello')
# def hello():
#     hasil = 5 + 19
#     return 'Ini Route Hello ' + str(hasil)

# @app.route('/template')
# def sabeb():
#     return render_template('contoh.html')

# @app.route('/template-with-data')
# def template_with_data():
#     # data = {
#     #     'name' : 'fikri',
#     #     'name2' : 'seto',
#     #     'name3' : 'Andi'
#     # }
#     data = ['Fikri' , 'Seto' , 'Andi']
#     return render_template('data.html', nama = data , panjang= len(data))

if __name__ == '__main__':
    app.run(debug=True, port=9999)
