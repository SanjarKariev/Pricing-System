from flask import Flask, render_template, request, redirect, url_for, make_response
import mysql.connector
import datetime

connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '32753275',
        database='Session'
)

app = Flask(__name__)


@app.route('/saveStudent', methods=['POST'])
def saveStudent():
    mycursor = connection.cursor(buffered=True)

    # try:
    Surname = request.form['Surname']
    Name = request.form['Name']
    MiddleName = request.form['MiddleName']
    Course = request.form['Course']
    Group = request.form['Group']
    Rating = request.form['Rating']
    code = request.form['code']
    select = request.form['select']
    data = request.form['data']
    DisciplineCode = request.form['DisciplineCode']



    mycursor.execute(f'INSERT INTO `CADETS` (`Course Code`,`Surname`,`Name`,`Middle Name`,`Course`,`Group`) VALUES ({int(code)}, "{Surname}", "{Name}", "{MiddleName}", {int(Course)}," {Group}") ')
    connection.commit()

    mycursor.execute(f'INSERT INTO  `OFFSETS` (`Course Code`,`The Date`,`Discipline Code`,`Offset`) VALUES ({int(code)}, NOW(),"{int(DisciplineCode)}", {int(select)})')
    connection.commit()

    mycursor.execute(f'INSERT INTO  `EXAMS` (`Course Code`,`The Date`,`Discipline Code` , `Rating`) VALUES ({int(code)}, NOW(),"{int(DisciplineCode)}", {int(Rating)})')
    connection.commit()

    response = make_response('Все ок!', 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

    # except Exception as e:
    #
    #     response = make_response('Ошибка', 200)
    #     response.headers['Access-Control-Allow-Origin'] = '*'
    #     return response

@app.route('/Discipline', methods=['POST'])
def Discipline():
    mycursor = connection.cursor(buffered=True)

    try:
        DisciplineCode = request.form['DisciplineCode']
        DisciplineName = request.form['DisciplineName']
        NumberofHours = request.form['NumberofHours']

        print(NumberofHours, DisciplineName, DisciplineCode)

        mycursor.execute(f'INSERT INTO `DISCIPLINES` (`Discipline Code`,`Discipline Name` ,`Number of Hours`) VALUES ({int(DisciplineCode)},{DisciplineName}, {int(NumberofHours)})')
        connection.commit()

        response = make_response('Все ок!', 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except Exception as e:

        response = make_response('Ошибка', 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')
