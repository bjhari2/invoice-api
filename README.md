# Invoice API

API for CRUD operations on invoice details

## Endpoints available for the API
<ul>
<li>/invoices/ - To fetch all the invoices</li>
<li>/invoices/&ltint:pk&gt - To perform CRUD operations on the invoice detail with the given id</li>
</ul>

## Steps to get the repo working

<ul>
	<li>Clone the repo</li>
	<li>Setup a MySQL database named <code>invoice</code>. Edit the database credentials and other details as required in the <code>settings.py</code> file in the <code>invoice</code> folder.</li>
	<li>Create a virtual environment <br>

    python -m venv /path/to/new/virtual/environment
    
</li>

<li>Activate the virtual environment. (<code>&ltvenv&gt</code> must be replaced by the path to the directory containing the virtual environment)
    <ul>
	<li>In Command prompt 

    C:\> <venv>\Scripts\activate.bat
    
</li>
	<li>In PowerShell

    PS C:\> <venv>\Scripts\Activate.ps1
</li>
	<li>In bash/zsh (MacOS)
	
    $ source <venv>/bin/activate
</li>
</ul>
</li>
<li>Run the following command:

```bash
pip install -r /path/to/requirements.txt
```
</li>
<li>In the folder containing the file <code>manage.py</code> make and run migrations.

```bash
python manage.py makemigrations
python manage.py migrate
```
</li>
<li>Start the server with the following command:

```bash
python manage.py runserver
```
</li>
</ul>
