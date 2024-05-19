# lightvisontest
Interview test of Light Vision Inc
author: Do Duy Manh

I. Requirements:

QUESTION 2:
We have lots of problem with image data. So we need to check whether you can handle it or not.
Please make API program to save and query it. And make script file to save image from internet.
(A. API Program / B. Data Insert and Query Script)

    (A. API Program)
    1. Make DBMS Table with ORM.
    2. Make API to save and query the data.
    3. Check the Query API.

    (B. Data Insert and Query Script)
    1. Make script to store the data with your API.
    2.1. Get the Any image data from tensorflow Image classification site. 
    Ex) https://www.tensorflow.org/datasets/catalog/beans?hl=ko
    2.2. Save image data with your API.

II. Result.
    More detail in /documentation/project_specification.pptx

    1. Backend server
    API:
        save: Save an image from the url that you add.
        upload: Upload an image from local.
        list: Get list of the images information that are stored in database.
        get: Download an image from database.
        remove: Remove an image in database.
    * More detail in /documentation/api_specification.json.
        Step 1: open https://editor-next.swagger.io/
        Step 2: Click File/import file. Select file /documentation/api_specification.json

    2. Database postgres server:
        name: lvtest
        user: lvtest
        password: lvtest
        host: pgdb
        port: 5432

        Table: 
            lvtest_image:
                id: Integer - Unique
                text_id: UUID
                image: path to image
                name: String
                source: String
                filetype: String
                create_at: Datetime
                update_at: Datetime

        
    3. Script to get image dataset from tensorflow image classification and call backend api

    Functions:
        - Download Image dataset from tensorflow Image classification.
        - Call backend API to save and query image.


III. Test instruction
    1. Setup environment, download needed library.
    2. Run project with docker desktop.
    3. Run file /script/scripts.py to launch project.