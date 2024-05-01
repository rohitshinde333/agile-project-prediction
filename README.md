Of course! Here's the updated README file:

# L&T Createch Competition - Predictive Modeling for Agile Project Management

## Problem Statement
The objective of this project was to develop a predictive modeling algorithm to facilitate the monitoring and controlling of agile projects, such as software development, application development, web development, and IT projects.

## Project Overview
This project aimed to create a robust system for monitoring and controlling agile projects using predictive modeling techniques. It consisted of two main components: a backend developed using Python Flask and a frontend developed using Vue.js. The backend was responsible for processing data and making predictions, while the frontend provided an intuitive user interface for interacting with the system.

## Dataset
The project utilized the Jira issue and comments dataset from Kaggle for fine-tuning the predictive model. This dataset provided valuable insights into project management activities, including issue tracking and communication.

## Model Fine-Tuning
The predictive model was fine-tuned using the Jira dataset to classify project issues and comments into three categories: negative, neutral, and positive. The fine-tuned model achieved the following classification report:

```
              precision    recall  f1-score   support

    negative       0.82      0.74      0.78       235
     neutral       0.92      0.91      0.91      1186
    positive       0.80      0.89      0.84       338

    accuracy                           0.88      1759
   macro avg       0.85      0.85      0.84      1759
weighted avg       0.88      0.88      0.88      1759
```

## Contributors
- Rohit Shinde
- Harishri Vaidya
- Nutan Chapade

## Setup Instructions
### Backend:
1. Navigate to the `backend` directory.
2. Install the required Python dependencies using `pip install -r requirements.txt`.
3. Run the Flask server using `python main.py`.

### Frontend:
1. Navigate to the `frontend` directory.
2. Install the required Node.js dependencies using `npm install`.
3. Start the Vue.js development server using `npm run serve`.

## License
[Insert License Here]

## Acknowledgements
We would like to express our gratitude to L&T Createch for organizing the competition and providing us with the opportunity to work on this project. Additionally, we would like to thank the Kaggle community for providing access to the Jira dataset, which was instrumental in fine-tuning our predictive model.
