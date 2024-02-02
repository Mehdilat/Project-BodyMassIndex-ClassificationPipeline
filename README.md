# Body Mass Index (BMI) Machine Learning Classification Pipeline

<!--
add which ml models
-->

Body Mass Index (BMI) is a simple and widely-used method for estimating an individual's body fat based on their weight and height. Despite its simplicity, BMI provides a reasonably accurate representation of body fat for most people and is used to categorize individuals into various weight ranges, such as underweight, normal weight, overweight, and obese. These categories help medical professionals assess potential health risks related to weight and guide individuals in understanding their own health status. Although BMI doesn't measure body fat directly, its ease of calculation and interpretation makes it an indispensable tool in public health to identify weight-related health issues at an individual and population level. The BMI Machine Learning Classification Pipeline aims to harness the power of data and machine learning to predict BMI categories, facilitating a better understanding of health trends and aiding in the early detection and prevention of related health conditions.

In this project, the ["500 Person Gender-Height-Weight-Body Mass Index"](https://www.kaggle.com/datasets/yersever/500-person-gender-height-weight-bodymassindex) dataset available on Kaggle is utilized, encompassing data from 500 individuals, categorized by gender, height, and weight. The objective is to employ this dataset to train and evaluate various machine learning models such as Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Random Forests, and XGBoost, based on their accuracy. The highest-performing model is then integrated into a Flask Application Programming Interface (API). This API is containerized using Docker and pushed to [Docker Hub](https://hub.docker.com/repository/docker/mehdilat/bmi_ml/general), ensuring a seamless deployment process, and is subsequently hosted on Amazon Web Services (AWS) Elastic Compute Cloud (EC2). The deployed model is accessible at the following URL: .



This repository hosts a machine learning project that utilizes the ["500 Person Gender-Height-Weight-Body Mass Index"](https://www.kaggle.com/datasets/yersever/500-person-gender-height-weight-bodymassindex) dataset from Kaggle. The project encompasses the development, training, evaluation, and deployment of machine learning models to categorize individuals based on their BMI, using their gender, height, and weight data.

## Project Objectives

The primary goal is to apply machine learning techniques to accurately predict the BMI category. The project focuses on the following machine learning models:
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Random Forests
- XGBoost

The models are trained and evaluated, with the best-performing model being selected for deployment.

## Model Deployment

The top model is seamlessly integrated into a Flask Application Programming Interface (API). The deployment process involves:

### Containerization

- The Flask API, along with the machine learning model, is containerized using Docker, ensuring consistency and ease of deployment.
- The Dockerized application is hosted on Docker Hub. You can find the container in [Docker Hub](https://hub.docker.com/repository/docker/mehdilat/bmi_ml/general).

### Cloud Hosting

- The application is deployed on AWS Elastic Compute Cloud (EC2), leveraging its scalability and reliability.
- Access the deployed model through this URL: [http://13.38.251.38:5000/](http://13.38.251.38:5000/).
