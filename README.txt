Usage -> 

#set up vietual environment
python -m venv ./venv

#start virtual environment
./venv/Scripts/activate.ps1

#install required packages
pip install -r requirements.txt 

#run script
python -m valid_emaol_checker.py

#when prompted, input path to csv file with one wor for header, 
followed by a list of email addressefa-spin

#csv file will be output in same folder as script