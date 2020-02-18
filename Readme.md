# Predict return propensity using IBM Cloud Pak for Data and Watson Machine Learning

As part of our Intelligent Sterling Call Center Solution, our AI Assistant can surface real time insights about the customer's orders, based on the customer's order history and previous transactions. It also provides actionable recommendations to provide easy resolutions to common customer issues leading to an enhanced customer experience. Machine Learning models and techniques are used on the aggregated customer data from multiple data sources, to gain customer insights like Customer Life time Value, Churn, Return Propensity, and Upsell Purchase Probability. These help the Call Center executive to know the customer better, and take better business decisions like Upsell, Cross-sell, and Customer appeasement during a customer conversation. In this code pattern, we'll walk you through how to build a simple model to predict the propensity of an order to be returned (Return Propensity).

In the growing era of e-commerce, products being returned amounts to a large portion of the lost revenue. Hence, the sooner we can identify the chances of an order being returned, the better equipped we are at reducing the loss of revenue, both directly and indirectly in the form of lost customers. In this code pattern, we leverage IBM Cloud Pak for Data with Watson Machine Learning, which enables the customers to build and deploy models in a cloud environment of their choice (Hybrid or Private). The dataset used in this code pattern consists of curated order records obtained from [IBM Sterling Order Management](https://www.ibm.com/products/order-management).

When you have completed this code pattern, you will understand how to:

* Leverage ICP4D, Watson Studio and Watson Machine Learning to build and deploy machine learning models.
* Build a model to classify returns.
* Generate predictions using the deployed model by making REST calls.


# Architecture Diagram

<p align="center">
  <img src="https://user-images.githubusercontent.com/8854447/74355360-c7bb7c00-4d8a-11ea-88b4-0e9d95363c6f.png">
</p>


# Flow

1. User loads the Jupyter notebook into the IBM Cloud Pak for Data platform.
2. The data set is loaded into the Jupyter Notebook, either directly from the github repo or by uploading a copy obtained from the github repo.
3. The data is preprocessed, machine learning models are built and saved to Watson Machine Learning on IBM Cloud Pak for Data.
4. The machine learning model is deployed into production on the IBM Cloud Pak for Data platform and a scoring endpoint is obtained.
5. Using the scoring endpoint, the model is used to predict the propensity of returning an order using a frontend application.


# Included components

* [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data): Deploy a complete data and AI private cloud with all the necessary infrastructure and software components in a matter of hours. Natively built on Red Hat OpenShift Container Platform, the IBM Cloud Pak for Data System provides optimized hardware to increase container performance, while also accelerating time to value of your data workloads.

* [IBM Watson Machine Learning](https://www.ibm.com/cloud/machine-learning): IBM Watson Machine Learning makes it easy and cost-effective to deploy AI and machine learning assets in public, private, hybrid or multicloud environments. Seamlessly scale up your AI initiatives, growing pilot projects into business-critical enterprise deployments without large up-front investments.

* [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio): Analyze data using RStudio, Jupyter, and Python in a configured, collaborative environment that includes IBM value-adds, such as managed Spark.


# Featured technologies

* [Jupyter Notebooks](https://jupyter.org): An open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and explanatory text.
* [Pandas](https://pandas.pydata.org): An open source library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
* [Scikit-Learn](https://scikit-learn.org/stable/): An open source machine learning library providing simple and efficient tools for predictive data analysis (such as classification, regression, and clustering) for the Python programming language.


# Prerequisites

* [IBM Cloud Pak for Data](https://www.ibm.com/products/cloud-pak-for-data)
* [Watson Machine Learning Add On for IBM Cloud Pak for Data](https://www.ibm.com/support/producthub/icpdata/docs/content/SSQNUZ_current/wsj/analyze-data/ml-install-overview.html)


# Steps

Follow these steps to setup and run this code pattern:

1. [Create a new project](#1-create-a-new-project)
2. [Add the dataset and custom library zip to the assets section of your project](#2-add-the-dataset-and-custom-library-zip-to-the-assets-section-of-your-project)
3. [Add the notebook to your project](#3-add-the-notebook-to-your-project)
4. [Follow the steps in the notebook](#4-follow-the-steps-in-the-notebook)
    1. [Load and preprocess the data](#i-load-and-preprocess-the-data)
    2. [Build the model](#ii-build-the-model)
    3. [Save and deploy the model](#iii-save-and-deploy-the-model)
5. [Test the model](#5-test-the-model)
6. [Create a Python Flask app that uses the model](#6-create-a-python-flask-app-that-uses-the-model)


## 1. Create a new project

Launch a browser and navigate to your IBM Cloud Pak for Data deployment.

Go to the (☰) menu and click `Projects`.

<p align="center">
  <img alt="Click on (☰) Menu, then Projects" src="https://user-images.githubusercontent.com/8854447/74561833-61279100-4f37-11ea-8f79-10d73d53c0f8.png">
</p>

Click on `New project`.

<p align="center">
  <img alt="Start a new project" src="https://user-images.githubusercontent.com/8854447/74561927-9fbd4b80-4f37-11ea-8e0a-c0cc73b70db4.png">
</p>

Click on the top tile for `Create an empty project`.

<p align="center">
  <img alt="Create an empty project" src="https://user-images.githubusercontent.com/8854447/74562006-cda29000-4f37-11ea-9e85-c38ecfc68058.png">
</p>

Give the project a unique name and click `Create`.

<p align="center">
  <img alt="Pick a name" src="https://user-images.githubusercontent.com/8854447/74562085-ff1b5b80-4f37-11ea-9e8d-03771fa2f918.png">
</p>


## 2. Add the dataset and custom library zip to the assets section of your project

Once the project has been created, you can upload the dataset and the custom library to the assets section of the project.

The dataset and custom library are housed in a Git repository and you can obtain these by using the following `git clone` command.

```bash
git clone https://github.com/IBM/ReturnPropensity/
cd ReturnPropensity
```

Back on IBM Cloud Pak for Data, within your project, go to the `Assets` tab or click the `01/00` icon to open the `Load` tab.

Then either drag the `TON_PREV_NEW.csv` file from the cloned repository to the window or navigate to it using `browse for files to upload`:

<p align="center">
  <img alt="Add data set" src="https://user-images.githubusercontent.com/8854447/74562517-ff682680-4f38-11ea-9156-f98d561434c0.png">
</p>

Next, load the custom library by either dragging the `CustTrans-0.2.zip` file from the cloned repository to the window or navigate to it using `browse for files to upload`.

Once both files have been uploaded, you should see them listed under **Data Assets** in the Assets tab.

<p align="center">
  <img alt="View Uploaded data assets" src="https://user-images.githubusercontent.com/8854447/74562855-8917f400-4f39-11ea-8e2c-3a076a5cd07e.png">
</p>


## 3. Add the notebook to your project

Within your project on IBM Cloud Pak for Data, click the `+Add to project` button, and choose `Notebook` in the modal that opens.

<p align="center">
  <img alt="Add notebook-1" src="https://user-images.githubusercontent.com/8854447/74563276-705c0e00-4f3a-11ea-950a-b8c301dff6a5.png">
</p>

Alternatively, if the *Notebooks* section already exists on the **Assets** tab of your project, click `+ New notebook` to the right of *Notebooks*.

<p align="center">
  <img alt="Add notebook-2" src="https://user-images.githubusercontent.com/8854447/74564395-0002bc00-4f3d-11ea-9800-93cb3e9370cb.png">
</p>

On the next screen, select the **From file** tab, choose the `Default Python 3.6` environment and click on `Choose file`. 

<p align="center">
  <img alt="Upload notebook" src="https://user-images.githubusercontent.com/8854447/74564502-33454b00-4f3d-11ea-8e0e-2440ce1950ce.png">
</p>

Navigate to and select the `ReturnRiskPandas.jupyter-py36.ipynb` file in the cloned repository. Then click on `Create Notebook`.

<p align="center">
  <img alt="Create notebook" src="https://user-images.githubusercontent.com/8854447/74563755-7b636e00-4f3b-11ea-81c7-a19fa4be4bfb.png">
</p>

When the Jupyter notebook is loaded and the kernel is ready, you can start executing cells.

<p align="center">
  <img alt="Notebook loaded" src="https://user-images.githubusercontent.com/8854447/74564591-638ce980-4f3d-11ea-9f0a-57b33055a1a7.png">
</p>

> **Important**: *Make sure that you stop the kernel of your notebook(s) when you are done, in order to conserve memory resources!*

You will have to unlock the notebook before you can stop the kernel. On the **Assets** tab of your project, under the `Notebooks` section, find the row for the notebook named `ReturnRiskPandas.jupyter-py36` and click on the lock icon on the far right. In the modal that is displayed, click `Unlock`.

<p align="center">
  <img alt="Unlock notebook" src="https://user-images.githubusercontent.com/8854447/74564246-9edae880-4f3c-11ea-928b-5966efc8ad3c.png">
</p>

Next, click on the overflow menu for the `ReturnRiskPandas.jupyter-py36` notebook (right next to where the lock icon previously was) and select `Stop Kernel`.

<p align="center">
  <img alt="Stop kernel" src="https://user-images.githubusercontent.com/8854447/74564056-1f4d1980-4f3c-11ea-8201-6e6dd5b58db9.png">
</p>


## 4. Follow the steps in the notebook

Spend a minute looking through the sections of the notebook to get an overview.

You can run cells individually by highlighting each cell, and then clicking the `Run` button at the top of the notebook. While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (e.g. `[17]`).

<p align="center">
  <img alt="Run single cell" src="https://user-images.githubusercontent.com/8854447/74751814-caf7b180-523b-11ea-89ed-aa57c9bbb3e6.png">
</p>

Alternatively, you can go to `Cell` -> `Run All` to simply run all the cells one after the other. 

<p align="center">
  <img alt="Run all cells" src="https://user-images.githubusercontent.com/8854447/74752088-27f36780-523c-11ea-8ca5-5da6fd48a096.png">
</p>


### i. Load and preprocess the data

In the first few cells of the notebook, we will be loading and preprocessing the input data. The data is first imported into the notebook in step 1.0. It is then cleaned and preprocessed in step 2.0. As part of the cleaning and preprocessing, we do the following:

1. Replace all NAs and empty values with 0.
2. Convert columns with data type = "object" into category codes.
3. Find out how many of the orders were returned and how many were not.
4. Split the data into training and test sets.

In step 3.0, the custom transformer model provided in this repo is installed. We also need the sklearn-pandas library for this pattern, so this library is also installed.


### ii. Build the model

The cells in step 4.0 of the notebook contain the code that builds our prediction model using the custom library installed in step 3.0 and the data that was imported and preprocessed in steps 1.0 and 2.0.

For building the model, we do the following:

1. Create the custom pipeline transformer.
2. Pass the training set from the input data through transformer(fit), i.e. training the model.
3. Evaluate the accuracy of the model using the test set from the input data.


### iii. Save and deploy the model

Cells in step 5.0 of the notebook perform the following actions:

1. Create a WML API client.

You first need to create a Watson Machine Learning API Client. In the cell under `Add in the credentials as per your IBM Cloud Pak for Data cluster.`, replace the existing url, username and password with the url, username and password for your ICP4D cluster.

2. Create and specify a default deployment space.

Before deploying a model, we need to create a deployment space within which our model will be stored and deployed.

You can use the cell under `Use the following cell to perform any clean up of previously created models, deployments and spaces.` to clean up any lingering (previously created) deployment spaces, models and deployments.

You can then use the next few cells to create a new deployment space called "ReturnPropensity_Space" and set it as the default deployment space. 

3. Create a custom python runtime with the custom transformer library installed.

Another thing we need to do before deploying the model is to create a custom python runtime environment and install our custom transformer library in this environment. The cells in step 5.2 of the notebook perform these actions.

4. Store the model.

The cells in step 5.3 of the notebook walk through the process of storing the model in the default space.

5. Deploying the model.

The cells in step 5.4 of the notebook perform the process of deploying our stored model. This process takes some time and at the end, you should get a message saying `Successfully finished deployment creation`. The message will also display the deployment_uid which is needed to test out the model.


## 5. Test the model

There are 3 ways in which the model can be tested.

1. Test from within the notebook.

You can test the model from within the notebook by calling the client.deployments.score() method. It makes use of the deployment_uid that was displayed after successful deployment of the model in step 5.4 of the notebook.

The cells under step 6.0 of the notebook perform the following actions while trying to test the model:
* The deployment_uid is obtained.
* A scoring payload is created. The payload is the json representation of a sample order and this order's information will be provided as the test data to the model.
* The client.deployments.score() method is called to calculate the probability of return for the order represented by the scoring payload.

The result returned by the client.deployments.score() method contains the following pieces of information:
* the prediction of the model (0 = order will not be returned, 1 = order will be returned) for the given test input data.
* the probabilities of getting a prediction of 0 and 1 respectively for the given test input data.

2. Test using the ICP4D built-in tooling.

IBM Cloud Pak for Data offers built-in tooling to quickly test out Watson Machine Learning models.

For this, go to the (☰) menu and click `Analyze` -> `Analytics deployments`.

<p align="center">
  <img alt="Analytics deployments" src="https://user-images.githubusercontent.com/8854447/74755367-15c7f800-5241-11ea-99d2-e78c323004cb.png">
</p>

Click on *ReturnPropensity_Space* which is the deployment space that we had created and within which we had stored and deployed our model.

<p align="center">
  <img alt="View ReturnPropensity_Space" src="https://user-images.githubusercontent.com/8854447/74755885-ca621980-5241-11ea-80d3-1b86188179b5.png">
</p>

Click on the *Deployments* tab and then click on *ReturnRiskPandas_CustomTransformers_v0.2* which is the name we provided for the deployment.

<p align="center">
  <img alt="View deployed model" src="https://user-images.githubusercontent.com/8854447/74756175-2d53b080-5242-11ea-803a-dd5dfba0c26f.png">
</p>

Click on the *Test* tab and paste the contents of the [test_input.json](./test_input.json) file into the *Enter input data* cell. Click `Predict` which will call the model with the input data.

<p align="center">
  <img alt="Insert test input" src="https://user-images.githubusercontent.com/8854447/74756580-c4b90380-5242-11ea-8a4b-27398f088d1d.png">
</p>

The results will be displayed in the *Result* cell. Line 9 indicates the prediction of the model (0 = order will not be returned, 1 = order will be returned. Lines 11 and 12 show the probabilities of getting a prediction of 0 and 1 respectively for the given test input data.

<p align="center">
  <img alt="View prediction results" src="https://user-images.githubusercontent.com/8854447/74756760-182b5180-5243-11ea-8954-b3369ab8baad.png">
</p>


3. Test using cURL.

> NOTE: Windows users will need the *cURL* command. It's recommended to [download gitbash](https://gitforwindows.org/) for this, as you will also have other tools and you will be able to easily use the shell environment variables in the following steps.

In a terminal window, run the following to get a token to access the API. Use your IBM Cloud Pak for Data cluster's `url`, `username` and `password`:

```bash
curl -k -X GET https://<cluster-url>/v1/preauth/validateAuth -u <username>:<password>
```

A json string will be returned with a value for "accessToken" that will look *similar* to this:

```json
{
    "username":"sandy",
    "role":"Admin",
    "permissions": [
        "access_catalog",
        "administrator",
        "manage_catalog",
        "can_provision"
    ],
    "sub":"sandy",
    "iss":"KNOXSSO",
    "aud":"DSX",
    "uid":"1000331002",
    "authenticator":"default",
    "accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNjb3R0ZGEiLCJyb2xlIjoiQWRtaW4iLCJwZXJtaXNzaW9ucyI6WyJhY2Nlc3NfY2F0YWxvZyIsImFkbWluaXN0cmF0b3IiLCJtYW5hZ2VfY2F0YWxvZyIsImNhbl9wcm92aXNpb24iXSwic3ViIjoic2NvdHRkYSIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMxMDAyIiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJpYXQiOjE1NzM3NjM4NzYsImV4cCI6MTU3MzgwNzA3Nn0.vs90XYeKmLe0Efi5_3QV8F9UK1tjZmYIqmyCX575I7HY1QoH4DBhon2fa4cSzWLOM7OQ5Xm32hNUpxPH3xIi1PcxAntP9jBuM8Sue6JU4grTnphkmToSlN5jZvJOSa4RqqhjzgNKFoiqfl4D0t1X6uofwXgYmZESP3tla4f4dbhVz86RZ8ad1gS1_UNI-w8dfdmr-Q6e3UMDUaahh8JaAEiSZ_o1VTMdVPMWnRdD1_F0YnDPkdttwBFYcM9iSXHFt3gyJDCLLPdJkoyZFUa40iRB8Xf5-iA1sxGCkhK-NVHh-VTS2XmKAA0UYPGYXmouCTOUQHdGq2WXF7PkWQK0EA",
    "_messageCode_":"success",
    "message":"success"
}
```

Export the "accessToken" part of this response in the terminal window as `WML_AUTH_TOKEN`. 

```bash
export WML_AUTH_TOKEN=<value-of-access-token>
```

Next go to the *API reference* tab on ICP4D and get the `URL` for the deployment by copying the `Endpoint`, and export it as `URL`:

<p align="center">
  <img alt="View prediction results" src="https://user-images.githubusercontent.com/8854447/74758288-237f7c80-5245-11ea-9c0f-ca3beb5b94de.png">
</p>

```bash
export URL=<endpoint-from-ICP4D>
```

Now run the following curl command from a terminal window. Remember to replace `<filepath-to-test-input-json>` with the path to the local copy of the [test_input.json](./test_input.json) file.

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d @<filepath-to-test-input-json> $URL
```

Alternatively you can simply paste the contents of the [test_input.json](./test_input.json) file in the curl command as shown below:

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data": [{"fields": ["BASKET_SIZE","EXTN_COMPOSITION","CARRIER_SERVICE_CODE_OL","CATEGORY","COUNTRY_OF_ORIGIN_OI","DAY_OF_MONTH","DAY_OF_WEEK","DAY_OF_YEAR","EXTN_BRAND","EXTN_DISCOUNT_ID","EXTN_IS_GIFT","EXTN_IS_PREORDER","EXTN_SHIP_TO_CITY","EXTN_SHIP_TO_COUNTRY","EXTN_SEASON","LIST_PRICE","MONTH_OF_YEAR","OTHER_CHARGES","OTHER_CHARGES_OL","REQ_DELIVERY_DATE","TOTAL_AMOUNT_USD","WEEKEND","ZIP_CODE","MTS_CTS","HOUR_OF_DAY","LOCKID"],"values": [[3, "91% Nylon, 9% Elastercell","STANDARD","Bikini","US",18,"Saturday",322,"XYZAI","None","N","N","Los Angeles","US","FW17",75,11,0.0,0.0,0,165.35,1,"Zipcode_401",24,19,277]]}]}' $URL
```

A json string similar to the one below will be returned.

```bash
{
    "predictions": [
        {
            "fields": [
                "prediction", 
                "probability"
            ], 
            "values": [
                [
                    0, 
                    [
                        0.6666666666666666, 
                        0.3333333333333333
                    ]
                ]
            ]
        }
    ]
}
```

The first numeric value after "values" indicates the prediction of the model (a 0 indicates that the order will not be returned, a 1 indicates that the order will be returned). The next 2 values indicate the probabilities of getting a prediction of 0 or 1 respectively.


## 6. Create a Python Flask app that uses the model

You can also access the web service directly through the REST API. This allows you to use your model for inference in any of your apps. For this code pattern, we will be using a Python Flask application to collect information, score it against the model, and show the results.


### Install the dependencies

The general recommendation for Python development is to use a virtual environment ([`venv`](https://docs.python.org/3/tutorial/venv.html)). To install and initialize a virtual environment, use the `venv` module on Python 3 (you install the virtualenv library for Python 2.7):

In a terminal, go to the cloned repo directory.

```bash
cd ReturnPropensity
```

Initialize a virtual environment with [`venv`](https://docs.python.org/3/tutorial/venv.html).

```bash
# Create the virtual environment using Python. Use one of the two commands depending on your Python version.
# Note, it may be named python3 on your system.
python -m venv venv       # Python 3.X
virtualenv venv           # Python 2.X

# Source the virtual environment. Use one of the two commands depending on your OS.
source venv/bin/activate  # Mac or Linux
./venv/Scripts/activate   # Windows PowerShell
```

> **TIP** To terminate the virtual environment use the `deactivate` command.

Finally, install the Python requirements.

```bash
cd flaskapp
pip install -r requirements.txt
```


### Update environment variables

It is a best practice to store configurable information as environment variables, instead of hard-coding any important information. To reference our model and supply an API key, we will pass these values into the application via a file that is read; the key-value pairs in this file are stored as environment variables.

Copy the `env.sample` file to `.env`.

```bash
cp env.sample .env
```

Edit `.env` to reference the `URL` and `TOKEN`.

* `URL` is your web service URL for scoring. This is the same value as the `Endpoint` that was obtained from ICP4D when testing the model using cURL. (It was exported as the $URL variable in the terminal.)
* `TOKEN` is your deployment access token. This is the same value as the `access token` that was obtained using a bash command when testing the model using cURL. (It was exported as the $WML_AUTH_TOKEN variable in the terminal.)

```bash
# Required: Provide your web service URL for scoring.
# E.g., URL=https://9.10.222.3:31843/dmodel/v1/project/pyscript/tag/score
URL=

# Required: Provide your web service deployment access token.
#           This TOKEN will be the part after `accessToken`. So, your
#           json string will look like:
#           {"username":"sandy","role":"Admin","permissions":["administrator","can_provision","manage_catalog","virtualize_transform","access_catalog"],"sub":"sandy","iss":"KNOXSSO","aud":"DSX","uid":"1000331001","authenticator":"default","accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2 <snip> neQ","_messageCode_":"success","message":"success"}
# The value for `TOKEN=` below will be:
#    TOKEN=eyJhbGciOi <snip> neQ

TOKEN=
```


### Start the application

Start the flask server by running the following command:

```bash
python returnPropensity.py
```

Use your browser to go to [http://localhost:5000](http://localhost:5000) and try it out.

> **TIP**: Use `ctrl`+`c` in the terminal to stop the Flask server when you are done.


#### Sample output

The user inputs various values:

<p align="center">
  <img alt="Input data" src="https://user-images.githubusercontent.com/8854447/74766931-f1c1e200-5253-11ea-9fa9-e9947b5cbce8.png">
</p>

The return propensity is returned:

<p align="center">
  <img alt="View prediction results" src="https://user-images.githubusercontent.com/8854447/74768300-52eab500-5256-11ea-8632-9a8f98f235cf.png">
</p>


# Learn more

* **IBM Sterling Order Management**: Interested in learning more about IBM Sterling Ordeer Management? Check out this series on how to manage [Growing Order Data](https://developer.ibm.com/components/sterling/series/growing-order-data-is-it-really-an-issue-blog-series).
* **Learn about IBM Sterling**: Enjoyed this Code Pattern? Check out code patterns, blogs, articlees and series on IBM Sterling products at [IBM Sterling on IBM Developer](https://developer.ibm.com/components/sterling/).
* **Artificial Intelligence Code Patterns**: Enjoyed this Code Pattern? Check out our other [AI Code Patterns](https://developer.ibm.com/technologies/artificial-intelligence/).
* **Data Analytics Code Patterns**: Enjoyed this Code Pattern? Check out our other [Data Analytics Code Patterns](https://developer.ibm.com/technologies/data-science/).
* **AI and Data Code Pattern Playlist**: Bookmark our [playlist](https://www.youtube.com/playlist?list=PLzUbsvIyrNfknNewObx5N7uGZ5FKH0Fde) with all of our Code Pattern videos.
* **With Watson**: Want to take your Watson app to the next level? Looking to utilize Watson Brand assets? [Join the With Watson program](https://www.ibm.com/watson/with-watson/) to leverage exclusive brand, marketing, and tech resources to amplify and accelerate your Watson embedded commercial solution.
* **IBM Watson Studio**: Master the art of data science with IBM's [Watson Studio](https://www.ibm.com/cloud/watson-studio).


# License

This code pattern is licensed under the Apache Software License, Version 2.  Separate third party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the Developer [Certificate of Origin, Version 1.1 (DCO)](https://developercertificate.org/) and the [Apache Software License, Version 2](http://www.apache.org/licenses/LICENSE-2.0.txt).

Check the [ASL FAQ link](http://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN) for more details.