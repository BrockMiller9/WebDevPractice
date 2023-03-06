from flask import Flask, render_template, jsonify

app= Flask(__name__)

JOBS = [
    {
        'id':1,
        'title': 'Data Analyst',
        'location': 'Seattle, Washington',
        'salary': '$50,000'
    },
    {
        'id':2,
        'title': 'Data Scientist',
        'location': 'Vancouver, British-Columbia',
        'salary': '$70,000'
    },
    {
        'id':3,
        'title': 'Frontend Engineer',
        'location': 'Remote',
    },
    {
        'id':4,
        'title': 'Backend Engineer',
        'location': 'San-Francisco, California',
        'salary': '$80,000'
    },
]


@app.route('/')
def hello_world():
    return render_template('home.html', jobs = JOBS, company_name='Freedom')


@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)







if __name__ == '__main__':
    app.run('0.0.0.0', debug =True)

