# Uber & Lyft Data Analysis 

## Overview

Brief overview of the project, its objectives, and the datasets used.

## Dataset Download

https://www.kaggle.com/datasets/brllrb/uber-and-lyft-dataset-boston-ma 

## Local Setup

 **Importing Datasets**:
   - Place the downloaded Uber and Lyft datasets in the `data` directory.

## AWS Setup

1. **AWS Account**:
   - Sign up for an AWS account if you haven't already.

2. **S3 Bucket Creation**:
   - Create an S3 bucket in your AWS account to store the datasets.
   - Before creating a crawler, ensure you have public data in your S3 bucket.
   - Upload the downloaded dataset to your bucket.
   - Create a role that allows crawlers to access your S3 bucket.
   - Follow the steps mentioned below to create a crawler, specifying the S3 path where your data is stored.

3. **AWS Glue Database Creation and Crawling**:
   - In AWS Glue, you can use a crawler to populate the AWS Glue Data Catalog with tables. 
     To add a crawler using the AWS Glue console:
   - Go to the AWS Glue Console.
   - Click on “Crawlers” in the left-hand navigation menu.
   - Click the “Add crawler” button.
   - Provide a name for your crawler and click “Next”.
   - Select “Data stores” as the data store type and choose “S3” as the data store.
   - Enter the S3 path where your data is stored and click “Next”.
   - On the “Configure the crawler’s output” screen, choose “Database” as the output and create a new database to store the metadata catalog.
   - Click “Finish” to create the crawler.
     
4. **Crawling Data to Athena**:
   -AWS Glue crawlers help discover schema information for datasets and register them as tables in the AWS Glue Data Catalog.
   To set up a crawler:
   - Provide a name for the crawler.
   - Choose data sources and add custom classifiers to ensure AWS Glue recognizes the data correctly.
   - Configure an IAM role for the crawler to run processes correctly.
   - Create a database to hold the dataset2.
5. **Exporting to Power BI with Athena ODBC**:
   - Here are the steps to achieve this integration:

   - Install the Athena ODBC Driver:
   First, ensure you have the Amazon Athena ODBC driver installed on your system. You can download it based on your system’s bit version.
   Launch Power BI Desktop:
   Open Power BI Desktop on your machine.
   - Get Data:
   Click on File and select Get Data from the Home ribbon.
   - Search for Athena:
   In the search box, type “Athena”.
   Select Amazon Athena and click Connect.
   - Configure Connection:
   On the Amazon Athena connection page, provide the following information:
   For DSN, enter the name of the ODBC DSN you want to use (configure this beforehand).
   - Choose an appropriate Data Connectivity mode:
   For smaller datasets, select Import. This imports selected tables and columns into Power BI Desktop.
   For larger datasets, choose DirectQuery. In this mode, no data is copied; Power BI queries the underlying data source directly.
   - Authentication:
   When prompted to configure data source authentication, choose either Use Data Source Configuration or AAD Authentication.
   Click Connect.
   - Select Dataset:
   Your data catalog, databases, and tables will appear in the Navigator dialog box.
   In the Display Options pane, select the checkbox for the dataset you want to use.

## Usage

1. **Analyzing Data with Power BI**:
   - Open Power BI Desktop.
   - Connect to the Athena dataset using the ODBC driver.
   - Start analyzing the data and creating visualizations.



