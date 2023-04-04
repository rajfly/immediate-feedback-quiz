# immediate-feedback-quiz
A simple python based application designed to give immediate feedback to participants for a quiz on army ants.

### Install and run 
```bash
# install
conda create -y -n quiz python=3.9 && conda activate quiz
pip install pandas

# run for each participant
python quiz.py

# run after everyone has taken the quiz to combine results from all participant csv files
pytnon combine.py
```