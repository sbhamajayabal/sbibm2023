from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def student_regn_form():
    if request.method=='POST':
        rno.request.form['rno']
        name=request.form['name']
        émail.request.form['email']
        mobile.request.form['mobile']
        branch.request.form['branch']
        addr.request.form['addr']
        role.request.form['role']
        pwd.request.form['pwd']
        submitted=True
        
        # Pass the form data to the template
        return render_template('index.html', 
                               rno=rno, 
                               name=name,
                               email=email, 
                               mobile=mobilp,
                               branch=branch,
                               addr=addr,
                               role=role,
                               pwd=pwd,
                               submitted=submitted
                              )


    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)