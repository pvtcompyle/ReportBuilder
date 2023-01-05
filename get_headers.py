import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__)

def get_data(headers):
    # read the CSV file
    df = pd.read_csv("data.csv")
    
    # select the specified headers
    df = df[headers]
    
    # return the data as a list of dictionaries
    return df.to_dict(orient='records')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # get the selected headers from the form
        headers = request.form.getlist("headers")
        
        # get the data for the selected headers
        data = get_data(headers)
        
        # render the template with the data
        return render_template("index.html", data=data, headers=headers)
    else:
        # read the CSV file and get all the headers
        df = pd.read_csv("data.csv")
        all_headers = df.columns.tolist()
        
        # render the template with the list of all headers
        return render_template("index.html", all_headers=all_headers)



if __name__ == "__main__":
    app.run()
