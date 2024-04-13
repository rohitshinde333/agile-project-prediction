from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from openai import OpenAI
from flask_cors import CORS
client = OpenAI(
    api_key='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',
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///developers.db'
db = SQLAlchemy(app)
CORS(app)
class Developer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tech_stack = db.Column(db.String(100), nullable=False)
    experience = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Developer(name={self.name}, tech_stack={self.tech_stack}, experience={self.experience})"

@app.route('/suggest_team', methods=['POST'])
def suggest_team():
    requirements = request.json.get('requirements')

    available_engineers = Developer.query.all()
    engineer_info = ', '.join([f"{engineer.name} ({engineer.tech_stack})" for engineer in available_engineers])

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Given the project specifications provided in the document, suggest the technology stack and the number of people required for the project. Currently available engineers: {engineer_info}. Requirements: {requirements}"
            }
        ],
        model="gpt-3.5-turbo",
    )
    message = response.model_dump_json(indent=2)
    return message


@app.route('/developers', methods=['GET', 'POST'])
def manage_developers():
    if request.method == 'GET':
        developers = Developer.query.all()
        developers_data = [{'name': developer.name, 'tech_stack': developer.tech_stack, 'experience': developer.experience} for developer in developers]
        return jsonify({'developers': developers_data})
    elif request.method == 'POST':
        data = request.json
        new_developer = Developer(name=data['name'], tech_stack=data['tech_stack'], experience=data['experience'])
        db.session.add(new_developer)
        db.session.commit()
        return jsonify({'message': 'Developer added successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
