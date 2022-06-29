# Breve explicación
Django Ninja es una app para Django que permite integrar Pydantic, dataclasses y type hints de forma más amigable en Django, consiguiendo una sintaxis similar a lo que ofrece FastAPI a la hora de implementar los endpoints, pero con todas las baterías incluidas de un framework maduro como Django y su ORM.

## Proyecto
### Misc
Se integró Black, precommit, isort, flake8 y Mypy. Herramientas que permiten un desarrollo ordenado y homogéneo.

### Cliente/Front
El proyecto cuenta con un cliente realizado en Angular 13 y Bootstrap muy básico pero seguro, implementando Guards (previniendo Broken Access Control y navegaciones indebidas) y JWT como método de autentificación.

### DB
Como motor de base de datos se optó por PostgreSQL.

### API/Backend
Se divide en 3 capas simples:

1. **Endpoints**: donde se implementan los endpoints de la API. Cada función se encarga únicamente de llamar al servicio correspondiente y de armar la Response.
2. **Services**: donde se implementa la lógica de negocio y se resuelven las peticiones realizadas por la capa de endpoints.
3. **Models**: ORM de Django.

Los **schemas** son utilizados por Django Ninja para validar y formatear la data entrante y saliente de los endpoints, permitiendo una buena integración con los IDEs y editores gracias a typehints.

Las **políticas** implementadas exponen métodos de consulta de los modelos según el usuario loggeado que intenta acceder a la información, previniendo vulnerabilidades tipo IDOR.
