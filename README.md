<p align="center"><img width=30% src="static/adl_dlmml.png"></p>

<center>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)
[![GitHub issues](https://img.shields.io/github/issues-raw/Auto-DL/DLMML?color=red)](https://github.com/Auto-DL/DLMML/issues?q=is%3Aopen+is%3Aissue)
[![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/Auto-DL/DLMML)](https://github.com/Auto-DL/DLMML/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/Auto-DL/DLMML)](https://github.com/Auto-DL/DLMML/pulls?q=is%3Aopen+is%3Apr)
[![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed-raw/Auto-DL/DLMML?color=green)](https://github.com/Auto-DL/DLMML/pulls?q=is%3Apr+is%3Aclosed)

</center>

# DLMML

The intermediary representation of the generated model.
This ideally would be done using our [FrontEnd](https://github.com/Auto-DL/Generator/tree/fossunited-demo/FrontEndApp).


## How to run

#### There are essentially three ways to run this code

1. The code is an API, which is called by the Generator frontend. For instructions on how to run the React and Django Servers (GUI) please head on to [User Guidlelines of the Generator Repository](https://github.com/Auto-DL/Generator/blob/master/docs/userguide.md)

2. Run the dev-server and call the API with a POST request (no-GUI). However, tools like postman can be used.

3. Don't want to run the server? Prefer jupyter notebooks instead? Head on to our `notebooks` directory

#### Steps for method 2: 

1. ```sh
    # clone the repo
    git clone https://github.com/Auto-DL/DLMML.git
    ```

2. *Activate your environment* (not compulsory but highly recommended)

3. Create a MongoDB (local or atlas) database and put the configuration details in a ".env" file (without quotes)

4. Place data in the `./data` directory

5. ```sh
    # change dir
    cd dev_server
    # run the flask app
    python app.py
    ```
6. Make the post request.

***Note:*** For an example post request and to know how the data is expected in the `./data` directory please head on to the [User Guide](https://github.com/Auto-DL/DLMML/blob/master/docs/userguide.md) 

#### What if I want to go for method 3:

- Follow steps 1 and 2 of method 2
- Run the `jupyter-notebook` command
- Using the GUI, navigate and run the notebooks
- [This](https://github.com/Auto-DL/DLMML/blob/master/notebooks/Code%20Generator%20PlayBook.ipynb) can be a good starting point


## Where to go next?

#### To know more about the project and initiative, please visit our [website](https://auto-dl.github.io/)

#### Curious to know about our front-end or backend development? [Here](https://github.com/Auto-DL/Generator), Have a look :)

## Note
- To know more about the technicalities of the project, read the our [developer guidelines](https://github.com/Auto-DL/DLMML/blob/master/docs/devguide.md).
- For more detailed instructions to run the DLMML part. Read our [User guidelines](https://github.com/Auto-DL/DLMML/blob/master/docs/userguide.md) 

## Contributing
Please take a look at our [contributing](https://github.com/Auto-DL/DLMML/blob/master/docs/contributing.md) guidelines if you're interested in helping!

#### Features to add
- Check if generated code is correct (current thought is to call model.compile and return errors if any)

- Add predict functionality to the generated model

- Add different model evaluation parameters

- Test for backward compatibility of libraries versions

- Benchmarking parameters

- Add model generation code for pytorch

- Visualization and data preprocessing steps to be added
