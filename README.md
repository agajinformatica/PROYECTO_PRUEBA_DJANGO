
# PROYECTO_PRUEBA_DJANGO
TAREA PARA ENTREVISTA PYTHON



# CRM de Clientes – Proyecto Técnico con Django

**Autor:** Arnold Jonatan Alvarado Giron  
**Email:** aj.alvarado.giron@gmail.com  

**Celular:** 993390916


**Ubicación:** Perú  
**Tecnologías:** Python, Django, SQLite, Faker  
**Rol:** Desarrollador Full Stack en formación

---

## 🎯 Objetivo del Proyecto

Este proyecto fue desarrollado como parte de una prueba técnica para el puesto de **Desarrollador Python Django**. El enfoque principal fue demostrar habilidades en:

- Diseño y modelado de base de datos
- Creación de vistas tipo CRM
- Carga masiva de datos realistas
- Manipulación de grandes volúmenes de datos (< 500,000 registros)
- Aplicación de filtros, ordenamientos y presentación de datos amigable

---

## 🛠️ Tecnologías Usadas

| Tecnología | Uso principal |
|-----------|----------------|
| **Django 5.2.3** | Framework backend |
| **SQLite** | Base de datos de desarrollo |
| **Faker** | Generación de datos ficticios |
| **HTML + CSS** | Plantilla CRM |
| **Python 3.12** | Lenguaje de programación base |

---

## 🧱 Arquitectura del Proyecto

El sistema se estructura en torno a 4 modelos:

- **User:** Representantes de ventas (modelo extendido de `AbstractUser`)
- **Company:** Compañías a las que pertenecen los clientes
- **Customer:** Clientes asignados a una compañía y a un representante
- **Interaction:** Registro de llamadas, emails, SMS, redes sociales, etc.

---

## 🔢 Carga Masiva de Datos

Para simular un entorno real, implementé un comando personalizado:

```bash
python manage.py populate_data


🖥️ Vista Principal – Estilo CRM
La aplicación muestra una vista tipo CRM con las siguientes características:

📌 Funcionalidades
📋 Lista de clientes con:

Nombre completo

Compañía

Cumpleaños ("Febrero 5")

Última interacción ("1 day ago (SMS)")

🔍 Filtros:

Buscar por nombre

Filtrar clientes con cumpleaños esta semana

🔃 Ordenamiento:

Por nombre

Por compañía

Por cumpleaños

Por última interacción

🧪 Usuarios de prueba
Los usuarios se generan automáticamente:

user1@test.com

user2@test.com

user3@test.com

Contraseña para todos: 123456
# Clona el repositorio
git clone <URL_DEL_REPOSITORIO>
cd crm_project
## Crea y activa entorno virtual
python -m venv venv
venv\Scripts\activate  # En Windows
### Instala las dependencias
pip install -r requirements.txt
####  Aplica migraciones: 
python manage.py migrate

##### Carga los datos ficticios:
python manage.py populate_data
###### Ejecuta el servidor
python manage.py runserver
####### Accede desde el navegador
http://127.0.0.1:8000




Estoy construyendo mi perfil como desarrollador full stack, con experiencia en backend Python/Django y aprendiendo tecnologías como React, TypeScript y bases de datos avanzadas.

Este reto fue una gran oportunidad para demostrar cómo abordo soluciones técnicas de manera ordenada, modular y escalable.

💻 Perfil profesional en constante crecimiento

💻 Perfil profesional en constante crecimiento

