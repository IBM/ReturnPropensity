# Predict return propensity using IBM Cloud Pak for data and Watson Machine Learning

As part of our Intelligent Sterling Call Center Solution, our AI Assistant can surface real time insights about the customer's orders, based on the customer's order history and previous transactions. It also provides actionable recommendations to  provide easy resolutions to common customer issues leading to an enhanced customer experience. Machine Learning models and techniques are used on the aggregated customer data from multiple data sources, to gain customer insights like Customer Life time Value, Churn, Return Propensity, Upsell Purchase Probability. These help the Call Center executive to know the customer better, and take better business decisions like Upsell, Cross-sell, Customer appeasement during a customer conversation. In this code pattern we'll walk you through how to build a simple model to predict the propensity of an order to be returned (Return Propensity).

In the growing era of e-commerce, products being returned amounts to a large portion of the lost revenue. Hence the sonner we can identify the chance of an order being returned the better it is at reducing the loss revenue, directly and indirectly in the form of lost customers. In this code pattern we leverage IBM Cloud Pak for Data with Watson Machine Learning, which enables the customers to build and deploy models in a cloud environment of their choice (Hybrid or Private).

When you have completed this code pattern, you will understand how to:

* Leverage ICP4D, Watson Studio and Watson Machine Learing to build and deploy machine learning models
* Build a model to classify returns.
* Generate predictions using the deployed model by making ReST calls.

# Architecture Diagram
TBD
![]()


## Included components

* [IBM Cloud Pak for Data](https://www.ibm.com/analytics/cloud-pak-for-data):Deploy a complete data and AI private cloud with all the necessary infrastructure and software components in a matter of hours. Natively built on Red Hat OpenShift Container Platform, Cloud Pak for Data System provides optimized hardware to increase container performance, while also accelerating time to value of your data workloads.

* [IBM Watson Machine Learning](https://www.ibm.com/cloud/machine-learning):Watson Machine Learning makes it easy and cost-effective to deploy AI and machine learning assets in public, private, hybrid or multicloud environments. Seamlessly scale up your AI initiatives, growing pilot projects into business-critical enterprise deployments without large up-front investments.

* [IBM Watson Studio](https://www.ibm.com/cloud/watson-studio): Analyze data using RStudio, Jupyter, and Python in a configured, collaborative environment that includes IBM value-adds, such as managed Spark.
  
# Watch the Video

TBD

# Steps to build and deploy the model on ICP4D

Follow these steps to setup and run this code pattern:

1. [Create a 6 node instance with ICP4D](#1-create-an-icp4d-cluster)
1. [Install WML add-on to IPC4D cluster](#2-install-wml-addon-to-icp4d-cluster)
1. [Create a project on ICP4D](#3-create-a-project)
1. [Add the dataset and custom library zip to the assets section of your project](#4-add-assets-to-project)
1. [Create a new notebook and import the code](#5-create-a-notebook-import-notebook)
1. [Build the model](#6-build-the-model)
1. [Create the custom runtime in WML](#7-create-custom-runtime)
1. [Deploy the model](#8-deploy-model)
1. [Test the scoring endpoint](#9-test-scoring-endpoint)


# License

This code pattern is licensed under the Apache Software License, Version 2.  Separate third party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the Developer [Certificate of Origin, Version 1.1 (DCO)](https://developercertificate.org/) and the [Apache Software License, Version 2](http://www.apache.org/licenses/LICENSE-2.0.txt).

Check the [ASL FAQ link](http://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN) for more details
