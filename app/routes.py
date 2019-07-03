from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import RegistrationForm
import boto3

dynamodb = boto3.client('dynamodb',region_name = 'us-east-1')


@app.route('/', methods=['GET', 'POST'])
def index():
    responses = dynamodb.get_item(
        TableName='users',
        Key={
                "userid": {
                    "N": "1"
                },
                "username": {
                    "S": "peter"
                }
        }
    )
    print(responses)
    form = RegistrationForm()
    if form.validate_on_submit():
        Responses = dynamodb.put_item(
            TableName='users',
            Item={
                "userid": {
                    "N": form.userid.data
                },
                "username": {
                    "S": form.username.data
                }
            }
        )
        print(Responses)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('index.html', title='Home', item=responses, form=form)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        Responses = dynamodb.put_item(
            TableName='users',
            Item={
                "userid": {
                    "N": form.userid.data
                },
                "username": {
                    "S": form.username.data
                }
            }
        )
        print(Responses)
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)
