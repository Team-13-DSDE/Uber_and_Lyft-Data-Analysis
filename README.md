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

3. **AWS Glue Database Creation and Crawling**:
   - Follow the steps outlined in [this section](#aws-glue-database-creation-and-crawling) to create a Glue database and crawl the datasets.

4. **Crawling Data to Athena**:
   - Follow the steps outlined in [this section](#crawling-data-to-athena) to crawl the datasets into Athena.

5. **Exporting to Power BI with Athena ODBC**:
   - Follow the steps outlined in [this section](#exporting-to-power-bi-with-athena-odbc) to export the data to Power BI using Athena ODBC.

## Usage

1. **Analyzing Data with Power BI**:
   - Open Power BI Desktop.
   - Connect to the Athena dataset using the ODBC driver.
   - Start analyzing the data and creating visualizations.



