# fast-api-template

FastAPI is a high performance simple framework for building APIs(Application Programming Interface).

## Setup

**Important:** *More info [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)*

* **`Linux`** Systems:

    ```shell
    #sudo pip3 install virtualenv

    python3 -m venv ./venv

    source venv/bin/activate

    pip3 install fastapi uvicorn

    #pip3 install -r requirements.txt
    ```

    ```shell
    deactivate
    ```

* **`Windows`** Systems:

    ```shell
    #pip3 install virtualenv

    python3 -m venv ./venv

    venv\Scripts\activate

    pip3 install fastapi uvicorn

    #pip3 install -r requirements.txt
    ```

    ```shell
    venv\Scripts\deactivate
    ```

    If getting issue on `windows`, use administrator privileges

## Running

* Using from command line

    ```shell
    python3 app.py
    ```
    or
    ```shell
    uvicorn app:app --reload
    ```

    * [http://127.0.0.1/](http://127.0.0.1/) You can then navigate to the localhost to see your app in action.
    * [http://127.0.0.1/docs](http://127.0.0.1/docs) This yields the OpenAPI Swagger UI.
    * [http://127.0.0.1/redoc](http://127.0.0.1/redoc) This uses the Redoc UI with some documentations out of the box.

## Results



## CREDITS

>Kuldeep Singh Sidhu

Github: [github/singhsidhukuldeep](https://github.com/singhsidhukuldeep)
`https://github.com/singhsidhukuldeep`

Website: [Kuldeep Singh Sidhu (Website)](http://kuldeepsinghsidhu.com)
`http://kuldeepsinghsidhu.com`

LinkedIn: [Kuldeep Singh Sidhu (LinkedIn)](https://www.linkedin.com/in/singhsidhukuldeep/)
`https://www.linkedin.com/in/singhsidhukuldeep/`
