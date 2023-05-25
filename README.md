# MESA DE AYUDA
<hr>

## INSTALLATION

## clone  repository use

```bash
git clone https://github.com/joserafaelpm/MesaDeAyudaBackend.git
```
#### Create and Activate Environment
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```
#### Install requirements.txt
```bash
pip install -r requirements.txt
```
## RUN SERVER
```bash
python manage.py runserver
```
# ENDPOINTS

|ACTION|METHOD|SUFIX|
|------|------|----|
|LOGIN SUBJECT|GET|api/token/
|REFRESH LOGIN|GET|/api/token/refresh/
|CREATE USER|POST|usuarios/usuarios/
|LIST USERS|GET|usuarios/usuarios/
|GET USER BY ID|GET|/usuarios/usuario/{id}
|UPDATE USER|PUT|/usuarios/usuario/{id}
|DELETE USER BY ID|DELETE|/usuarios/usuario/{id}
|CREATE ROL|POST|usuarios/roles/
|LIST ROLES|GET|usuarios/roles/
|GET ROL BY ID|GET|/usuarios/rol/{id}
|UPDATE ROL|PUT|/usuarios/rol/{id}
|DELETE ROL BY ID|DELETE|/usuarios/rol/{id}
|CREATE CATEGORY|POST|actividades/categorias/
|LIST CATEGORIES|GET|actividades/categoriaS/
|GET CATEGORY BY ID|GET|/actividades/categoria/{id}
|UPDATE CATEGORY|PUT|/actividades/categoria/{id}
|DELETE CATEGORY BY ID|DELETE|/actividades/categoria/{id}
|CREATE ACTIVITY|POST|actividades/actividades/
|LIST ACTIVITIES|GET|actividades/actividades/
|GET ACTIVITY BY ID|GET|/actividades/actividad/{id}
|UPDATE ACTIVITY|PUT|/actividades/actividad/{id}
|DELETE ACTIVITY BY ID|DELETE|/actividades/actividad/{id}
|CREATE TECNICO|POST|actividades/tecnicos/
|LIST TECNICOS|GET|actividades/tecnicos/
|GET TECNICO BY ID|GET|actividades/tecnico/{id}
|UPDATE TECNICO|PUT|actividades/tecnico/{id}
|DELETE TECNICO BY ID|DELETE|actividades/tecnico/{id}
|CREATE ESTADO|POST|solicitudes/estados/
|LIST ESTADOS |GET|solicitudes/estados/
|GET ESTADO BY ID|GET|solicitudes/estado/{id}
|UPDATE ESTADO|PUT|solicitudes/estado/{id}
|DELETE ESTADO BY ID|DELETE|solicitudes/estado/{id}
|CREATE SOLICITUDES|POST|solicitudes/solicitudes/
|LIST SOLICITUDES |GET|solicitudes/solicitudes/
|GET SOLICITUDES BY ID|GET|solicitudes/solicitud/{id}
|UPDATE SOLICITUDES|PUT|solicitudes/solicitud/{id}
|DELETE SOLICITUDES BY ID|DELETE|solicitudes/solicitud/{id}
